from typing import Callable
from PIL import Image, ImageDraw
import cv2
import numpy as np

BG = (0xEE,) * 3
FG = (0x18,) * 3


def ease_in(x: float) -> float:
    return max(0, 1.2 * x * x - 0.2)


def apply_rule(points: list, rule: list):
    lst = []
    for i in range(len(points)):
        a = points[i]
        b = points[(i + 1) % len(points)]
        lst.append(a)

        d = (b[0] - a[0], b[1] - a[1])

        lst.extend(
            (
                a[0] + pn[0] * d[0] - pn[1] * d[1],
                a[1] + pn[0] * d[1] + pn[1] * d[0],
            )
            for pn in rule
        )

    return lst


class FractalRenderer:
    def __init__(
        self,
        points: list,
        rule: list,
        iter_n: int = 5,
        size: tuple[int, int] = (1920, 1080),
        ppu: float = 600.0,
    ):
        self.points = points
        self.rule = rule
        self.iter_n = iter_n
        self.size = size
        self.ppu = ppu

    def translate_points(self, points: list) -> list:
        avg_x = sum(p[0] for p in points) / len(points)
        avg_y = sum(p[1] for p in points) / len(points)
        return [
            (
                self.size[0] // 2 + (p[0] - avg_x) * self.ppu,
                self.size[1] // 2 - (p[1] - avg_y) * self.ppu,
            )
            for p in points
        ]

    def render(self) -> Image.Image:
        img = Image.new("RGB", self.size, BG)
        draw = ImageDraw.Draw(img)

        points = self.points[:]

        for _ in range(self.iter_n):
            points = apply_rule(points, self.rule)

        points = self.translate_points(points)
        draw.polygon(points, outline=FG, width=3)

        return img


def render_animation(
    points: list,
    rule: Callable[[float], list],
    iter_n: int = 5,
    size: tuple[int, int] = (1920, 1080),
    fps: int = 60,
    iter_dur: float = 1.0,
    fname: str = "output",
    save_last: bool = True,
):
    print("rendering", fname)
    # the number of frames per iteration
    iter_frames = int(fps * iter_dur)

    fourcc = cv2.VideoWriter.fourcc(*"mp4v")
    video = cv2.VideoWriter(f"{fname}.mp4", fourcc, fps, size)

    img = Image.new("RGB", size)
    for it in range(iter_n + 1):
        print(it + 1, "/", iter_n + 1)
        for i in range(iter_frames):
            x = ease_in((i + 1) / iter_frames)

            img = FractalRenderer(
                points=points,
                rule=rule(x),
                iter_n=int(it != 0),
                size=size,
                ppu=int(min(size) * 0.6 * (1 if it != 0 else x)),
            ).render()

            frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            video.write(frame)

        if it != 0:
            points = apply_rule(points, rule(1))

    if save_last:
        img.save(fname + ".png", "PNG")

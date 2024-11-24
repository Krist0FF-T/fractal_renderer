from math import sin, pi
from fractal_renderer import render_animation


SIZE = (1920*2, 1080*2)
NAME = "out/rajz"
N = 6


def rule(x: float) -> list:
    x = max(0, 1.2*x*x - 0.2)
    s = sin(pi/8)
    return [
        (s, -s/2*x),
        (0.5, s/2*x),
        (1-s, -s/2*x),
    ]


points = [
    (0, 1),
    (1, 1),
    (1, 0),
    (0, 0),
]

render_animation(
    points, rule, N, SIZE, fname=NAME
)

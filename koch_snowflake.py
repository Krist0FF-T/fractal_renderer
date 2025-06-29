from math import sin, pi
from fractal_renderer import render_animation


def rule(x: float) -> list:
    a = x / 3
    return [
        (0.5 - a / 2, 0),
        (0.5, sin(pi / 3) * a),
        (0.5 + a / 2, 0),
    ]


if __name__ == "__main__":
    render_animation(
        points=[
            (0, 0),
            (1, 0),
            (0.5, -sin(pi / 3)),
        ],
        rule=rule,
        iter_n=6,
        size=(1920, 1080),  # [::-1],
        fname="out/koch",
    )

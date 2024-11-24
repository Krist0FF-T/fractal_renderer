from math import sin, pi
from fractal_renderer import render_animation


SIZE = (1920*2, 1080*2)
NAME = "out/koch"
N = 6


def rule(x: float) -> list:
    a = max(0, 1.2*x*x - 0.2) / 3
    return [
        (0.5 - a/2, 0),
        (0.5, sin(pi/3)*a),
        (0.5 + a/2, 0),
    ]


points = [
    (0, 0),
    (1, 0),
    (0.5, -sin(pi/3))
]

render_animation(
    points, rule, N, SIZE, fname=NAME
)

from math import sin, pi, sqrt, cos
from fractal_renderer import render_animation


SIZE = (1920, 1080)
NAME = "out_1080p/rajz"
N = 6


def rule(x: float) -> list:
    a = sqrt(2)/2
    top = a - 0.5
    bottom = a/2 * cos(pi/8) - 0.5
    d = sin(pi/8) * a/2
    return [
        (0.5-d*x, bottom*x),
        (0.5, top*x),
        (0.5+d*x, bottom*x),
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

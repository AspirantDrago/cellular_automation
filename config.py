import dataclasses

import pygame as pg


@dataclasses.dataclass
class Padding:
    top: int
    right: int
    bottom: int
    left: int


class Config:
    # размеры
    COLUMNS = 50
    ROWS = 50

    CELL_SIZE = 12
    TITLE = 'Game of Life'

    PADDING = Padding(10, 10, 10, 10)

    WIDTH = COLUMNS * CELL_SIZE + PADDING.left + PADDING.right
    HEIGHT = COLUMNS * CELL_SIZE + PADDING.top + PADDING.bottom
    SIZE = (WIDTH, HEIGHT)

    BACKGROUND_COLOR = pg.color.Color(255, 255, 255)

    FPS = 15

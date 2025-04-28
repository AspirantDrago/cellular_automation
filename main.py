import pygame as pg

from config import Config

from src.life_agent import LifeAgent
from src.life_view import LifeView
from src.life_model import LifeModel

pg.init()
screen = pg.display.set_mode(Config.SIZE)


def main() -> None:
    clock = pg.time.Clock()
    running = True
    model = LifeModel(
        rows=Config.ROWS,
        cols=Config.COLUMNS
    )
    view = LifeView(model=model, cell_size=Config.CELL_SIZE)
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        screen.fill(Config.BACKGROUND_COLOR)
        model.update()
        screen.blit(view.render(), (Config.PADDING.left, Config.PADDING.top))
        pg.display.flip()
        clock.tick(Config.FPS)


if __name__ == "__main__":
    main()
    pg.quit()

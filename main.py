import pygame as pg

from cellular_automation import Automation, Agent
from config import Config

pg.init()
screen = pg.display.set_mode(Config.SIZE)


def main() -> None:
    clock = pg.time.Clock()
    running = True
    model = Automation(
        rows=Config.ROWS,
        cols=Config.COLUMNS,
        agent_class=Agent
    )
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        screen.fill(Config.BACKGROUND_COLOR)

        pg.display.flip()
        clock.tick(Config.FPS)


if __name__ == "__main__":
    main()
    pg.quit()

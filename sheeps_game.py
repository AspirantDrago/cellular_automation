import pygame as pg

from config import Config

from sheeps.sheep_view import SheepView
from sheeps.sheep_model import SheepModel
from sheeps.agents import *

pg.init()
screen = pg.display.set_mode(Config.SIZE)


def main() -> None:
    clock = pg.time.Clock()
    running = True
    model = SheepModel(
        rows=Config.ROWS,
        cols=Config.COLUMNS,
        count_sheep=10
    )
    view = SheepView(model=model, cell_size=Config.CELL_SIZE)
    plot = model.create_plot()
    plot.x_label = 'время'
    plot.y_label = 'количество'
    plot.title = 'График игры "Овцы"'
    plot.get_line(EmptyAgent.STATUS).visible = False
    plot.get_line(GrassAgent.STATUS).color = "#05FF47"
    plot.get_line(GrassAgent.STATUS).set_name('трава')
    plot.get_line(SheepAgent.STATUS).color = "#FF9BAD"
    plot.get_line(SheepAgent.STATUS).set_name('овцы')

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        screen.fill(Config.BACKGROUND_COLOR)
        model.update()
        screen.blit(view.render(), (Config.PADDING.left, Config.PADDING.top))
        screen.blit(plot.render((400, 600)), (620, 0))
        pg.display.flip()
        clock.tick(Config.FPS)
        pg.display.set_caption(f'Игра "Овцы" FPS: {int(clock.get_fps())}')


if __name__ == "__main__":
    main()
    pg.quit()

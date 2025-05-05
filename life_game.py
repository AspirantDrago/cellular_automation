import pygame as pg

from config import Config

from life.life_view import LifeView
from life.life_model import LifeModel
from life.life_agent import AgentStatus

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
    plot = model.create_plot()
    plot.x_label = 'время'
    plot.y_label = 'количество'
    plot.title = 'График игры "Жизнь"'
    plot.get_line(AgentStatus.LIVE).color = 'green'
    plot.get_line(AgentStatus.ALIVE).color = 'black'
    plot.get_line(AgentStatus.LIVE).set_name('живые')
    plot.get_line(AgentStatus.ALIVE).set_name('не живые')
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
        pg.display.set_caption(f'Игра "Жизнь" FPS: {int(clock.get_fps())}')


if __name__ == "__main__":
    main()
    pg.quit()

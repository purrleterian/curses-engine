from engine import Engine
import curses
import curses.textpad


def main(stdscr):
    game_window = stdscr.subpad(
        stdscr.getmaxyx()[0], stdscr.getmaxyx()[1]-30, 0, 0)

    game = Engine(game_window)

    stdscr.bkgd(ord(" "), curses.color_pair(1))
    stdscr.refresh()

    text_area = curses.newwin(
        stdscr.getmaxyx()[0], 30, 0, stdscr.getmaxyx()[1]-30)

    text_area.box()
    text_area.refresh()

    # Game Loop #
    # --------- #

    while game.running:
        game.update()
        text_area.refresh()

    text_area.refresh()
    game.screen.refresh()


if __name__ == "__main__":
    curses.wrapper(main)

import curses
from player import Player


class Engine:
    def __init__(self, screen):
        self.running = True
        self.screen = screen

        self.height, self.width = self.screen.getmaxyx()

        self.screen.clear()
        self.screen.nodelay(1)
        curses.curs_set(0)

        # Initialize Colors #
        # ----------------- #

        # RED
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

        # GREEN
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

        # BLUE
        curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)

        # YELLOW
        curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)

        # PURPLE
        curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

        self.new()

    def new(self):
        """ Runs when a new instance is created. Here is where shit is initialized """

        self.player = Player(self, 5, 5)

    def draw(self):
        """ Prepare to render stuff """
        self.screen.bkgd(".", curses.color_pair(2))
        self.screen.box()

        self.player.draw()

        self.screen.refresh()

    def events(self):
        """ Handles input """
        key = self.screen.getch()
        if key == ord("q"):
            self.running = False
            curses.endwin()

        elif key == curses.KEY_RESIZE:
            self.screen.erase()

        self.player.move(key)

        self.screen.refresh()
        self.screen.clear()

    def update(self):
        """ Puts everything together """
        self.events()
        self.draw()

        curses.napms(1)

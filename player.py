import curses


class Player:
    def __init__(self, game, x, y):
        self.game = game
        self.screen = game.screen

        self.character = "@"
        self.x = x
        self.y = y

    def draw(self):
        try:
            self.screen.addch(self.y, self.x, self.character,
                              curses.color_pair(5))
            self.screen.refresh()

        except curses.error:
            pass

    def move(self, key):
        if key == curses.KEY_LEFT:
            self.x -= 1

        if key == curses.KEY_RIGHT:
            self.x += 1

        if key == curses.KEY_UP:
            self.y -= 1

        if key == curses.KEY_DOWN:
            self.y += 1

        # --------------------------------------------------- #

        if self.x > self.game.width - 2:
            self.x = self.game.width - 2

        elif self.y > self.game.height-2:
            self.y = self.game.height-2

        if self.x < 1:
            self.x = 1

        elif self.y < 1:
            self.y = 1

#!/usr/bin/python3

import pygame
import random
import logging

from qni_core import logger, base_game, pygame_utils



class ElectrodesTest(base_game.BaseGame):
    _logger = logging.getLogger('electrodes_test')
    RELEASED_COLOR = (0, 20, 0)

    def __init__(self):
        base_game.BaseGame.__init__(self)

    def __loop__(self, pygame_events, time_diff):
        # randomly colorize newly touched electrodes
        for i in self.electrodes.get_newly_touched():
            self._logger.info('elec %s,\t%s', i.index, i.grid_indexes)
            pygame.draw.ellipse(
                self.window_surface, pygame_utils.get_rand_color(), i.rect,
                random.randrange(4))
        # colorize newly released electrodes with RELEASED_COLOR
        for i in self.electrodes.get_newly_released():
            pygame.draw.ellipse(
                self.window_surface, self.RELEASED_COLOR, i.rect)


def main():
    app = ElectrodesTest()
    app.mainloop()


if __name__ == '__main__':
    main()

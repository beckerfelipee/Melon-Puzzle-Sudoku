import functions as fc
import variables as var
import grid


def set_var():
    var.colours = True
    var.cheats = True
    var.tips = True


def start_game():
    var.user = fc.set_user()
    grid.detect_save()
    grid.start_grid()


def run():
    start_game()
    fc.moves()


set_var()
run()

import variables as var
import time


def elapsed_time(moment, win):
    if moment == "start":
        var.start_time = time.time()
    if moment == "end":
        var.end_time = time.time()
        current_time = open("db_elapsed_time.txt", "r")
        tdb_close = current_time
        var.start_l = 0
        for line in current_time:
            if line == var.user + "'s Elapsed time \n" or line == var.user + "'s Elapsed time\n":
                break
            else:
                var.start_l += 1

        count = len(open("db_elapsed_time.txt", "r").readlines())
        if var.start_l != count:
            var.saved = 1
        else:
            var.saved = 0

        if var.saved == 0:
            e_time = var.end_time - var.start_time
            e_time = "%.3f" % e_time             # Para diminuir as casas decimais
            append = open("db_elapsed_time.txt", "a")
            L = ["\n", var.user + "'s Elapsed time \n", str(e_time), "\n"]
            append.writelines(L)
            append.close()
        else:
            current_time = open("db_elapsed_time.txt", "r")
            current_time = current_time.readlines()
            current_time = current_time[var.start_l + 1]
            tdb_close.close()
            current_time = float(current_time)
            e_time = (var.end_time - var.start_time) + current_time
            e_time = "%.3f" % e_time
            lines = open("db_elapsed_time.txt", "r").readlines()
            if win == 1:
                lines[var.start_l] = var.user + "'s Winner's time \n"
            else:
                lines[var.start_l] = var.user + "'s Elapsed time \n"
            var.e_time = e_time
            lines[var.start_l + 1] = str(e_time)
            open("db_elapsed_time.txt", "w").write("".join(lines))

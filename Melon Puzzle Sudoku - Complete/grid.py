import time
import variables as var
import functions as fc

# stats temporárias
slot = "x"
save = 0


def count_slots():
    grids_db = open("db_grid_default.txt", "r")
    grids_db = grids_db.readlines()
    grids_db = str(grids_db)
    count = grids_db.count("Slot")
    var.slot_count = count


def invalid_slot():
    fc.skip(1, "run")
    print("Erro:\n  Você precisa digitar o número do Slot!")
    time.sleep(1)
    var.no_slot = True


def choose_slot():
    var.no_slot = True
    count_slots()

    # escolher slot
    while var.no_slot:
        print("\nCaso você não tenha personalizado um Tabuleiro nos arquivos do jogo, o Slot 1 é o recomendado")
        slot = input("Digite o número do slot que você deseja carregar para seu novo jogo: ")
        try:
            while int(slot) < 1 or int(slot) > var.slot_count:
                slot = input("Você precisa inserir um número de 1 a " + str(var.slot_count) + ": ")
            var.slot = str(slot)
            if var.slot != "1":
                time.sleep(1)
                print("\nVocê tem certeza que deseja selecionar o Slot "+slot+"?")
                print("Slots não recomendados podem não ter solução.")
                fc.yes_or_no()
                if var.yes:
                    var.no_slot = False
                    fc.skip(1, "run")
                else:
                    var.no_slot = True
                    fc.skip(1, "run")
            else:
                var.no_slot = False
                fc.skip(1, "run")
        except ValueError:
            invalid_slot()


def find_line(option, x):
    if option == "slot":
        grids_db = open("db_grid_default.txt", "r")
        var.start_l = 1
        for line in grids_db:
            if line == "Slot " + var.slot + "\n":
                break
            else:
                var.start_l += 1
        grids_db.close()

    elif option == "save":
        saved_db = open("db_grid_autosave.txt", "r")
        var.start_l = 0 + x
        for line in saved_db:
            if line == var.user + "'s Grid \n":
                break
            else:
                var.start_l += 1
        saved_db.close()


def transform_to_grid(archive, type, style):

    # transformar slot em grid calculável

    grids_db = open(archive, type)
    gdb_close = grids_db
    grids_db = grids_db.readlines()
    grids_db = grids_db[var.start_l:var.start_l + 10]
#    print(grids_db)
    n = 0  # linhas

    #  Tirar "\n"

    while n < 9:
        gpop = grids_db[n].index('\n')
        grids_db[n] = list(grids_db[n])
        gdb_n = grids_db[n]
        gdb_n.pop(gpop)

        #  Tirar "," e " "

        x = 0  # vírgulas
        y = 0  # espaços
        x_count = gdb_n.count(',')
        y_count = gdb_n.count(' ')
        while x < x_count:
            gpop = gdb_n.index(',')
            gdb_n.pop(gpop)
            while y < y_count:
                gpop = gdb_n.index(' ')
                gdb_n.pop(gpop)
                y += 1
            x += 1

        #  Transformar os números em inteiros

        z = 0  # números
        while z < 9:
            if gdb_n[z] == "-":  # Caso o número seja negativo
                gdb_n[z] = gdb_n[z] + gdb_n[z+1]
                gdb_n.remove(gdb_n[z+1])
            gdb_n[z] = int(gdb_n[z])
            z += 1
        n += 1

    #  Transformar em grid usável
    if style == "set":
        grids_db.pop()
    elif style == "load":
        pass
    var.grid = grids_db
    gdb_close.close()


def set_grid():
    choose_slot()
    find_line("slot", 0)
    transform_to_grid("db_grid_default.txt", "r", "set")


def detect_save():
    find_line("save", 0)
    count = len(open("db_grid_autosave.txt", "r").readlines())
#    print(var.start_l)   Apenas para confirmar que está funcionando.
#    print(count)                        II
    if var.start_l != count:
        var.saved = 1
    else:
        var.saved = 0


def save_grid(win):
    grid = var.grid

    n = [0]  # Qtd. de números (de 0 a 80)
    while n.count(0) < 81:
        n.append(0)

    x = 0  # linha
    y = 0  # Coluna
    z = 0  # ordem dos números (de 0 a 80)

    while x // 9 < 9:
        while y < 9:
            n[z] = str(grid[x // 9][y])
            y += 1
            z += 1
            x += 1
        y = 0

    z = 0  # ordem dos números (de 9 em 9)
    x = 0  # ordem das linhas (de 0 a 8)
    s = ", "
    p = " \n"

    lin = ["l"]
    while lin.count("l") < 9:
        lin.append("l")

    while z <= 72:
        lin[x] = "," + n[z] + s + n[z + 1] + s + n[z + 2] + s + n[z + 3] + s + n[z + 4] + \
                 s + n[z + 5] + s + n[z + 6] + s + n[z + 7] + s + n[z + 8] + "," + p
        z += 9
        x += 1

    #  Procurar grid com nome de usuário

    find_line("save", 0)
    count = len(open("db_grid_autosave.txt", "r").readlines())

    #  Se ainda não houver grid salvo para o usuário

    if var.start_l == count:
        append = open("db_grid_autosave.txt", "a")
        L = ["\n", var.user + "'s Grid \n", lin[0], lin[1], lin[2], lin[3], lin[4], lin[5], lin[6], lin[7], lin[8]]
        append.writelines(L)
        append.close()

    #  Se já houver grid salvo para o usuário

    else:
        lines = open("db_grid_autosave.txt", "r").readlines()
        if win == 1:
            lines[var.start_l] = var.user + "'s Winner's Grid! \n"
        else:
            lines[var.start_l] = var.user + "'s Grid \n"
        lines[var.start_l + 1] = lin[0]
        lines[var.start_l + 2] = lin[1]
        lines[var.start_l + 3] = lin[2]
        lines[var.start_l + 4] = lin[3]
        lines[var.start_l + 5] = lin[4]
        lines[var.start_l + 6] = lin[5]
        lines[var.start_l + 7] = lin[6]
        lines[var.start_l + 8] = lin[7]
        lines[var.start_l + 9] = lin[8]
        open("db_grid_autosave.txt", "w").write("".join(lines))


def load_grid():
    find_line("save", 1)
    transform_to_grid("db_grid_autosave.txt", "r", "load")


def start_grid():
    if var.saved == 1:
        fc.skip(1, "run")
        print("\n\n\n                                Bem-vindo(a) de volta, " + var.user + "!")
        time.sleep(1)
        print("\n\n                         Você tem um jogo salvo, gostaria de continuá-lo?")
        fc.yes_or_no()
        if var.yes:
            load_grid()
        else:
            fc.skip(1, "run")
            print("\n\n            " + var.user + ", Vamos definir um novo tabuleiro para você!")
            time.sleep(1)
            set_grid()
    else:
        fc.skip(1, "run")
        print("\n\n            " + var.user + ", Vamos definir um tabuleiro para você começar!")
        time.sleep(1)
        set_grid()
    save_grid(0)

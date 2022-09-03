import variables as var
import functions as fc
import time


def trophy():
    print("________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n"
          "________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ \n"
          "___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ \n"
          "_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ \n"
          "¶¶¶¶______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______¶¶¶¶ \n"
          "¶¶¶_______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________¶¶¶            Parabéns, " + var.user + "!!!!\n"
          "¶¶________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________¶¶¶      Você conseguiu completar o Sudoku!\n"
          "¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______¶¶¶ \n"
          "¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶ \n"
          "_¶¶¶___¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶____¶¶¶           Número de movimentos: " + str(var.n_moves) + "\n"
          "_¶¶¶¶___¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶__¶¶¶¶            Tempo decorrido: " + var.final_time + "\n"
          "___¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶ \n"
          "____¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶ \n"
          "______¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶¶¶¶ \n"
          "_______________¶¶¶¶¶¶¶¶¶¶¶¶ \n"
          "_________________¶¶¶¶¶¶¶¶ \n"
          "___________________¶¶¶¶ \n"
          "___________________¶¶¶¶ \n"
          "___________________¶¶¶¶ \n"
          "___________________¶¶¶¶ \n"
          "_______________¶¶¶¶¶¶¶¶¶¶¶¶ \n"
          "____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ \n"
          "____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ \n"
          "____________¶¶¶____________¶¶¶ \n"
          "____________¶¶¶____________¶¶¶ \n"
          "____________¶¶¶____________¶¶¶ \n"
          "____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ \n"
          "____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ \n"
          "__________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶")
    var.to_input = input("_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶                           "
                         "Pressione 'Enter' para finalizar.")


def board():

    n = ['']
    while n.count('') < 81:
        n.append('')

    # Arrumar simetria da board:
    # um n negativo ocupa 2 caracteres [-n], um positivo ocupa apenas 1 [n]

    x = [0]  # linha
    y = [0]  # Coluna
    z = [0]  # ordem dos números (de 0 a 80)

    while x[0] // 9 < 9:
        while y[0] < 9:
            if var.grid[x[0] // 9][y[0]] >= 0:
                n[z[0]] = " " + str(var.grid[x[0] // 9][y[0]])  # [ n]
            else:
                n[z[0]] = str(var.grid[x[0] // 9][y[0]])  # [-n]
            y[0] += 1
            z[0] += 1
            x[0] += 1
        y[0] = 0

    if var.colours:
        reset = "\033[0m"
        blue = "\033[34m"
        yellow = "\033[33m"

        z = [0]
        while z[0] < 81:
            if z[0] == 10 or z[0] == 19 or z[0] == 31 or z[0] == 32 \
                    or z[0] == 48 or z[0] == 49 or z[0] == 61 or z[0] == 70:
                n[z[0]] = blue + n[z[0]] + reset
            else:
                if n[z[0]] != " 0":
                    n[z[0]] = yellow + n[z[0]] + reset
            z[0] += 1
    time.sleep(1)
    if var.slot == "1":
        print("\n\n Melon Puzzle Sudoku:       [Tabuleiro original]")
    else:
        print("\n\n Melon Puzzle Sudoku:")

    print("\n", "      2 -9 -6    -3  0 -3     0  3  0",
          "\n", "   +-----------------------------------+",
          "\n", " 0 |", n[0], n[1], n[2], " |", n[3], n[4], n[5], " |", n[6], n[7], n[8], " |", " Linha 1",
          "\n", "-4 |", n[9], n[10], n[11], " |", n[12], n[13], n[14], " |", n[15], n[16], n[17], " |", " Linha 2",
          "\n", " 3 |", n[18], n[19], n[20], " |", n[21], n[22], n[23], " |", n[24], n[25], n[26], " |", " Linha 3",
          "\n", "   |-----------+-----------+-----------|",
          "\n", " 0 |", n[27], n[28], n[29], " |", n[30], n[31], n[32], " |", n[33], n[34], n[35], " |", " Linha 4",
          "\n", " 6 |", n[36], n[37], n[38], " |", n[39], n[40], n[41], " |", n[42], n[43], n[44], " |", " Linha 5",
          "\n", " 1 |", n[45], n[46], n[47], " |", n[48], n[49], n[50], " |", n[51], n[52], n[53], " |", " Linha 6",
          "\n", "   |-----------+-----------+-----------|",
          "\n", " 0 |", n[54], n[55], n[56], " |", n[57], n[58], n[59], " |", n[60], n[61], n[62], " |", " Linha 7",
          "\n", " 0 |", n[63], n[64], n[65], " |", n[66], n[67], n[68], " |", n[69], n[70], n[71], " |", " Linha 8",
          "\n", " 2 |", n[72], n[73], n[74], " |", n[75], n[76], n[77], " |", n[78], n[79], n[80], " |", " Linha 9",
          "\n", "   +-----------------------------------+")


def menu():
    on_menu = True
    while on_menu:
        fc.skip(1, "run")
        print("\n")
        print("\n                                        Melon Puzzle Sudoku")
        print("\n                                           Menu principal")
        print()
        print("\n                                            [1] Voltar")
        print("\n                                            [2] Opções")
        print("\n                                            [3] Sair")
        option = input("\n\n\n\n              Selecione um número: ")
        if option == "1":
            on_menu = False
        elif option == "2":
            options()
        elif option == "3":
            exit()
        else:
            pass


def options():
    while True:
        if var.colours:
            change_colour = "sem cor"
        else:
            change_colour = "colorido"
        if var.cheats:
            c_action = "Proibir"
        else:
            c_action = "Permitir"
        if var.tips:
            t_action = "Proibir"
        else:
            t_action = "Permitir"

        fc.skip(1, "run")
        print("\n")
        print("\n                                        Melon Puzzle Sudoku")
        print("\n                                           Menu de Opções")
        print()
        print("\n                                            [1] Voltar")
        print("\n                                            [2] Trocar para [" + change_colour + "]")
        print("\n                                            [3] " + c_action + " cheats")
        print("\n                                            [4] " + t_action + " dicas")
        option2 = input("\n\n\n              Selecione um número: ")

        if option2 == "1":
            break
        elif option2 == "2":
            if var.colours:
                var.colours = False
            else:
                var.colours = True
        elif option2 == "3":
            if var.cheats:
                var.cheats = False
            else:
                var.cheats = True
        elif option2 == "4":
            if var.tips:
                var.tips = False
            else:
                var.tips = True
        else:
            pass

import os
import time
import elapsed_time as ep
import variables as var
import movement
import verify
import screens
import grid


def skip(sec, mode):
    # Pula a cena
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    if mode == "command":
        return command
    else:
        time.sleep(sec)
        return os.system(command)


def set_user():
    # Guarda o nome do usuário
    user = input("\n Para começar, insira seu nome: ")
    print("Nome guardado com sucesso...")
    skip(1, "run")
    return user


def yes_or_no():
    answer = input("\n                                    digite [Sim] ou [Não] \n\n"
                   "                                              ")
    var.yes = answer_yes_or_no(answer)


def answer_yes_or_no(answer):
    while answer != "S" and answer != "s" and answer != "N" and answer != "n" and answer != "Sim" and \
            answer != "sim" and answer != "Não" and answer != "não" and answer != "nao" and answer != "Nao":
        answer = input("verifique se digitou corretamente e tente novamente: ")
    if answer == "S" or answer == "s" or answer == "Sim" or answer == "sim":
        return True
    elif answer == "N" or answer == "n" or answer == "Não" or answer == "não" or answer == "nao" or answer == "Nao":
        return False


def compute_final_time(sec, mode):
    h = (sec // 3600)
    h = int(h)
    m = (sec % 3600) // 60
    m = int(m)
    s = (sec % 60)
    s = float("%.3f" % s)
    if mode == "test":
        return h, m, s
    else:
        return str(h) + " horas, " + str(m) + " minutos e " + str(s) + " segundos"


def invalid_int():
    print("\nMovimento invalidado...\n Você só pode inserir números inteiros! ")
    time.sleep(1)
    print("\n Reiniciando movimento..")
    skip(1, "run")
    screens.board()
    return moves()


def moves():
    ep.elapsed_time("start", 0)
    movement.movement()
    verify.verify()


def win():
    skip(1, "run")
    grid.save_grid(1)
    ep.elapsed_time("start", 1)
    ep.elapsed_time("end", 1)
    var.final_time = compute_final_time(float(var.e_time), "run")
    screens.trophy()
    exit()


def try_menu(open_menu, mode):
    if open_menu == "menu" or open_menu == "Menu" or open_menu == "Pause" or open_menu == "pause":
        if mode == "test":
            return "Open"

        else:
            return screens.menu()
    else:
        if mode == "test":
            return "Pass"
        else:
            pass


def easter():
    skip(1, "run")
    ep.elapsed_time("end", 0)
    time.sleep(1)
    print("\nVocê encontrou um segredo! \n\n ")
    time.sleep(1)
    print("Dev: ")
    time.sleep(1)
    print("- Felipe Becker \n")
    sec = 3
    while sec > 0:
        time.sleep(1)
        print(str(sec) + "...")
        sec -= 1
    time.sleep(1)
    win()

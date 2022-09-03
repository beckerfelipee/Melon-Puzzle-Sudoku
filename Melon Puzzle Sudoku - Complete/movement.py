import time
import variables as var
import functions as fc
import screens
import grid


def movement():
    # opção de menu
    open_menu = input("\n Escreva 'menu' para abrir o menu de opções \n Ou pressione [Enter] para continuar\n ")
    fc.try_menu(open_menu, "run")

    # selecionando a linha
    fc.skip(0, "run")
    screens.board()
    sr_prov = input("\n Por favor, digite o número da linha que você quer mudar: ")

    try:
        sr_prov = int(sr_prov)
    except ValueError:
        return fc.invalid_int()

    # O uso do try previne que o jogo encerre por um erro inesperado, diferentemente de apenas usar a opção
    # int(input("")) -> nesse caso, quando se envia um valor que não seja transformável para int (como uma letra),
    # o jogo simplesmente encerra, ao invés de oferecer outra chance de o jogador enviar um número.

    if var.cheats:
        if sr_prov == 57517:
            fc.easter()
    while int(sr_prov) > 9 or int(sr_prov) < 1:
        sr_prov = input(" Você só pode inserir números entre 1 e 9, \n tente novamente: ")  # Aviso
        try:
            sr_prov = int(sr_prov)
        except ValueError:
            return fc.invalid_int()
    sr = sr_prov - 1
    print(" ", var.grid[sr], "-> Linha selecionada")

    # selecionando coluna

    sc_prov = input("\n Por favor, digite a posição (de 1 a 9) do número que você quer mudar: ")
    try:
        sc_prov = int(sc_prov)
    except ValueError:
        return fc.invalid_int()

    while sc_prov > 9 or sc_prov < 1:
        sc_prov = input(" Você só pode inserir números entre 1 e 9, \n tente novamente: ")  # Aviso
        try:
            sc_prov = int(sc_prov)
        except ValueError:
            return fc.invalid_int()
    sc = sc_prov - 1

    # Mudando sinal de Nº pré-posicionado (regra do Melon Puzzle)

    if (sr, sc) == (5, 3) or (sr, sc) == (5, 4) or (sr, sc) == (6, 7) or (sr, sc) == (7, 7) or \
            (sr, sc) == (1, 1) or (sr, sc) == (2, 1) or (sr, sc) == (3, 4) or (sr, sc) == (3, 5):
        print("\n Você gostaria de mudar o sinal de (" + str(var.grid[sr][sc]) + ") ?")
        change_sig = input("Digite 'sim' ou 'não' : ")

        while change_sig != "sim" and change_sig != "Sim" and change_sig != "não" and change_sig \
                != "Não" and change_sig != "nao" and change_sig != "s" and change_sig != "n":
            print("\n Verifique se digitou corretamente e tente novamente:")
            change_sig = input("\n Digite 'sim' ou 'não' : ")

        if change_sig == "sim" or change_sig == "Sim" or change_sig == "s":
            var.grid[sr][sc] = -var.grid[sr][sc]
            fc.skip(1, "run")
            print("\n O sinal do número foi alterado!")
        else:
            fc.skip(1, "run")
            print("\n O sinal do número não foi alterado")

    # Adicionar ou modificar número

    else:
        new_n = input("  digite o novo número: ")
        try:
            new_n = int(new_n)
        except ValueError:
            return fc.invalid_int()

        while new_n > 4 or new_n < -4:
            new_n = input(" Você só pode inserir números entre -4 e 4, \n tente novamente: ")
            try:
                new_n = int(new_n)
            except ValueError:
                return fc.invalid_int()
        var.grid[sr][sc] = new_n
        fc.skip(1, "run")
        print("Número alterado com sucesso..")
        time.sleep(1)
    grid.save_grid(0)
    screens.board()

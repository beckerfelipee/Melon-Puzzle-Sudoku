import time
import variables as var
import functions as fc


def verify():
    grid = var.grid
    dicas = var.tips

    # Definindo Linhas

    r1 = grid[0]
    r2 = grid[1]
    r3 = grid[2]
    r4 = grid[3]
    r5 = grid[4]
    r6 = grid[5]
    r7 = grid[6]
    r8 = grid[7]
    r9 = grid[8]

    # Definindo Colunas

    c1 = grid[0][:1] + grid[1][:1] + grid[2][:1] + grid[3][:1] + \
         grid[4][:1] + grid[5][:1] + grid[6][:1] + grid[7][:1] + grid[8][:1]
    c2 = grid[0][1:2] + grid[1][1:2] + grid[2][1:2] + grid[3][1:2] + \
         grid[4][1:2] + grid[5][1:2] + grid[6][1:2] + grid[7][1:2] + grid[8][1:2]
    c3 = grid[0][2:3] + grid[1][2:3] + grid[2][2:3] + grid[3][2:3] + \
         grid[4][2:3] + grid[5][2:3] + grid[6][2:3] + grid[7][2:3] + grid[8][2:3]
    c4 = grid[0][3:4] + grid[1][3:4] + grid[2][3:4] + grid[3][3:4] + \
         grid[4][3:4] + grid[5][3:4] + grid[6][3:4] + grid[7][3:4] + grid[8][3:4]
    c5 = grid[0][4:5] + grid[1][4:5] + grid[2][4:5] + grid[3][4:5] + \
         grid[4][4:5] + grid[5][4:5] + grid[6][4:5] + grid[7][4:5] + grid[8][4:5]
    c6 = grid[0][5:6] + grid[1][5:6] + grid[2][5:6] + grid[3][5:6] + \
         grid[4][5:6] + grid[5][5:6] + grid[6][5:6] + grid[7][5:6] + grid[8][5:6]
    c7 = grid[0][6:7] + grid[1][6:7] + grid[2][6:7] + grid[3][6:7] + \
         grid[4][6:7] + grid[5][6:7] + grid[6][6:7] + grid[7][6:7] + grid[8][6:7]
    c8 = grid[0][7:8] + grid[1][7:8] + grid[2][7:8] + grid[3][7:8] + \
         grid[4][7:8] + grid[5][7:8] + grid[6][7:8] + grid[7][7:8] + grid[8][7:8]
    c9 = grid[0][8:] + grid[1][8:] + grid[2][8:] + grid[3][8:] + \
         grid[4][8:] + grid[5][8:] + grid[6][8:] + grid[7][8:] + grid[8][8:]

    # Definindo Quadrados

    s1 = grid[0][0:3] + grid[1][0:3] + grid[2][0:3]
    s2 = grid[0][3:6] + grid[1][3:6] + grid[2][3:6]
    s3 = grid[0][6:] + grid[1][6:] + grid[2][6:]
    s4 = grid[3][0:3] + grid[4][0:3] + grid[5][0:3]
    s5 = grid[3][3:6] + grid[4][3:6] + grid[5][3:6]
    s6 = grid[3][6:] + grid[4][6:] + grid[5][6:]
    s7 = grid[6][0:3] + grid[7][0:3] + grid[8][0:3]
    s8 = grid[6][3:6] + grid[7][3:6] + grid[8][3:6]
    s9 = grid[6][6:] + grid[7][6:] + grid[8][6:]

    #  Verificação de números duplicados

    sucess = True
    if dicas:
        print("\n Dicas: ")

    time.sleep(1)

    #                                    Linhas

    if r1.count(-4) > 1 or r1.count(-3) > 1 or r1.count(-2) > 1 or r1.count(-1) > 1 \
            or r1.count(4) > 1 or r1.count(3) > 1 or r1.count(2) > 1 or r1.count(1) > 1:
        if dicas:
            print("Existem números dúplicados na Linha 1")
        sucess = False
    if r2.count(-4) > 1 or r2.count(-3) > 1 or r2.count(-2) > 1 or r2.count(-1) > 1 \
            or r2.count(4) > 1 or r2.count(3) > 1 or r2.count(2) > 1 or r2.count(1) > 1:
        if dicas:
            print("Existem números dúplicados na Linha 2")
        sucess = False
    if r3.count(-4) > 1 or r3.count(-3) > 1 or r3.count(-2) > 1 or r3.count(-1) > 1 \
            or r3.count(4) > 1 or r3.count(3) > 1 or r3.count(2) > 1 or r3.count(1) > 1:
        if dicas:
            print("Existem números dúplicados na Linha 3")
        sucess = False
    if r4.count(-4) > 1 or r4.count(-3) > 1 or r4.count(-2) > 1 or r4.count(-1) > 1 \
            or r4.count(4) > 1 or r4.count(3) > 1 or r4.count(2) > 1 or r4.count(1) > 1:
        if dicas:
            print("Existem números dúplicados na Linha 4")
        sucess = False
    if r5.count(-4) > 1 or r5.count(-3) > 1 or r5.count(-2) > 1 or r5.count(-1) > 1 \
            or r5.count(4) > 1 or r5.count(3) > 1 or r5.count(2) > 1 or r5.count(1) > 1:
        if dicas:
            print("Existem números dúplicados na Linha 5")
        sucess = False
    if r6.count(-4) > 1 or r6.count(-3) > 1 or r6.count(-2) > 1 or r6.count(-1) > 1 \
            or r6.count(4) > 1 or r6.count(3) > 1 or r6.count(2) > 1 or r6.count(1) > 1:
        if dicas:
            print("Existem números dúplicados na Linha 6")
        sucess = False
    if r7.count(-4) > 1 or r7.count(-3) > 1 or r7.count(-2) > 1 or r7.count(-1) > 1 \
            or r7.count(4) > 1 or r7.count(3) > 1 or r7.count(2) > 1 or r7.count(1) > 1:
        if dicas:
            print("Existem números dúplicados na Linha 7")
        sucess = False
    if r8.count(-4) > 1 or r8.count(-3) > 1 or r8.count(-2) > 1 or r8.count(-1) > 1 \
            or r8.count(4) > 1 or r8.count(3) > 1 or r8.count(2) > 1 or r8.count(1) > 1:
        if dicas:
            print("Existem números dúplicados na Linha 8")
        sucess = False
    if r9.count(-4) > 1 or r9.count(-3) > 1 or r9.count(-2) > 1 or r9.count(-1) > 1 \
            or r9.count(4) > 1 or r9.count(3) > 1 or r9.count(2) > 1 or r9.count(1) > 1:
        if dicas:
            print("Existem números dúplicados na Linha 9")
        sucess = False

    #                                         Colunas

    if c1.count(-4) > 1 or c1.count(-3) > 1 or c1.count(-2) > 1 or c1.count(-1) > 1 \
            or c1.count(4) > 1 or c1.count(3) > 1 or c1.count(2) > 1 or c1.count(1) > 1:
        if dicas:
            print("Existem números dúplicados na Coluna 1")
        sucess = False
    if c2.count(-4) > 1 or c2.count(-3) > 1 or c2.count(-2) > 1 or c2.count(-1) > 1 \
            or c2.count(4) > 1 or c2.count(3) > 1 or c2.count(2) > 1 or c2.count(1) > 1:
        if dicas:
            print("Existem números dúplicados na Coluna 2")
        sucess = False
    if c3.count(-4) > 1 or c3.count(-3) > 1 or c3.count(-2) > 1 or c3.count(-1) > 1 \
            or c3.count(4) > 1 or c3.count(3) > 1 or c3.count(2) > 1 or c3.count(1) > 1:
        if dicas:
            print("Existem números dúplicados na Coluna 3")
        sucess = False
    if c4.count(-4) > 1 or c4.count(-3) > 1 or c4.count(-2) > 1 or c4.count(-1) > 1 \
            or c4.count(4) > 1 or c4.count(3) > 1 or c4.count(2) > 1 or c4.count(1) > 1:
        if dicas:
            print("Existem números dúplicados na Coluna 4")
        sucess = False
    if c5.count(-4) > 1 or c5.count(-3) > 1 or c5.count(-2) > 1 or c5.count(-1) > 1 \
            or c5.count(4) > 1 or c5.count(3) > 1 or c5.count(2) > 1 or c5.count(1) > 1:
        if dicas:
            print("Existem números dúplicados na Coluna 5")
        sucess = False
    if c6.count(-4) > 1 or c6.count(-3) > 1 or c6.count(-2) > 1 or c6.count(-1) > 1 \
            or c6.count(4) > 1 or c6.count(3) > 1 or c6.count(2) > 1 or c6.count(1) > 1:
        if dicas:
            print("Existem números dúplicados na Coluna 6")
        sucess = False
    if c7.count(-4) > 1 or c7.count(-3) > 1 or c7.count(-2) > 1 or c7.count(-1) > 1 \
            or c7.count(4) > 1 or c7.count(3) > 1 or c7.count(2) > 1 or c7.count(1) > 1:
        if dicas:
            print("Existem números dúplicados na Coluna 7")
        sucess = False
    if c8.count(-4) > 1 or c8.count(-3) > 1 or c8.count(-2) > 1 or c8.count(-1) > 1 \
            or c8.count(4) > 1 or c8.count(3) > 1 or c8.count(2) > 1 or c8.count(1) > 1:
        if dicas:
            print("Existem números dúplicados na Coluna 8")
        sucess = False
    if c9.count(-4) > 1 or c9.count(-3) > 1 or c9.count(-2) > 1 or c9.count(-1) > 1 \
            or c9.count(4) > 1 or c9.count(3) > 1 or c9.count(2) > 1 or c9.count(1) > 1:
        if dicas:
            print("Existem números dúplicados na Coluna 9")
        sucess = False

    #                                       Quadrados

    if s1.count(-4) > 1 or s1.count(-3) > 1 or s1.count(-2) > 1 or s1.count(-1) > 1 \
            or s1.count(4) > 1 or s1.count(3) > 1 or s1.count(2) > 1 or s1.count(1) > 1:
        if dicas:
            print("Existem números dúplicados no 1º Quadrado")
        sucess = False
    if s2.count(-4) > 1 or s2.count(-3) > 1 or s2.count(-2) > 1 or s2.count(-1) > 1 \
            or s2.count(4) > 1 or s2.count(3) > 1 or s2.count(2) > 1 or s2.count(1) > 1:
        if dicas:
            print("Existem números dúplicados no 2º Quadrado")
        sucess = False
    if s3.count(-4) > 1 or s3.count(-3) > 1 or s3.count(-2) > 1 or s3.count(-1) > 1 \
            or s3.count(4) > 1 or s3.count(3) > 1 or s3.count(2) > 1 or s3.count(1) > 1:
        if dicas:
            print("Existem números dúplicados no 3º Quadrado")
        sucess = False
    if s4.count(-4) > 1 or s4.count(-3) > 1 or s4.count(-2) > 1 or s4.count(-1) > 1 \
            or s4.count(4) > 1 or s4.count(3) > 1 or s4.count(2) > 1 or s4.count(1) > 1:
        if dicas:
            print("Existem números dúplicados no 4º Quadrado")
        sucess = False
    if s5.count(-4) > 1 or s5.count(-3) > 1 or s5.count(-2) > 1 or s5.count(-1) > 1 \
            or s5.count(4) > 1 or s5.count(3) > 1 or s5.count(2) > 1 or s5.count(1) > 1:
        if dicas:
            print("Existem números dúplicados no 5º Quadrado")
        sucess = False
    if s6.count(-4) > 1 or s6.count(-3) > 1 or s6.count(-2) > 1 or s6.count(-1) > 1 \
            or s6.count(4) > 1 or s6.count(3) > 1 or s6.count(2) > 1 or s6.count(1) > 1:
        if dicas:
            print("Existem números dúplicados no 6º Quadrado")
        sucess = False
    if s7.count(-4) > 1 or s7.count(-3) > 1 or s7.count(-2) > 1 or s7.count(-1) > 1 \
            or s7.count(4) > 1 or s7.count(3) > 1 or s7.count(2) > 1 or s7.count(1) > 1:
        if dicas:
            print("Existem números dúplicados no 7º Quadrado")
        sucess = False
    if s8.count(-4) > 1 or s8.count(-3) > 1 or s8.count(-2) > 1 or s8.count(-1) > 1 \
            or s8.count(4) > 1 or s8.count(3) > 1 or s8.count(2) > 1 or s8.count(1) > 1:
        if dicas:
            print("Existem números dúplicados no 8º Quadrado")
        sucess = False
    if s9.count(-4) > 1 or s9.count(-3) > 1 or s9.count(-2) > 1 or s9.count(-1) > 1 \
            or s9.count(4) > 1 or s9.count(3) > 1 or s9.count(2) > 1 or s9.count(1) > 1:
        if dicas:
            print("Existem números dúplicados no 9º Quadrado")
        sucess = False

    #                                       0's Duplicados

    if sucess:
        if r1.count(0) > 1 or r2.count(0) > 1 or r3.count(0) > 1 or r4.count(0) > 1 \
                or r5.count(0) > 1 or r6.count(0) > 1 or r7.count(0) > 1 or r8.count(0) > 1 or r9.count(0) > 1:
            sucess = False
            if dicas:
                print("Existem números 0's duplicados em alguma(s) linha(s)")
        if c1.count(0) > 1 or c2.count(0) > 1 or c3.count(0) > 1 or c4.count(0) > 1 \
                or c5.count(0) > 1 or c6.count(0) > 1 or c7.count(0) > 1 or c8.count(0) > 1 or c9.count(0) > 1:
            sucess = False
            if dicas:
                print("Existem números 0's duplicados em alguma(s) coluna(s)")
        if s1.count(0) > 1 or s2.count(0) > 1 or s3.count(0) > 1 or s4.count(0) > 1 \
                or s5.count(0) > 1 or s6.count(0) > 1 or s7.count(0) > 1 or s8.count(0) > 1 or s9.count(0) > 1:
            sucess = False
            if dicas:
                print("Existem números 0's duplicados em algum(s) quadrado(s)")

    #  Verificação da soma dos 0's (Regra do Melon Puzzle)

    #  Linhas
    if sucess:
        if sum(r1[0:r1.index(0)]) != 0:
            sucess = False
            if dicas:
                print("A soma dos números até o [0] na linha 1 deve ser igual a [0]")
        if sum(r2[0:r2.index(0)]) != -4:
            sucess = False
            if dicas:
                print("A soma dos números até o [0] na linha 2 deve ser igual a [-4]")
        if sum(r3[0:r3.index(0)]) != 3:
            sucess = False
            if dicas:
                print("A soma dos números até o [0] na linha 3 deve ser igual a [3]")
        if sum(r4[0:r4.index(0)]) != 0:
            sucess = False
            if dicas:
                print("A soma dos números até o [0] na linha 4 deve ser igual a [0]")
        if sum(r5[0:r5.index(0)]) != 6:
            sucess = False
            if dicas:
                print("A soma dos números até o [0] na linha 5 deve ser igual a [6]")
        if sum(r6[0:r6.index(0)]) != 1:
            sucess = False
            if dicas:
                print("A soma dos números até o [0] na linha 6 deve ser igual a [1]")
        if sum(r7[0:r7.index(0)]) != 0:
            sucess = False
            if dicas:
                print("A soma dos números até o [0] na linha 7 deve ser igual a [0]")
        if sum(r8[0:r8.index(0)]) != 0:
            sucess = False
            if dicas:
                print("A soma dos números até o [0] na linha 8 deve ser igual a [0]")
        if sum(r9[0:r9.index(0)]) != 2:
            sucess = False
            if dicas:
                print("A soma dos números até o [0] na linha 9 deve ser igual a [2]")

        #  Colunas
        if sum(c1[0:c1.index(0)]) != 2:
            sucess = False
            if dicas:
                print("A soma dos números até o [0] na 1ª coluna deve ser igual a [2]")
        if sum(c2[0:c2.index(0)]) != -9:
            sucess = False
            if dicas:
                print("A soma dos números até o [0] na 2ª coluna deve ser igual a [-9]")
        if sum(c3[0:c3.index(0)]) != -6:
            sucess = False
            if dicas:
                print("A soma dos números até o [0] na 3ª coluna deve ser igual a [-6]")
        if sum(c4[0:c4.index(0)]) != -3:
            sucess = False
            if dicas:
                print("A soma dos números até o [0] na 4ª coluna deve ser igual a [-3]")
        if sum(c5[0:c5.index(0)]) != 0:
            sucess = False
            if dicas:
                print("A soma dos números até o [0] na 5ª coluna deve ser igual a [0]")
        if sum(c6[0:c6.index(0)]) != -3:
            sucess = False
            if dicas:
                print("A soma dos números até o [0] na 6ª coluna deve ser igual a [-3]")
        if sum(c7[0:c7.index(0)]) != 0:
            sucess = False
            if dicas:
                print("A soma dos números até o [0] na 7ª coluna deve ser igual a [0]")
        if sum(c8[0:c8.index(0)]) != 0:
            sucess = False
            if dicas:
                print("A soma dos números até o [0] na 8ª coluna deve ser igual a [3]")
        if sum(c9[0:c9.index(0)]) != 0:
            sucess = False
            if dicas:
                print("A soma dos números até o [0] na 9ª coluna deve ser igual a [0]")
    fc.elapsed_time("end", 0)

    if sucess:
        time.sleep(1)
        fc.win()
        # Vitória!!

    else:
        var.n_moves += 1
        fc.moves()
        # Continuar jogando..

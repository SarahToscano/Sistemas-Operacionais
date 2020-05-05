from operator import itemgetter
import copy
from pythonds.basic.stack import Stack
from decimal import Decimal


def main():
    texto = []
    with open('input.txt') as arq:
        texto = arq.read()

    texto = texto.split()  # quebra os dados de acordo com os espaços
    seq = list(map(int, texto))  # Converte os numeros de string para inteiro
    quadros = seq[0]
    paginas = int(len(seq)-1)  # calcula o numero de paginas
    table = [-1]*quadros

    seq.remove(seq[0])
    seq2 = copy.deepcopy(seq)
    seq3 = copy.deepcopy(seq)
    seq4 = copy.deepcopy(seq)

    faltas_fifo = 0
    faltas_otimo = 0
    faltas_lru = 0

    faltas_fifo = FIFO(paginas, quadros, table, seq2)

    table = [-1] * quadros  # Zera a tabela que foi preenchida pelo FIFO
    faltas_otimo = OTM(paginas, quadros, table, seq3)

    table = [-1] * quadros  # Zera a tabela que foi preenchida pelo OTM
    faltas_lru = LRU(paginas, quadros, table, seq4, seq)

    print("FIFO", faltas_fifo)
    print("OTM", faltas_otimo)
    print("LRU", faltas_lru)


def FIFO(paginas, quadros, table, seq2):
    faltas = 0
    repeticoes = 0
    i = 0

    if (paginas >= quadros):
        # print("seq2:", seq2)
        # print("tabela:", table)
        # print("num de faltas:", faltas, "\n")
        while (len(seq2) > 0):
            while(i < quadros):  # tipo um for
                # if ((len(seq2) > 0)):
                if(not(seq2[0] in table)):
                    # print("movendo:", seq2[0], "para a tabela")
                    faltas += 1
                    table[i] = seq2[0]
                    # print("tabela", table)
                    seq2.remove(seq2[0])
                    # print("sequencia nova:", seq2,"\n")
                    if (len(seq2) == 0):
                        # print("\nnum de faltas:", faltas)
                        return faltas
                else:
                    # print("valor:", seq2[0], "ja existe na tabela")
                    seq2.remove(seq2[0])
                    # print("tabela", table)
                    # print("sequencia nova:", seq2,"\n")
                    if(len(seq2) == 0):
                        # print("\nnum de faltas:", faltas)
                        return faltas
                    else:
                        i -= 1
                i += 1
            i = 0
    else:
        faltas = paginas  # custo da inserção das novas paginas na tabela de quadros
    # print("\nnum de faltas:", faltas)
    return (faltas)


def procura(seq, direcao, table, quadros, historico, seq_original, count_pos):
    ant = 0
    aux = [0]*quadros
    agr = 0
    j = 0
    nada = 0
    indice = 0
    melhor_op = -1
    historico = []
    minimo = 0
    maximo = 0
    # print("----------------------------------------------------------------")
    # Esta função serve tanto para o OTM qnt para o LRU
    # Sua funcionalidade eh a seguinte, dado um indice (posicao de determinado elemento no vetor)
    # Ela procura com base na direcao (direita ou esquerda) qual eh o elemento que mais demora a
    # aparecer e TEM que retornar a posicao deste elemento na tabela de quadros

    # count = posição do valor a a entrar na tabela
    # valor a entrar = pag a ser inserida na tabela
    # direcao pode assumir 2 valores: 0 -> OTM: analisa a partir do count [count, paginas]
    #                                1 -> LRU: analisa a partir 0 até o count  [0, count]
    if(direcao == 0):  # OTM
        for l in range(0, quadros):
            for i in range(0, len(seq)):
                if(not(table[l] in seq)):
                    # print("nao estou ate agr")
                    # Nao faz nada
                    nada += 1
                else:
                    aux[l] += 1
        for l in range(0, quadros):
            if(aux[l] == 0):
                # print("Sua melhor opção eh o valor:",
                # seq[l], "que esta no indice:", l)
                return(l)
        for i in range(0, len(seq)):
            # Achamos uma pagina listada e nao eh a ultima
            if((seq[i] in table) & (len(seq) > 2)):
                # print("Pagina", seq[i], "esta na tabela")
                if(not(seq[i]in historico)):  # A pagina NAO foi chamada outras vezes
                    melhor_op = seq[i]
                    # print("Melhor OP:", melhor_op)
                    ant = seq[i]
                else:
                    # print("Pagina", seq[i], "nao serve")
                    nada += 1
                historico.append(seq[i])
                # print("historico:", historico)
                # print("\n")
            if((i == len(seq)-1)):  # Acabaram as paginas e nenhuma foi encontrada = FIFO
                if(melhor_op == -1):
                    if(j == quadros-1):
                        j = 0
                        indice = j
                        melhor_op = table[j]
                        # print("Sua melhor opção eh o valor:",
                        #      melhor_op, "que esta no indice:", indice)

                    else:
                        indice = j
                        melhor_op = table[j]
                        # print("Sua melhor opção eh o valor:", melhor_op, "que esta no indice:", indice)
                    j += 1
                    # print(
                    #    "Fudeu,Acabaram as paginas e nenhuma foi encontrada fazer FIFO")
                else:
                    for k in range(0, quadros):
                        if(table[k] == melhor_op):
                            indice = k
                # print("Sua melhor opção eh o valor:",
                #      melhor_op, "que esta no indice:", indice)
        # print("----------------------------------------------------------------")
        return(indice)
    ideal = 0
    if(direcao == 1):
        pag = [-1]*len(seq_original)
        for i in range(count_pos-1, -1, -1):
            #print("Percorrendo o array ao ocntrario ")
            #print("sequencia", seq_original)
            #print("i:", i)
            if(seq_original[i] in table):  # Se a pagina da sequencia ainda estiver na tabela
                # Se a pagina n tiver sido indexada no pag
                # print("Pagina", seq_original[i],
                #      "esta na tabela, Pode ser retirada")
                if(not(seq_original[i] in pag)):
                    pag[i] = seq_original[i]
                    #print("Indexou", seq_original[i], "em pag:", i)
                    #print("pag.", pag)
            else:
                pass
        # print(pag)
        maior = max(pag)
        for i in range(0, len(seq_original)):
            if(pag[i] != -1):  # Pega o numero da pagina que esta na posição mais baixa do array
                ideal = pag[i]
                for k in range(0, quadros):
                    if(table[k] == ideal):
                        indice = k
                        #print("A pag a ser retirada da tabela sera", ideal)
                        #print("O indice da pagina sera", indice)
                        return(indice)

        # print("----------------------------------------------------------------")
    return(indice)
# Como o preenchimento dos primeiros valores da tabela de quadros eh igual
# ou seja so há alteração quando há a substituição de paginas, o LRU vai ser preenchido inicialmente
# igual ao OTM, para isso foi criada uma variavel FLAG que vai indicar se o algoritmo do OTM continua a
# preencher a tabela de quadros ou se ele retorna a tabela e a sequencia com os valores iniciais


def OTM(paginas, quadros, table, seq3):
    faltas = 0
    count = 0
    aux = 0
    i = 0
    indice = 0
    historico = []
    # print("Faltas=", faltas, "\n")
    if (paginas >= quadros):
        # print("seq2:", seq3)
        # print("tabela:", table)
        # print("num de faltas:", faltas, "\n")
        while (-1 in table):
            while (i < quadros):  # tipo um for
                if (not (seq3[0] in table)):
                    # print("movendo:", seq3[0], "para a tabela")
                    faltas += 1
                    # print("Faltas=", faltas, "\n")

                    table[i] = seq3[0]
                    # print("tabela", table)
                    seq3.remove(seq3[0])
                    # print("sequencia nova:", seq3, "\n")
                    if (len(seq3) == 0):
                        # print("\nnum de faltas:", faltas)
                        i = quadros+1
                else:
                    seq3.remove(seq3[0])
                    # print("tabela", table)
                    # print("sequencia nova:", seq3, "\n")
                    if (len(seq3) == 0):
                        # print("\nnum de faltas:", faltas)
                        i = quadros+1
                    else:
                        i -= 1
                i += 1
            i = 0
        else:
            i = 0
            # print("tabela", table)
            # print("sequencia nova:", seq3, "\n")
            while (len(seq3) > 0):
                i = 0
                while(i < quadros):
                    # print("[i]:", i)
                    # print(seq3[i], "tem em", table)
                    if(seq3[i] in table):
                        # print("Removendo elemento:", seq3[i])
                        # print("seq ant:", seq3)
                        seq3.remove(seq3[i])
                        # print("seq dps:", seq3, "\n")
                        if (len(seq3) == 0):
                            i = quadros+1
                        else:
                            i -= 1
                    else:
                        # print("\nSem repetiçoes")
                        # print("tabela", table)
                        # print("sequencia nova:", seq3, "\n")
                        indice = procura(
                            seq3, 0, table, quadros, historico, 0, 0)
                        # print("\nVoltei p funcao")
                        # print("table",  table)
                        # print("seq", seq3)
                        # print("Substituir", table[indice], "por", seq3[i])
                        table[indice] = seq3[i]
                        seq3.remove(seq3[i])
                        # print("table", table)
                        # print("seq", seq3)
                        # print(i)
                        # print("\n")
                        faltas += 1
                        # print("Faltas=", faltas, "\n")
                        if (len(seq3) == 0):
                            i = quadros+1
                        else:
                            i -= 1
                    i += 1
                i = 0
    else:
        faltas = paginas  # custo da inserção das novas paginas na tabela de quadros
    # print("\nnum de faltas:", faltas)
    return (faltas)


def LRU(paginas, quadros, table, seq4, seq_original):
    #print("table", table)
    # print(seq4)
    count_pos = 0
    faltas = 0
    i = 0
    historico = []
    if (paginas >= quadros):
        #print("num de faltas:", faltas, "\n")
        while (-1 in table):
            while (i < quadros):  # tipo um for
                if (not (seq4[0] in table)):  # Pagina ainda nao esta na tabela
                    #print("movendo:", seq4[0], "para a tabela")
                    faltas += 1
                    count_pos += 1
                    #print("Faltas=", faltas, "\n")
                    table[i] = seq4[0]
                    #print("tabela", table)
                    seq4.remove(seq4[0])
                    #print("sequencia nova:", seq4, "\n")
                    if (len(seq4) == 0):
                        #print("\nnum de faltas:", faltas)
                        i = quadros + 1
                else:  # Remove a pagina da fila e nao faz alteracao na tabela
                    seq4.remove(seq4[0])
                    count_pos += 1  # Incrementa o indice para o array da sequencia original
                    #print("tabela", table)
                    #print("sequencia nova:", seq4, "\n")
                    if (len(seq4) == 0):
                        #print("\nnum de faltas:", faltas)
                        i = quadros + 1
                    else:
                        i -= 1
                i += 1
            i = 0
        else:
            #print("Tabela completa pela primeira x\n")
            for i in range(0, quadros):
                historico.append(table[i])
            #print("historico:", historico)
            i = 0
            #print("tabela", table)
            #print("sequencia nova:", seq4, "\n")
            while (len(seq4) > 0):
                i = 0
                while (i < quadros):
                    #print("[i]:", i)
                    #print(seq4[i], "tem em", table)
                    if (seq4[i] in table):
                        #print("Removendo elemento:", seq4[i])
                        #print("seq ant:", seq4)
                        seq4.remove(seq4[i])
                        count_pos += 1
                        #print("seq dps:", seq4, "\n")
                        if (len(seq4) == 0):
                            i = quadros + 1
                        else:
                            i -= 1
                    else:
                        #print("\nSem repetiçoes")
                        #print("tabela", table)
                        #print("sequencia nova:", seq4, "\n")
                        indice = procura(seq4, 1, table, quadros, historico,
                                         seq_original, count_pos)
                        #print("\nVoltei p funcao")
                        #print("table", table)
                        #print("seq", seq4)
                        #print("Substituir", table[indice], "por", seq4[i])
                        table[indice] = seq4[i]
                        seq4.remove(seq4[i])
                        #print("table", table)
                        #print("seq", seq4)
                        # print(i)
                        # print("\n")
                        faltas += 1
                        count_pos += 1
                        #print("Faltas=", faltas, "\n")
                        if (len(seq4) == 0):
                            i = quadros + 1
                        else:
                            i -= 1
                    i += 1
                i = 0
    else:
        faltas = paginas  # custo da inserção das novas paginas na tabela de quadros
    #print("\nnum de faltas:", faltas)
    return (faltas)


main()

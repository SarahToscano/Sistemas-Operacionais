from operator import itemgetter
import copy

def FCFO(matriz, processos):
    tempo_espera=0; tempo_retorno=0; tempo_resposta=0
    aux=0; count=0; j=1 #j aponta para a coluna do tempo de saida
    soma_retorno=0; n=processos; linhas=processos
    for i in range (0,linhas):
        if(i==0):
            tempo_espera = 0
            aux = matriz[i][j]
            soma_retorno=n*matriz[i][j] #multiplica o valor pela quantidade de repetições, lógica no README.txt
            soma_retorno-=matriz[i][0]  #retira o valor do tempo de entrada
        else:
            n=n-1
            soma_retorno+=n*matriz[i][j]
            soma_retorno-=matriz[i][0]
            tempo_espera+=aux-matriz[i][0]#retira o tempo de entrada, por isso j=0
            aux+=matriz[i][j]
    tempo_espera=tempo_espera/processos
    tempo_retorno=soma_retorno/processos
    tempo_resposta=tempo_espera

    return tempo_retorno,tempo_resposta,tempo_espera

def RR(matriz,matriz_2, processos, quantum):
    tempo_espera = 0; tempo = 0; tempo_retorno = 0; tempo_resposta = 0
    j = 1; count = 0; aux = 0; index=[]; linhas=processos

    while (count != processos):
        for i in range(0, linhas):
            aux += processos - quantum
            for q in range(0, quantum):  # Rerira somente o que tiver disponivel a partir do quantum
                if (matriz_2[i][j]):
                    #print('aaa',matriz_2)
                    matriz_2[i][j] -= 1  # Retira o tempo do quantum
                    index.append(i + 1)
                    if (matriz_2[i][j] == 0):
                        count += 1
                else:
                    break
    count = 0

    rev = copy.deepcopy(index)
    rev.reverse() #facilita o momento de finalização dos processos
    #print('lista normal :', index)
    #print('lista reversa:', rev)

    i = 0; k = 1; flag = 0
    count = [0] * processos
    soma = [0] * processos
    stop = [0] * processos

    for k in range(1, processos + 1):
        while ((rev[i] != k)):  # percorre a lista ao contrario p achar o momento  em q o processo foi inicializado pela ultima x
            if (i == len(rev)):
                break
            i += 1
        count[k - 1] = i
        i = 0
    # Esse for acha a primeira ocorrencia do processo na lista reversa
    #print('count:', count)
    i = 0

    for k in range(1, processos + 1):
        i = 0
        while (i < len(rev)):
            if (i == 0):  # percorre a partir da 1 ocorrencia
                i = copy.deepcopy(count[k - 1])
            if (rev[i] != k):
                soma[k - 1] += 1
            i += 1
    #print('soma com tempo de entrada: ', soma)  # soma as ocorrencias dos outros processos = a qntdd de tempo na fila

    for k in range(1, processos + 1):
        soma[k - 1] -= matriz[k - 1][0]  # retira o tempo de entrada
    #print('soma sem tempo de entrada: ', soma)

    for k in range(1, processos + 1):
        tempo_espera += soma[k - 1]
        tempo_retorno+=len(rev)-count[k-1] #acha o tempo da ultima execucao do programa

    tempo_espera = tempo_espera / processos
    tempo_retorno=tempo_retorno/processos

    soma=[0]*processos
    i=0;count=0
    #print(index)
    for k in range(1, processos + 1):
        while ((index[i] != k)):  # percorre a lista INDEX p achar o momento  em q o processo foi inicializado pela ultima x
            if (i == len(index)):
                break
            soma[k-1]+=1
            i=i+1
        i=0
    #soma neste momento tem o tempo de inicio da primeira execução dos processos
    count=0
    for k in range(1, processos+1):
        soma[k-1]-=matriz[k-1][0]#retira tempo de entrada
        count+=soma[k-1]#somatorio de 'soma' tempo da primeira execucao de todos os processos
    #print("count", count)
    tempo_resposta=count/processos

    return(tempo_retorno,tempo_resposta,tempo_espera)


def SJF(matriz, linhas):
    tempo_ini = [0]*linhas; duracao=[0]*linhas
    time=0;exec=[0]*linhas; maior=0; menor=0; index=0
    tempo_espera=0;tempo_resposta=0;tempo_retorno=0;acc=0
    output=[0]*3

    for i in range (0, linhas):
        tempo_ini[i] = matriz[i][0]
        duracao[i]=matriz[i][1] #calcula duracao dos processos
    maior=max(tempo_ini)
    time=0; aux=0;count=0

    while(not(all(duracao[i]==0 for i in range (0,linhas)))): #enqt a lista de duracao estiver preenchida
        #print('duracao:', duracao)
        aux=index
        index = 0
        menor = 2048
        for i in range(0, linhas):
            if ((duracao[i]!=0) & (duracao[i]< menor) & (matriz[i][0] <= time)):  # encontra o menor processo ja iniciado
                menor = duracao[i]
                index = i
        #print('menor valor: ', duracao[index])
        if (time > maior):
            if(aux!=index):
                tempo_espera += time - tempo_espera
                #print('processo iniciado: ', index, '   tempo de espera', tempo_espera)
                acc+=tempo_espera-matriz[index][0]
            #print('tempo de entrada ultrapassado')# verifica se o maior tempo de entrada ja foi ultrapassado
            for i in range(0, duracao[index]):
                duracao[index] -= 1  # executa o processo de menor duracao ate zerar
                time += 1
                #print(' -- processo[', index +1, ']: ', duracao[index], '  time:', time)
        else:
            if(duracao[index]>0):
                #print('aux:', aux, 'index:', index) #verifica se não eh o msm processo sendo excutado
                if (aux != index): #mudanca de escalonamento
                    count = 0

                if(count==0):
                    aux=index
                    tempo_espera += time - tempo_espera
                    #print('processo iniciado: ', index, '   tempo de espera', tempo_espera)
                    acc += tempo_espera -matriz[index][0]
                duracao[index] -= 1
                time += 1
                #print(' --> processo[', index+1, ']: ', duracao[index], '   time:', time)
        if(duracao[index]==0):
            tempo_retorno+=time - matriz[index][0]
        count+=1
        #print('')
    tempo_espera=acc/linhas
    tempo_resposta=tempo_espera
    tempo_retorno=tempo_retorno/linhas

    #print('tempo retorno:', tempo_retorno)
    #print('tempo de resposta:', tempo_resposta)
    #print('tempo de espera:', tempo_resposta)

    return(tempo_retorno,tempo_resposta,tempo_espera)


#------------------------------------------------------------------------------------------------------------
def main():
    texto = []
    with open('test.txt') as arq:
        texto = arq.read()

    texto=texto.split() #quebra os dados de acordo com os espaços
    texto_num = list(map(int, texto)) #Converte os numeros de string para inteiro
    #print("Lista:", texto_num)
    linhas = int(len(texto) / 2)  # calcula o numero de processos|linhas
    count=0; n=linhas; quantum=2
    matriz = [];flag=1

    for i in range(0,linhas):
        linha = []
        for j in range(0,2):
            if(j==1):
                if(texto_num[count]==0):
                    print('O processo com duracao nula foi removido do escalonador')
                    flag=0
                    linhas-=1

            linha.append(texto_num[count])
            print("texto:",texto_num[count])
            count=count+1
        if(flag==1):
            matriz.append(linha) #matriz desordenada pelo tempo de entrada do processo
            print("matriz.append:", matriz)
        flag =1

    matriz.sort(key=itemgetter(0)) #Organiza a matriz de acordo com o tempo de entrada ->coluna(0)
    print("Dados:", matriz)


    matriz_2=copy.deepcopy(matriz) #copia da matriz original para poder alterar os valores do tempo de duração
    SJF_v=0

    FCFO_v = (FCFO(matriz,linhas))
    RR_v= (RR(matriz,matriz_2,linhas,quantum))
    SJF_v= (SJF(matriz,linhas))

    #desempactomento de tuplas
    a,b,c=FCFO_v
    d,e,f= SJF_v
    g,h,i= RR_v


    print('\nFCFO', FCFO_v)
    print('SJF', SJF_v)
    print('RR', RR_v)

    with open('output.txt', 'w') as arquivo:
        arquivo.write("FCFS " + str(a) +' ' + str(b) + ' '+ str(c) + "\n")
        arquivo.write("SJF " + str(d) +' ' + str(e) + ' '+ str(f) + "\n")
        arquivo.write("RR " + str(g) +' ' + str(h) + ' '+ str(i) + "\n")


main()











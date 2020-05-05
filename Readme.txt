#Autora: Sarah Andrade Toscano de Carvalho
#Projeto desenvolvido na disciplina de Sistemas Operacionais - UFPB/CI

                      REQUISIÇÕES DO PROJETO:

-> Programa 01: Escalonador de CPU

   Neste projeto você deve implementar um conjunto de algoritmos de escalonamento de CPU e escrever um programa que calcula uma série de      estatísticas baseado nestes algoritmos. ¨ Os algoritmos de escalonamento a serem implementados são os seguintes:
   ¤ FCFS: First-Come, First-Served
   ¤ SJF: Shortest Job First
   ¤ RR: Round Robin (com quantum = 2)

   O seu programa deverá ler de um arquivo uma lista de processos com seus respectivos tempos de chegada e de duração e deverá imprimir na    tela uma tabela contendo os valores para as seguintes métricas:
   ¤ Tempo de retorno médio
   ¤ Tempo de resposta médio
   ¤ Tempo de espera médio

   ### Descrição da entrada:
   A entrada é composta por uma série de pares de números inteiros separados por um espaço embranco indicando o tempo de chegada e a
   duração de cada processo. A entrada termina com o fim do arquivo.

   ### Descrição da saída:
   A saída é composta por linhas contendo a sigla de cada um dos três algoritmos e os valores das três métricas solicitadas 
   
   ----------------------------------------------------------------------------------------------------------------------------
   
-> Programa 02: Algoritmos de substituição de página

   Neste projeto você deve escrever um programa para simular o funcionamento dos principais algoritmos de substituição de páginas          estudados na disciplina. Os algoritmos de substituição de páginas a serem implementados são os seguintes:
   ¤ FIFO (First In, First Out)
   ¤ OTM: Algoritmo Ótimo
   ¤ LRU: (Least Recently Used ou Menos Recentemente Utilizado)

   O seu programa deverá ler de um arquivo um conjunto de número inteiros onde o primeiro número representa a quantidade de quadros de      memória disponíveis na RAM e os demais representam a sequência de referências às páginas, sempre um número por linha. Seu programa      deverá imprimir na saída o número de faltas de páginas obtido com a utilização de cada um dos algoritmos.

   ### Descrição da entrada:
   A entrada é composta por uma série números inteiros, um por linha, indicando, primeiro a quantidade de quadros disponíveis na memória    RAM e, em seguida, a sequência de referências à memória.

   ### Descrição da saída:
   A saída é composta por linhas contendo a sigla de cada um dos três algoritmos e a quantidade de faltas de página obtidas com a          utilização de cada um deles

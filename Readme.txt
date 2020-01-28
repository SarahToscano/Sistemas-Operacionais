-> O arquivo com os casos de testes tem que ser nomeado como 'test.txt'
-> O programa foi feito em python e utiliza recursos da biblioteca itemgetter do pacote operator
   para reordenar os dados do arquivo de entrada  (-- from operator import itemgetter --)

Lógica utilizada para o tempo de retorno - FCFS:
|20|
|20|+|10|
|20|+|10|+|6|
|20|+|10|+|6|+|8|
 n*20+ (n-1)*10 +...-Tempo de entrada -> n=numero de processos

 Tem um bug no RR qnd eh 0
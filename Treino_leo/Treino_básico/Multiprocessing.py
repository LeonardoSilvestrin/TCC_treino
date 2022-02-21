#multiprocessing ideal para CPU bound (alto uso de CPU)
#multithread ideal para IO bound (espera input, etc)

#numero de processos limitado ao número de cores do cpu: para ver o número de cores, usar cpu_count()

import time
from multiprocessing import Process, cpu_count

def counter(num):
    count = 0
    while count < num:
        count +=1

def main():
    #versão sem processamento paralelo:
    #a = Process(target = counter,args = (100000000,))
    #a.start()
    #a.join()
    #tempo para finalizar: 6,7464111
    #==========================================================
    #versão com processamento paralelo: 
    a = Process(target = counter,args = (50000000,))
    b = Process(target = counter,args = (50000000,))
    a.start()
    b.start()
    a.join()
    b.join()
    #tempo para finalizar: 3,4744683
    #===========================================================
    print("Finished in:", time.perf_counter(), "seconds")
    print(cpu_count())
if __name__ == '__main__':
    main()
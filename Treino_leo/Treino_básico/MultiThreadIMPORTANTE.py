import time
import threading


def f1():
    time.sleep(1)
    print("primeira função")
    
def f2():
    time.sleep(2)
    print("segunda função")
    
def f3():
    time.sleep(3)
    print("terceira função")
    

#==========monothread===========
#f1()
#f2()
#f3()
#==========multithread==========
x = threading.Thread(target = f1,args = ())
y = threading.Thread(target = f2,args = ())
z = threading.Thread(target = f3,args = ())

x.start()
y.start()
z.start()

#main espera x y e z completarem antes de passar para as próximas instruções:
print(threading.active_count())

x.join() 
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())

#somente uma das threads é processada por vez, o interpretador não roda elas em paralelo de verdade.
#multithreading é melhor quando temos funções I/O bound, ou seja, que esperam algum evento externo ocorrer para continuar, como um input.
#multiprocessing é melhor quando temos um programa que seja CPU bound, ou seja, que aguarde eventos internos para continuar

#CPU bound = multiprocessing
#IO bound = multithreading
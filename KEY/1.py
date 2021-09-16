from os import cpu_count
from datetime import datetime
from math import sqrt
from threading import Thread

def calc():
    for i in range(0, 200000000):
        sqrt(i)

threads = []; start = datetime.now()

for i in range(cpu_count()):
    print('Registering thread {}'.format(i))
    threads.append(
        Thread(target=calc)
    )
print('Step-1:', (datetime.now()-start).total_seconds(), 'seconds'); point = datetime.now()

for thread in threads:
    thread.start()

print('Step-2:', (datetime.now()-point).total_seconds(), 'seconds'); point = datetime.now()

for thread in threads:
    thread.join()

print('Step-3:', (datetime.now()-point).total_seconds(), 'seconds')

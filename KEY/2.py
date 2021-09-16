from os import cpu_count
from datetime import datetime
from math import sqrt
from multiprocessing import Process

def calc():
    for i in range(0, 200000000):
        sqrt(i)

processes = []; start = datetime.now()

for i in range(cpu_count()):
    print('Registering process {}'.format(i))
    processes.append(
        Process(target=calc)
    )
print('Step-1:', (datetime.now()-start).total_seconds(), 'seconds'); point = datetime.now()

for process in processes:
    process.start()

print('Step-2:', (datetime.now()-point).total_seconds(), 'seconds'); point = datetime.now()

for process in processes:
    process.join()

print('Step-3:', (datetime.now()-point).total_seconds(), 'seconds')

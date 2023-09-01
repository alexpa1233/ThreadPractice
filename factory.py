import random
from threading import Thread, Semaphore
from time import sleep
from random import uniform


NUMBER_OF_WORKERS = 10
NUMBER_OF_TRUCKS = 40
WEEK_DAYS = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']


pallets = Semaphore(0)      # Palés de chocolate listos para llevar


class Worker(Thread):
    '''Simula el trabajo de los empleados de la fábrica produciendo los palés
    de chocolate, así como sus periodos de descanso'''

    WORKLEG_TIME = 8
    REST_TIME = 12
    PALLETS_PER_TIMEUNIT = 5

    def __init__(self, number):
        Thread.__init__(self)
        self.name = str(number)

    def goToFactory(self):
        print('[TRABAJADOR ' + self.name + '] Acudiendo al trabajo...')
        sleep(uniform(1, 3))

    def work(self):
        
        tiempoSobrante = 0
        hora_de_descanso = random.randint(1,self.WORKLEG_TIME)
        print('[TRABAJADOR ' + self.name + '] Produciendo chocolate...')
        
        for i in range(0,self.WORKLEG_TIME + 1):
            if hora_de_descanso != i:
                for i in range(0,self.PALLETS_PER_TIMEUNIT):
                    pallets.release()
                
            sleep(1)    
        
        

    def rest(self):
        print('[TRABAJADOR ' + self.name + '] Jornada acabada, a casa a descansar')
        sleep(self.REST_TIME)
        

    def run(self):
        for i in WEEK_DAYS:
            self.work()
            self.rest()
        
        

class Truck(Thread):
    '''Simula el comportamiento de los camiones que acuden a la fábrica
    para llevarse los palés de chocolate'''

    MAX_CAPACITY = 25
    

    def __init__(self, number):
        Thread.__init__(self)
        self.name = str(number)
        self.contador = int(random.uniform(1,2))

    def travel(self):
        print('[CAMIÓN ' + self.name + '] Acudiendo a la fábrica...')
        sleep(uniform(1,12))
        

    def load(self):
        print('[CAMIÓN ' + self.name + '] Cargando palés...')
        for i in range(self.MAX_CAPACITY):
            pallets.acquire()
        
        
       

    def run(self):
        sleep(uniform(12,60))                
        self.travel()
        self.load()
        sleep(48)
        self.travel()
        self.load()

                
            

            
       
        

if __name__ == '__main__':
    print('Fábrica de chocolates')
    for i in range(NUMBER_OF_TRUCKS):
        myTruck = Truck(str(i))
        myTruck.start()
        
 
    for i in range(NUMBER_OF_WORKERS):
        myWorker = Worker(str(i))
        myWorker.start()



        


        
 

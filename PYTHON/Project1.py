class Robot:
    def __init__(self, name, numberofmodels, energy):
        self.name=name
        self.numberofmodels=numberofmodels
        self.models=[]
        self.energy=energy
    def ShowInfo(self):
        print(f'Robot: Название модели {self.name}, Количество модулей {self.numberofmodels}, Значение питания {self.energy}')
    def Walk(self, distance):
        self.energy=self.energy-distance*10
        print(f'Robot: Оставшаяся энергия {self.energy}')
    def Add_Model(self, models):
        if len(self.models)<self.numberofmodels:
            self.models.append(models)
            print('Модуль успешно добавлен.')
        else:
            print('Недостаточно места.')
class Models:
    def __init__(self, name, description):
        self.name=name
        self.description=description
R1=Robot('Eva', 1, 3500)
R1.ShowInfo()
R1.Walk(50)
R2=Robot('WALL-E', 2, 2400)
R2.ShowInfo()
R2.Walk(20)
R3=Robot('A.I.sha 2026', 3, 4700)
R3.ShowInfo()
R3.Walk(100)
R4=Robot('Mini', 1, 2100)
R4.ShowInfo()
R4.Walk(30)
M1=Models('Speed Accelerator', 'Boosts more speed, but uses much battery.')
M2=Models('Battery Saver', 'Saves the battery life.')
M3=Models('Lively communication', 'Makes the speech and language more realistic.')
M4=Models('Video Generator', 'Create videos look like movies.')
M5=Models('Friendly Flash', 'Your forever friend.')
M6=Models('Police Guard', 'Watches and protects you.')
R2.Add_Model(M1)
R2.Add_Model(M2)
R2.Add_Model(M3)
R1.Add_Model(M6)
R4.Add_Model(M5)
R4.Add_Model(M1)
R3.Add_Model(M6)
R3.Add_Model(M4)
R3.Add_Model(M3)
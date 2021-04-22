class Car():
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color =color
        self.name = name
        self.is_police = is_police

    def go(self):
        return print('Машина поехала')
    def stop(self):
        return print('Машина остановилась')
    def turn(self, direction):
        if direction == '<':
            return print('Машина повернула налево')
        elif direction == '>':
            return print('Машина повернула направо')
        else:
            return print('Машине не повернула')
    def show_speed(self):
        return print(f'Скорость автомобиля {self.name} = {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return print(f'Скорость автомобиля {self.name} = {self.speed}. ПРЕВЫШЕНИЕ.')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return print(f'Скорость автомобиля {self.name} = {self.speed}. ПРЕВЫШЕНИЕ.')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        return print(f'Скорость полицейского автомобиля {self.name} = {self.speed}. Скорость не ограничена')

class SportCar(Car):
    def show_speed(self):
        if self.speed < 100:
            return print(f'Слишком медленно')

tc = TownCar(61, 'Red', 'Town_R1', False)
tc.go()
tc.show_speed()
wc = WorkCar(42, 'Green', 'Worker_3', False)
wc.stop()
wc.show_speed()
pc = PoliceCar(88, 'White', 'Cop_6', True)
pc.turn('>')
pc.show_speed()
sc = SportCar(99, 'Blue', 'Ferra', False)
sc.show_speed()
ac = Car(44, 'Brown', 'Default', False)
ac.show_speed()
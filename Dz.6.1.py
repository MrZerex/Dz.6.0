from time import sleep
class Svetofor():
    __one_color = None
    def colors(self):
        ch = 0
        while True:
            print('Красный свет')
            sleep(7)
            print('Желтый свет')
            sleep(2)
            print('Зеленый свет')
            sleep(1)
            ch += 1
            if ch == 5:
                break
svet = Svetofor()
svet.colors()

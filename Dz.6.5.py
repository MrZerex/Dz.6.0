class Stationery():
    def __init__(self, tittle='Main'):
        self.tittle = tittle

    def draw(self):
        return print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        return print('Отрисовка ручкой')

class Pencil(Stationery):
    def draw(self):
        return print('Отрисовка карандашом')

class Handle(Stationery):
    def draw(self):
        return print('Отрисовка маркером')

st = Stationery()
st.draw()
pn = Pen()
pn.draw()
pcl = Pencil()
pcl.draw()
hdl = Handle()
hdl.draw()
class Road():
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def doroga(self):
        return f'Масса асфальта равна: {((self._lenght) * (self._width) * 25 * 5) / 1000} т.'

dor = Road(20, 5000)
print(dor.doroga())
# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, x_coord, y_coord):
        self._x = x_coord
        self._y = y_coord
        self._speed = 0.5
        self._direction = "UP"
        self._state = "crawl"

    def get_speed(self):
        if self._state == "crawl":
            self._speed = 0.5
        elif self._state == "fly":
            self._speed = 1.2
        else:
            raise ValueError('Рожденный ползать летать не должен!')

    def move(self, direction):
        speed = self.get_speed()
        if direction == "UP":
            self.field.set_unit(y=self._y + speed, x=self._x, unit=self)
        elif direction == "DOWN":
            self.field.set_unit(y=self._y - speed, x=self._x, unit=self)
        elif direction == "LEFT":
            self.field.set_unit(y=self._y, x=self._x - speed, unit=self)
        elif direction == "RIGTH":
            self.field.set_unit(y=self._y, x=self._x + speed, unit=self)

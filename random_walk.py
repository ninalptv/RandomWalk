from random import choice

class RandomWalk():
    """Класс для генерирования случайных блужданий."""
    def __init__(self, num_points=5000):
        """Инициализирует атрибуты блуждания."""
        self.num_points = num_points  # количество точек
        self.x_values = [0]  # список для хранения значений х
        self.y_values = [0]  # список для хранения у

    def get_step(self):
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        step = direction * distance
        return step


    def fill_walk(self):
        """Вычисляет все точки блуждания."""
        while len(self.x_values) < self.num_points:  # выполняется цикл до количества точек
            x_step = self.get_step()
            y_step = self.get_step()
            if x_step == 0 and y_step == 0:  # если оба шага =0 то блуждание останавливается, но цикл пролжается
                continue
            x = self.x_values[-1] + x_step  # получаем следующее значение х, прибавляем шаг к последнему значению кот хранится в self.x_values
            y = self.y_values[-1] + y_step
            self.x_values.append(x)  # значение присоединяется к списку
            self.y_values.append(y)


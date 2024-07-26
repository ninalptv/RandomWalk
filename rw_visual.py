import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(50000)  # случайное блуждание из 50000 точек
    rw.fill_walk()
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9))  # figsize=(15,9)- разрешение диаграммы в дюймах
    point_numbers = range(rw.num_points)  # генерируется список чисел, размер которого равен колву точек, он нужен для назначения цветакаждой точке блуждания
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Greens, edgecolor='none', s=1)  # edgecolor='none' - удаляет черный контур вокруг точки
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)  # выводится начальная и ниже конечная точка
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    ax.get_xaxis().set_visible(False)  # убираются оси с диаграммы
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break



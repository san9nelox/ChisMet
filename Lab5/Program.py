import matplotlib.pyplot as plt
from tabulate import tabulate


def main():
    headers = ['Аналитическая функция', 'Эйлера явный', 'Рунге-Кутта четвертого порядка',
               'Адамса трехшаговый явный'
               ]
    data_N = [10, 20, 30]
    for N in data_N:
        step = 1 / N
        data = []
        prev_y_Eul = 2
        prev_y_Run = 2
        prev_prev_y_Adam = 2
        prev_y_Adam = 1000
        y_Adam = 1000
        array_x = []
        for i in range(N):
            data_row = []
            x = 1 - step * i

            array_x.append(x)
            data_row.append(analytical(x))

            prev_y_Eul = Eulers_explicit(x, prev_y_Eul, step)
            data_row.append(prev_y_Eul)

            prev_y_Run = Runge_Kutta(x, prev_y_Run, step)
            data_row.append(prev_y_Run)

            if prev_y_Adam == 1000:
                prev_y_Adam = prev_y_Run
                data_row.append(prev_y_Run)

            elif y_Adam == 1000:
                y_Adam = prev_y_Run
                data_row.append(prev_y_Run)

            else:
                temp = Adams(x, y_Adam, prev_y_Adam, prev_prev_y_Adam, step)
                prev_prev_y_Adam = prev_y_Adam
                prev_y_Adam = y_Adam
                y_Adam = temp
                data_row.append(y_Adam)

            data.append(data_row)
        print(f'Результаты методов для {N} точек')
        print(tabulate(data, headers=headers, tablefmt='grid'))
        i = 0
        for head in headers:
            graph(array_x, [row[i] for row in data], f'{head} для {N}')
            i += 1
        all_graph(array_x, data, f'Результаты методов для {N} точек')


def analytical(x):
    return 2 * x ** 3


def f(x, y):
    return 3 * y / x


def Eulers_explicit(x, y, h):
    return y - f(x, y) * h


def Runge_Kutta(x, y, h):
    K1 = h * f(x, y)
    K2 = h * f(x + h / 2, y + K1 / 2)
    K3 = h * f(x + h / 2, y + K2 / 2)
    K4 = h * f(x + h, y + K3)
    return y - 1 / 6 * (K1 + 2 * K2 + 2 * K3 + K4)


def Adams(x, y, y_prev, y_prev_prev, h):
    return y - h / 12 * (23 * f(x, y) - 16 * f(x, y_prev) + 5 * f(x, y_prev_prev))


def graph(x: list, y: list, name: str):
    plt.plot(x, y, color='blue')
    plt.title(name)
    plt.show()


def all_graph(x: list, data: list, name: str):
    colors = ['blue', 'red', 'pink', 'orange']
    i = 0
    for color in colors:
        plt.plot(x, [row[i] for row in data], color=color)
        i += 1
    plt.title(name)
    plt.show()


if __name__ == '__main__':
    main()

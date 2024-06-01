import math

import matplotlib.pyplot as plt


def main():
    data_N = [9, 19]
    for n in data_N:
        data_analytical = analytical(n)
        data_shoot = shooting_method(n)
        data_run = run_through_method(n)
        print_graph(data_analytical, data_shoot, data_run, n)


def analytical(n):
    step = 1 / n
    data = []
    for i in range(n + 1):
        data.append(analytical_func(i * step))
    return data


def analytical_func(x):
    return math.pow(math.e, -x) + math.pow(math.e, x) + 2.2 * x * x - 2.2 * x - 2


def shooting_method(n):
    epsilon = math.pow(10, -5)
    step = 1 / n
    mu = 1
    mu_prev = 0
    temp = find_y(n, step, mu_prev)
    fi_mu_prev = f_mu(temp[len(temp) - 1])
    while math.fabs(mu - mu_prev) > epsilon:
        temp = find_y(n, step, mu)
        fi_mu = f_mu(temp[len(temp) - 1])
        temp = mu
        mu = mu - fi_mu / (fi_mu - fi_mu_prev) * (mu - mu_prev)
        mu_prev = temp
        fi_mu_prev = fi_mu
    return find_y(n, step, mu)


def find_y(n, h, mu) -> list:
    y = mu
    z = mu - 2.2
    data = [y]
    for i in range(n):
        y, z = Cauchy_method(h * i, y, z, h)
        data.append(y)
    return data


def f_mu(y):
    return y - math.e - 1 / math.e + 2


def Cauchy_method(x, y, z, h):
    y_half = y + h / 2 * z
    z_half = z + h / 2 * (y + 2.2 * x * (1 - x) + 6.4)
    y_k = y + h * z_half
    z_k = z + h * (y_half + 2.2 * (x + h / 2) * (1 - x - h / 2) + 6.4)
    return y_k, z_k


def run_through_method(n):
    h = 1 / n
    data_lambda = []
    data_mu = []
    lamb = 2 / (2 + 2 * h + h * h)
    mu = (-4.4 * h + h * h * 6.4) / (-2 - 2 * h - h * h)
    data_lambda.append(lamb)
    data_mu.append(mu)
    for i in range(1, n + 1):
        lamb, mu = find_lambda_and_mu(lamb, mu, i, h)
        data_lambda.append(lamb)
        data_mu.append(mu)
    length = len(data_lambda)
    data_lambda[length - 1] = 0
    data_mu[length - 1] = math.e + 1 / math.e - 2
    data_y = []
    y = math.e + 1 / math.e - 2
    for k in range(length, 0, -1):
        y = data_lambda[k - 1] * y + data_mu[k - 1]
        data_y.append(y)
    return list(reversed(data_y))


def find_lambda_and_mu(lamb, mu, i, h):
    temp = lamb
    lamb = 1 / (h * h + 2 - temp)
    mu = (mu - h * h * (2.2 * h * i * (1 - h * i) + 6.4)) / (h * h + 2 - temp)
    return lamb, mu


def print_graph(data_analyt, data_shoot, data_run, n):
    step = 1 / n
    x = []
    for i in range(n + 1):
        x.append(i * step)
    plt.figure()

    plt.plot(x, data_analyt, label='Аналитическое решение', color='blue')

    plt.plot(x, data_shoot, label='Метод стрельбы', color='red')

    plt.plot(x, data_run, label='Метод прогонки', color='green')
    plt.title(f'Графики для разбиения на {n + 1} точек')
    plt.legend()
    plt.grid(True)
    plt.xlim(0, 1)
    plt.show()
    count_shoot = 0
    count_run = 0
    for i in range(len(data_analyt)):
        if math.fabs(data_analyt[i] - data_shoot[i]) < math.fabs(data_analyt[i] - data_run[i]):
            count_shoot += 1
        else:
            count_run += 1
    print(count_shoot, count_run)


if __name__ == '__main__':
    main()

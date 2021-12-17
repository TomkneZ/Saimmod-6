from graphviz import Source
from simulations import simulate_work


DEVICES_COUNT = 2
ITERATIONS_COUNT = 1000000
ERLANG_ORDER = 2


def show_graph():
    path = 'graph.gv'
    graph = Source.from_file(path)
    graph.view()


def calculate_repair_intensity(mean_time):
    hours_in_day = 24
    if mean_time != 0:
        return ERLANG_ORDER / mean_time * hours_in_day
    else:
        return float('inf')


if __name__ == '__main__':
    #show_graph()
    λ = float(input("Интенсивность λ потока неисправностей (неисправн./сутки): "))
    m = float(input("Среднее значение времени ремонта (в часах): "))
    μ = calculate_repair_intensity(m)
    results = simulate_work(ITERATIONS_COUNT, ERLANG_ORDER, λ, μ, DEVICES_COUNT)
    print('P0 (оба узла работают): %f' % results.p0)
    print('P01 (один узел работает, второй ремонтируется): %f' % results.p01)
    print('P11 (оба узла ремонтируются): %f' % results.p11)


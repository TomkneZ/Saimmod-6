from device import Device
from math import isfinite
from collections import namedtuple

Result = namedtuple('Result', ['p0', 'p11', 'p01'])


def simulate_work(iterations_count, erlang_order, break_intensity, repair_intensity, devices_count):
    device_constructor = lambda: Device(
        erlang_order,
        break_intensity,
        repair_intensity
    )
    devices = [device_constructor() for _ in range(devices_count)]

    all_time = 0
    all_up = 0
    all_down = 0
    one_up = 0

    for _ in range(iterations_count):
        time = min((device._need_time for device in devices if isfinite(device._need_time)), default=1)

        if all((not device.broken for device in devices)):
            all_up += time
        elif all((device.broken for device in devices)):
            all_down += time
        else:
            one_up += time

        for device in devices:
            device.change_state(time)
        all_time += time

    return Result(
        p0=all_up / all_time,
        p11=all_down / all_time,
        p01=one_up / all_time
    )

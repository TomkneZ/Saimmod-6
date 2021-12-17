from math import log
from random import random


class Device:
    def __init__(self, erlang_shape, break_intensity, repair_intensity):
        self._break_intensity = break_intensity
        self._repair_intensity = repair_intensity
        self._need_time = self.get_working_time()
        self._erlang_shape = erlang_shape
        self.broken = False

    def change_state(self, time):
        if self.broken:
            self.try_repair(time)
        else:
            self.try_break(time)

    def try_repair(self, time):
        if time >= self._need_time:
            self._need_time = self.get_working_time()
            self.broken = False
        else:
            self._need_time -= time

    def try_break(self, time):
        if time >= self._need_time:
            self._need_time = self.get_repair_time()
            self.broken = True
        else:
            self._need_time -= time

    def get_working_time(self):
        return self.get_random_working_time(self._break_intensity)

    def get_repair_time(self):
        return self.get_random_repair_time(self._repair_intensity, self._erlang_shape)

    def get_random_working_time(self, intensity):
        if intensity != 0:
            return -1 / intensity * log(random())
        else:
            return float('inf')

    def get_random_repair_time(self, intensity, erlang_order):
        if intensity != 0:
            return -1 / intensity * sum((log(random()) for _ in range(erlang_order)))
        else:
            return float('inf')

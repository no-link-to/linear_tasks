import math

import matplotlib.pyplot as plt


class LinearAlgebra:
    _x_coords = []
    _y_coords = []
    _figure = None
    _axis = None
    _amount = 0
    _limit_axis = 0
    _is_minus_axis = False

    def __init__(self, x_coords, y_coords, amount_dots, default_limit_axis):
        self._x_coords = x_coords
        self._y_coords = y_coords
        self._amount = amount_dots
        self._limit_axis = default_limit_axis

        self._init_plot()

    def _init_plot(self):
        self._figure, self._axis = plt.subplots()

        self._axis.set_xlabel('x')
        self._axis.set_ylabel('y')

    def _handle_limits(self, next_limit_axis=None, is_minus_axis=False):
        if next_limit_axis is not None:
            self._limit_axis = next_limit_axis
        if self._is_minus_axis is not is_minus_axis:
            self._is_minus_axis = is_minus_axis
        self._axis.set_xlim(min(self._x_coords) - self._limit_axis if self._is_minus_axis else 0,
                            max(self._x_coords) + self._limit_axis)
        self._axis.set_ylim(min(self._y_coords) - self._limit_axis if self._is_minus_axis else 0,
                            max(self._y_coords) + self._limit_axis)

    def _matrix_and_coords_multiplication(self, matrix, coords):
        return [matrix[0] * coords[0] + matrix[1] * coords[1], matrix[2] * coords[0] + matrix[3] * coords[1]]

    def _linear_worker(self, matrix, x_coords, y_coords):
        next_x_coords = []
        next_y_coords = []
        for i in range(self._amount):
            x = x_coords[i]
            y = y_coords[i]
            next_x, next_y = self._matrix_and_coords_multiplication(matrix, [x, y])
            next_x_coords.append(next_x)
            next_y_coords.append(next_y)
        return next_x_coords, next_y_coords

    def draw_figure(self):
        self._axis.plot(self._x_coords + [self._x_coords[0]],
                        self._y_coords + [self._y_coords[0]], 'b-')

    def draw_vector(self, *args):
        v1, v2, length_v1, length_v2 = args
        x, y = v1
        self._axis.quiver(x, y, length_v1 * x, length_v1 * y, angles='xy', scale_units='xy', scale=1, color='green')
        if v2:
            x, y = v2
            self._axis.quiver(x, y, length_v2 * x, length_v2 * y, angles='xy', scale_units='xy', scale=1, color='yellow')

    def draw_task_figure(self, matrix, task_axis_limit=None, is_minus_axis=False):
        self._handle_limits(task_axis_limit, is_minus_axis)

        next_x_coords, next_y_coords = self._linear_worker(matrix=matrix,
                                                           x_coords=self._x_coords,
                                                           y_coords=self._y_coords)

        self._axis.plot(next_x_coords + [next_x_coords[0]],
                        next_y_coords + [next_y_coords[0]], 'r-')

    def run(self):
        plt.show()


if __name__ == '__main__':

    linal = LinearAlgebra(x_coords=[4, 6, 8, 12], y_coords=[10, 8, 10, 12], amount_dots=4, default_limit_axis=30)
    linal.draw_figure()

    # Пункт 1
    # linal.draw_task_figure([-0.8, 0.6, 0.6, 0.8], task_axis_limit=10, is_minus_axis=True)
    # linal.draw_vector([1/3, 1], [-3, 1], 5, 2)

    # Пункт 2
    # linal.draw_task_figure([1, 0, 4, 0], task_axis_limit=40)

    # Пункт 3
    # linal.draw_task_figure([0.643, 0.766, -0.766, 0.643], task_axis_limit=15, is_minus_axis=True)

    # Пункт 4
    # linal.draw_task_figure([-1, 0, 0, -1], is_minus_axis=True)

    # Пункт 5
    # linal.draw_task_figure([(-4 + 3 * math.sqrt(3)) / 10, (3 + 4 * math.sqrt(3)) / 10,
                            # (3 + 4 * math.sqrt(3)) / 10, (4 - 3 * math.sqrt(3)) / 10], task_axis_limit=10)

    # Пункт 6
    # linal.draw_task_figure([1, 1, 3, 4], task_axis_limit=80)

    # Пункт 7
    # linal.draw_task_figure([4, -1, -3, 1], is_minus_axis=True)

    # Пункт 8
    # linal.draw_task_figure([1, 0, 7, -1], task_axis_limit=70)

    # Пункт 9
    # linal.draw_task_figure([math.sqrt(5), 0, 0, math.sqrt(5)])

    # Пункт 10
    # linal.draw_task_figure([math.sqrt(math.pi) / math.pi, 0, 0, (6 * math.sqrt(math.pi)) / math.pi])

    # Пункт 11
    # linal.draw_task_figure([8, 5, 5, 2], task_axis_limit=130) #130
    # linal.draw_vector([(3 - math.sqrt(34)) / 5, 1], [(3 + math.sqrt(34)) / 5, 1], 5, 5)

    # Пункт 12
    # linal.draw_task_figure([8, 0, 5, 8], task_axis_limit=160)
    # linal.draw_vector([0, 1], [], 20, 5)

    # Пункт 13
    # linal.draw_task_figure([8, -3, 2, 8], task_axis_limit=110)

    # Пункт 14
    # linal.draw_task_figure([1, 0, 0, 1]) # Сам в себя отображает
    # linal.draw_vector([0, 1], [1, 0], 5, 5)

    # Пункт 15
    # A
    # linal.draw_task_figure([3, 2, 5, 2], task_axis_limit=80)
    # linal.draw_vector([(1 - math.sqrt(41)) / 10, 1], [(1 + math.sqrt(41)) / 10, 1], 6, 6)

    # B
    # linal.draw_task_figure([4, 7, -1, 6], task_axis_limit=120)
    # Тут комплексные собственные вектора

    # A*B
    # linal.draw_task_figure([10, 33, 18, 47], task_axis_limit=500) # A*B # Делать отдельные скрины начинается 320 500
    # linal.draw_vector([(-37 - math.sqrt(3745)) / 36, 1], [(-37 + math.sqrt(3745)) / 36, 1], 5, 5)

    # B*A
    # linal.draw_task_figure([47, 22, 27, 10], task_axis_limit=500) # B*A # Делать отдельные скрины начинается 410 210
    # linal.draw_vector([(37 - math.sqrt(3745)) / 54, 1], [(37 + math.sqrt(3745)) / 54, 1], 5, 5)

    # Пункт 16
    # A
    # linal.draw_task_figure([1, 2, 6, 5], task_axis_limit=500) # Делать отдельные скрины
    # linal.draw_vector([-1, 1], [1 / 3, 1], 5, 5)

    # B
    # linal.draw_task_figure([4, 3, 9, 10], task_axis_limit=500) # Делать отдельные скрины
    # linal.draw_vector([-1, 1], [1 / 3, 1], 5, 5)

    # A*B = B*A
    # linal.draw_task_figure([22, 23, 69, 68], task_axis_limit=2000) # A*B=B*A # Делать отдельные скрины начинается 318 956
    # linal.draw_vector([-1, 1], [1 / 3, 1], 5, 5)

    linal.run()

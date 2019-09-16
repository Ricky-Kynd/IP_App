class Histogram:
    def __init__(self, data, x_width=5, y_width=10):
        self.data = data
        self.x_width = x_width
        self.y_width = y_width

    def draw_horizontal_histogram(self, x_index=0, y_index=1, unit=10):
        for index in range(len(self.data)):
            self.data[index][y_index] = int(self.data[index][y_index])
            print('{:<{}}|{:<{}}'.format(self.data[index][x_index], self.x_width, (self.data[index][y_index] // unit) * '*', self.y_width))

    def draw_vertical_histogram(self, x_index=0, y_index=1, unit=10):
        data_x = [x[x_index] for x in self.data] #x_index element in self.data
        data_y = [(y[y_index] // unit) for y in self.data] #y_index element in self.data
        max_len = max(data_y)

        #--- print star and spaces
        for row in range(max_len -1, -1, -1):
            for column in range(len(data_y)):
                if row < data_y[column]:
                    print('*', end=" " * (self.x_width - 1))
                else:
                    print(end=" " * (self.x_width))
            print('')
        #--- print border bottom
        print('{}'.format('-' * self.x_width * len(data_y)))
        #--- Print names
        for i in data_x:
            print('{:<{}}'.format(i, self.x_width), end='')

    def __str__(self):
        return 'x_width={} y_width={}, data={}'.format(self.x_width, self.y_width, self.data)
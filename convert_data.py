import numpy


class ConvertData:
    def __init__(self, mouse_pos, thick_x, thick_y):
        self.mouse_pos = mouse_pos
        self.width = 28
        self.height = 28
        self.grid_width = 500
        self.grid_height = 500
        self.thick_x = thick_x
        self.thick_y = thick_y

    def convert_data(self):
        """
        Scale the image at 28 by 28px
        :return: numpy array
        """
        scale_grid = []
        scale_grid_row = []
        differ_x = self.width / self.grid_width
        differ_y = self.height / self.grid_height
        for y in range(self.height):
            for x in range(self.width):
                scale_grid_row.append(0)
            scale_grid.append(numpy.array(scale_grid_row))
            scale_grid_row.clear()
        scale_grid = numpy.array(scale_grid)
        for mouse_pos in self.mouse_pos:
            x_pos, y_pos = mouse_pos
            scale_x, scale_y = (round(x_pos*differ_x), round(y_pos*differ_y))
            scale_grid[scale_y][scale_x] = 255
        return scale_grid

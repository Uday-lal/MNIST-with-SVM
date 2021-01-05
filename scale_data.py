import numpy


class ScaleData:
    def __init__(self, mouse_pos, thick_x, thick_y):
        self.mouse_pos = mouse_pos
        self.width = 28
        self.height = 28
        self.grid_width = 500
        self.grid_height = 500
        self.thick_x = thick_x
        self.thick_y = thick_y

    def scale_img_data(self):
        """
        Scale the image at 28 by 28px
        :return: numpy array
        """
        scale_grid = []
        scale_grid_row = []
        differ_x = self.width / self.grid_width
        differ_y = self.height / self.grid_height
        scale_width, scale_height = round(self.thick_x*differ_x), round(self.thick_y*differ_y)

        for y in range(self.height):
            for x in range(self.width):
                scale_grid_row.append(0)
            scale_grid.append(numpy.array(scale_grid_row))
            scale_grid_row.clear()
        scale_grid = numpy.array(scale_grid)

        for mouse_pos in self.mouse_pos:
            x_pos, y_pos = mouse_pos
            scale_x, scale_y = round(x_pos * differ_x), round(y_pos * differ_y)
            scale_grid[scale_y][scale_x] = 255

            for h in range(scale_height):
                for w in range(scale_width):
                    scale_grid[scale_y + h][scale_x + w] = 255

        return scale_grid

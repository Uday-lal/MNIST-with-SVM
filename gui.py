import pygame
# from tkinter import messagebox
# import pickle
import sys
from convert_data import ConvertData
import numpy


def mouse_input():
    """
    Getting the mouse input
    :return: cursor position when when user click
    """
    is_clicked = pygame.mouse.get_pressed(num_buttons=5)
    mouse_pos = pygame.mouse.get_pos()
    if is_clicked[0]:
        return mouse_pos


class MnistGui:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("MNIST")
        self.width = 500
        self.height = 500
        self.bg_color = (255, 255, 255)
        self.pixel_color = (255, 255, 255)
        self.pixel_width = 10
        self.pixel_height = 10
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.cursor_pos = []
        self.thickness_x = 50
        self.thickness_y = 50

    def run(self):
        """
        Running the whole main loop
        :return: None
        """
        while True:
            self.mouse_pos = mouse_input()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    convert_data = numpy.array([ConvertData(self.cursor_pos, thick_x=self.thickness_x,
                                                            thick_y=self.thickness_y).convert_data()])
                    print(convert_data)
                    # n_sample, nx, ny = convert_data.shape
                    # convert_data = convert_data.reshape((n_sample, nx * ny))
                    # model_ = open("mnist.pickel", "rb")
                    # model = pickle.load(model_)
                    # messagebox.showinfo("showinfo", f"My prediction is {model.predict(convert_data)[0]}")
            if self.mouse_pos is not None:
                self.cursor_pos.append((self.mouse_pos[0], self.mouse_pos[1]))
            self.draw()
            self.screen.fill(self.bg_color)

    def draw(self):
        """
        Fill the pixel on the screen
        :return: None
        """
        try:
            color = (255, 0, 0)
            for cursor_pos in self.cursor_pos:
                pygame.draw.rect(self.screen, color,
                                 pygame.Rect(cursor_pos[0], cursor_pos[1], self.thickness_x, self.thickness_y))
            pygame.display.update()
        except Exception:
            pass


MnistGui().run()

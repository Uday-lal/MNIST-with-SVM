import pygame
import sys


def mouse_input():
    """
    Getting the mouse input
    :return: mouse position when when user click
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
        self.bg_color = (0, 0, 0)
        self.pixel_color = (255, 255, 255)
        self.pixel_width = 10
        self.pixel_height = 10
        self.thickness = 100
        self.screen = pygame.display.set_mode((self.width, self.height))

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
            self.screen.fill(self.bg_color)
            self.draw_pixel()
            pygame.display.flip()

    def draw_pixel(self):
        """
        Draw the pixel on the screen
        :return: list
        """
        x = 0
        y = 0
        for row in range(self.width):
            if y <= self.height:
                for column in range(self.height):
                    pygame.draw.rect(self.screen, self.pixel_color,
                                     pygame.Rect(x, y, self.pixel_width, self.pixel_height))
                    x += self.pixel_width
                y += self.pixel_height
                x = 0
            else:
                break

    def fill_pixel(self):
        """
        Fill the pixel on the screen
        :return: None
        """
        pass


if __name__ == "__main__":
    MnistGui().run()

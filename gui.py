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
        self.fps = 60
        self.bg_color = (0, 0, 0)
        self.pixel_color = (255, 255, 255)
        self.pixel_width = 10
        self.pixel_height = 10
        self.thickness = 10
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.cursor_pos = []

    def run(self):
        """
        Running the whole main loop
        :return: None
        """
        clock = pygame.time.Clock()
        while True:
            clock.tick(self.fps)
            self.mouse_pos = mouse_input()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
            if self.mouse_pos is not None:
                self.cursor_pos.append((self.mouse_pos[0], self.mouse_pos[1]))
            if self.cursor_pos:
                self.fill_pixel()
            self.screen.fill(self.bg_color)
            self.draw_pixel()
            pygame.display.flip()

    def draw_pixel(self):
        """
        Draw the pixel on the screen
        :return: None
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
        for cursor_pos in self.cursor_pos:
            pygame.draw.circle(self.screen, (255, 0, 0), cursor_pos, self.thickness)
            pygame.display.update()


if __name__ == "__main__":
    MnistGui().run()

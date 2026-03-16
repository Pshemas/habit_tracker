from date_utils import *
from colorsets import *
from LCD_0inch96 import *
from habit_data import TrackerData

class TrackerInterface:
    def __init__(
        self,
        screen: LCD_0inch96,
        rectangle_amount: int = 5,
        rectangle_size: int = 30,
        x_start: int = 5,
        y_start: int = 25,
        text_top: str = "",
        text_bottom: str = "",
    ):
        self.rectangle_amount = rectangle_amount
        self.rectangle_size = rectangle_size
        self.x_start = x_start
        self.y_start = y_start
        self.screen = screen
        self.text_top = text_top
        self.text_bottom = text_bottom
        self.selected = self.rectangle_amount - 1

    def draw_interface(self, data: TrackerData):
        self.screen.fill(WHITE)
        if data:
            self.text_top = data.pixels[self.selected].show_result()
        self.screen.text(self.text_top, 2, 10, BLACK)
        for idx, pixel in enumerate(data.pixels):
            self.screen.rect(
                self.x_start + (idx * self.rectangle_size) + 3,
                self.y_start + 3,
                self.rectangle_size - 6,
                self.rectangle_size - 6,
                pixel.get_color(),
                True,
            )

        self.screen.rect(
            self.x_start + (self.selected * self.rectangle_size),
            self.y_start,
            self.rectangle_size,
            self.rectangle_size,
            RED,
        )
        self.screen.text(self.text_bottom, 2, 60, BLACK)
        self.screen.display()

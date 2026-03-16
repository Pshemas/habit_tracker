from date_utils import create_full_date_str
from colorsets import *
from controls import get_pixela
import ntptime


class Pixel:
    COLOR_PALETTE = [lightgrey, scarlet1, scarlet2, scarlet3, scarlet4]

    def __init__(self, date_str: str, score: int = 0):
        self.date = date_str
        self.score = score

    def get_bare_date(self) -> str:
        return self.date.replace(".", "")

    def show_result(self) -> str:
        return f"{self.date} - {self.score}"

    def get_color(self):
        if self.score <= 0:
            return self.COLOR_PALETTE[0]
        elif self.score >= 4:
            return self.COLOR_PALETTE[-1]
        else:
            return self.COLOR_PALETTE[self.score]

    def update_pixel_score(self):
        self.score = get_pixela(self.get_bare_date())


class TrackerData:
    def __init__(self, size: int):
        self.size = size
        self.pixels = []
        self.timestamp = 0
        self.fill_intial_data()

    def update_timestamp(self):
        self.timestamp = ntptime.time()

    def fill_intial_data(self):
        self.pixels = []
        self.update_timestamp()
        for i in range(self.size):
            date_str = create_full_date_str(self.timestamp, i)
            self.pixels.insert(0, Pixel(date_str))

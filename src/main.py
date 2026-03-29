from machine import Pin
from time import sleep
from LCD_0inch96 import LCD_0inch96
from colorsets import WHITE, BLACK
from wifi_func import connect_wifi, NoWifiError
from ui import TrackerInterface
from habit_data import TrackerData
from controls import *

KEY_UP = Pin(2, Pin.IN, Pin.PULL_UP)
KEY_DOWN = Pin(18, Pin.IN, Pin.PULL_UP)
KEY_LEFT = Pin(16, Pin.IN, Pin.PULL_UP)
KEY_RIGHT = Pin(20, Pin.IN, Pin.PULL_UP)
KEY_CTRL = Pin(3, Pin.IN, Pin.PULL_UP)
KEY_A = Pin(15, Pin.IN, Pin.PULL_UP)
KEY_B = Pin(17, Pin.IN, Pin.PULL_UP)


if __name__ == "__main__":
    lcd = LCD_0inch96()
    lcd.fill(WHITE)
    lcd.text("Startuje :)", 30, 30, BLACK)
    lcd.display()

    try:
        wifi = connect_wifi()

        app_data = TrackerData(5)
        sleep(1)

        ui = TrackerInterface(lcd)
        ui.draw_interface(app_data)
        get_pixels_scores(app_data, ui)

        while True:
            if KEY_A.value() == 0:
                print("A pressed")
                update_pixels_scores(app_data, ui)
            if KEY_B.value() == 0:
                print("B pressed")
                ui.text_bottom = "Rejestruje +1"
                ui.draw_interface(app_data)
                app_data.update_timestamp()
                add_to_today_score(app_data.timestamp)
                update_pixels_scores(app_data, ui)
            if KEY_LEFT.value() == 0:
                print("LEFT pressed")
                move_selection_box(ui, app_data, -1)

            if KEY_RIGHT.value() == 0:
                print("RIGHT pressed")
                move_selection_box(ui, app_data, +1)

            if KEY_CTRL.value() == 0:
                print("To CTRL")

            sleep(0.2)

    except NoWifiError as error:
        lcd.fill(WHITE)
        lcd.text("Brak wifi", 30, 30, BLACK)
        lcd.display()
        print(error)
        # TODO: add reboot via one of the exposed buttons

    except:
        lcd.fill(WHITE)
        lcd.text("Przerwane!", 5, 30, BLACK)
        lcd.text("Sprobuj restartu.", 5, 40, BLACK)
        lcd.display()
        # TODO: add reboot via one of the exposed buttons

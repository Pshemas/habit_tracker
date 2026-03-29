from ui import *
from habit_data import *
import requests
from time import sleep
import ujson
from date_utils import create_full_date_str

pixela_meta = []
with open(".pixela", "r") as f:
    for line in f:
        pixela_meta.append(line.strip())

TOKEN = pixela_meta[0]
USERNAME = pixela_meta[1]
PIXELA_URL = pixela_meta[2]
CODE_GRAPH = pixela_meta[3]


class RequestRejected(Exception):
    pass


def move_selection_box(ui: TrackerInterface, app_data: TrackerData, step: int):
    ui.selected = (ui.selected + step) % ui.rectangle_amount
    ui.text_top = app_data.pixels[ui.selected]
    ui.draw_interface(app_data)


def get_pixela(datestr: str) -> int:
    print(datestr)
    url = f"https://pixe.la/v1/users/{USERNAME}/graphs/{CODE_GRAPH}/{datestr}"
    headers = {"X-USER-TOKEN": TOKEN}
    response = None

    for _ in range(7):
        try:
            response = requests.get(
                url,
                headers=headers,
                timeout=60,
            )
            json_response = response.json()
            if "isRejected" in json_response and json_response["isRejected"] == True:
                raise RequestRejected
            print(f"\n\n{json_response}\n\n")
            return int(json_response["quantity"])

        except RequestRejected:
            print("Request rejected. Retrying.")
        except KeyError:
            return 0

        finally:
            if response is not None:
                response.close()

    raise RequestRejected


def add_to_today_score(current_timestamp):
    today = create_full_date_str(current_timestamp).replace(".", "")
    score = get_pixela(today)
    score = str(int(score) + 1)
    data = {"date": "".join(today), "quantity": score}
    headers = {
        "X-USER-TOKEN": TOKEN,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    url = f"https://pixe.la/v1/users/{USERNAME}/graphs/{CODE_GRAPH}"
    print(f"\n SENDING RESPONSE for {today}\n")
    response = requests.post(url, headers=headers, data=ujson.dumps(data))
    response.close()

    # TODO: ensure it went through - retry if it didn't, like in get_pixela


def get_pixels_scores(app_data: TrackerData, ui: TrackerInterface):
    ui.text_bottom = "Aktualizuje"
    ui.draw_interface(app_data)
    for pixel in app_data.pixels:
        pixel.update_pixel_score()
        ui.draw_interface(app_data)
    ui.text_bottom = "Gotowe"
    ui.draw_interface(app_data)


def update_pixels_scores(app_data: TrackerData, ui: TrackerInterface):
    app_data.update_timestamp()
    if app_data.pixels[-1].date != create_full_date_str(app_data.timestamp):
        app_data.fill_intial_data()
    get_pixels_scores(app_data, ui)

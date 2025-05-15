import datetime
import requests
from casioplot import *

date = datetime.date.today()
url = f"https://www.nytimes.com/svc/wordle/v2/{date:%Y-%m-%d}.json"
response = requests.get(url).json()
wordle_answer = response['solution'].upper()

def rectangle(start_x, start_y, end_x, end_y, color):
    width = abs(end_x - start_x)
    height = abs(end_y - start_y)
    for x in range(width + 1):
        for y in range(height + 1):
            set_pixel(start_x + x, start_y + y, color)

white = (255, 255, 255)
black = (0, 0, 0)
grey = (10, 10, 10)

rectangle(0, 0, 17, 25, grey)
rectangle(19, 0, 19+17, 25, grey)
draw_string(0, 0, wordle_answer, white,  "large")

show_screen()

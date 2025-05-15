import casioplot

from casioplot import *

print(get_pixel(10, 10))
red = (255, 0, 0)
set_pixel(10, 10, red)
print(get_pixel(10, 10))
show_screen()  # Don't forget to show the screen to see the result.

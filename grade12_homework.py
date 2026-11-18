# Grade 12 Python Homework – mBot2

import cyberpi

cyberpi.display.clear()

cyberpi.display.show_label("Name: Ylli", 0, 16)
cyberpi.display.show_label("Surname: Berisha", 1, 16)
cyberpi.display.show_label("Favorite Color: Dark Green", 2, 16)

cyberpi.display.show_label("Favorite Subjects:", 3, 16)
cyberpi.display.show_label("1. Biology", 4, 16)
cyberpi.display.show_label("2. Chemistry", 5, 16)
cyberpi.display.show_label("3. Physical Education", 6, 16)

cyberpi.led.on(255, 0, 0)

from microbit import *
compass.calibrate()
while True:
    value=compass.heading()
    if value>=46 and value<=134:
        display.show('E')
    elif value>=135 and value<=224:
        display.show('S')
    elif value>=225 and value<=314:
        display.show('W')
    else:
        display.show('N')
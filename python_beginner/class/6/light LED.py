from microbit import *
boat=Image("09900:"
            "09900:"
            "99999:"
            "00900:"
            "09090")
boat2=Image("09900:"
            "09909:"
            "09990:"
            "90900:"
            "09090")
boat4=Image("09900:"
            "99900:"
            "09990:"
            "00909:"
            "09090")

boat3=[boat,boat2,boat,boat4]
while True:
    display.show(boat3,delay=300)
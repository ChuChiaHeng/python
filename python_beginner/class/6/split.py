from microbit import *
old_str="05050:05050:05050:99999:09990"
img_list=old_str.split(":")
img_list[0]="55555"
new_str=':'.join(img_list)
display.show(Image(new_str))
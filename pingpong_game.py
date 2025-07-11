from pygame import *

#IMAGES-----------
img_back = "meja.pingpong.jpg"

#data-----------
finish = False
run = True

#game window -------------
win_width = 700
win_height = 500
display.set_caption("pingpong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

#game loops --------------
while run:

    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background,(0,0))

        display.update()
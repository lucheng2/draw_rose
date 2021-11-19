from PIL import Image, ImageOps
import numpy as np
import turtle

gray_threshold = 100
image_path = '原图.jpg'
title = '给吴欢的玫瑰'
pen_size = 2
pen_color = "red"
width, height = 400, 800
width_weight, height_weight = 1.5, 2
start_x, start_y = 0, 0


def get_data():
    im = Image.open(image_path)
    im = ImageOps.grayscale(im)
    arr = np.array(im)
    w, h = arr.shape
    global width, height
    width, height = int(w*width_weight), int(h*height_weight)
    w, h = w//2, h//2
    data = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] < gray_threshold:
                data.append((h - j, w - i))
    return data


def init():
    turtle.title(title)
    turtle.setup(width, height, start_x, start_y)
    turtle.pensize(2)
    turtle.pencolor(pen_color)
    turtle.penup()


def draw():
    a = get_data()
    init()
    for m in a:
        turtle.goto(m[0], m[1])
        turtle.down()
        turtle.goto(m[0], m[1])
        turtle.up()

    turtle.mainloop()


draw()

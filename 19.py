import turtle
turtle.pensize(4)###画笔宽度
turtle.speed(5)###画笔速度
turtle.pencolor("yellow")###画笔颜色
turtle.fillcolor("red")##填充颜色
turtle.begin_fill()
for i in range(5):
    turtle.forward(200)
    turtle.right(144)

turtle.end_fill()###填充颜色
turtle.mainloop()
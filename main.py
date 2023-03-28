import turtle

crawler = turtle.Turtle()
crawler.speed(14)

crawler.pencolor('green')
crawler.fillcolor('yellow')

x = 0
for x in range(18):
    crawler.begin_fill()
    crawler.forward(200)
    crawler.left(100)
    x +=1
screen = crawler.getscreen()
screen.exitonclick()


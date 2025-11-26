import turtle
import random

# إعداد الشاشة
wn = turtle.Screen()
wn.bgcolor("black")  # خلفية سوداء لتظهر النجوم

# إعداد السلحفاة
t = turtle.Turtle()
t.speed(0)  # أسرع سرعة
t.hideturtle()

# دالة لرسم نجمة خماسية صغيرة في موقع محدد ولون محدد
def draw_star(x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

# رسم 50 نجمة عشوائية
for _ in range(50):
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    size = random.randint(10, 30)  # حجم النجمة عشوائي
    color = random.choice(["yellow", "white", "blue", "red", "green"])
    draw_star(x, y, size, color)

turtle.done()

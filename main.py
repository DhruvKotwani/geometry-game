from random import randint


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rect):
        if rect.lowleft.x < self.x < rect.upright.x and rect.lowleft.y < self.y < rect.upright.y:
            return True
        else:
            return False


class Rectangle:
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

    def area(self):
        temp = (self.upright.x - self.lowleft.x) * (self.upright.y - self.lowleft.y)
        return temp


rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)), Point(randint(10, 19), randint(10, 19)))
print(f"Rectangle Co-ordinates : ({rectangle.lowleft.x}, {rectangle.lowleft.y}) and ({rectangle.upright.x}, {rectangle.upright.y})")

user_point = Point(float(input("Guess X: ")), float(input("Guess Y: ")))

user_area = float(input("Guess the area of rectangle: "))

print(f"Your point was inside rectangle : {user_point.falls_in_rectangle(rectangle)}")
print(f"Your area was off by {(rectangle.area() - user_area)}")

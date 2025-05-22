class Rectangle:
  def __init__(self, x1, y1, x2, y2):
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2
  def show(self):
    print(f'좌측 상단 꼭짓점이 {(self.x1,self.y1)}이고 우측 하단 꼭짓점이 {(self.x2,self.y2)}인 사각형입니다.')

  def getWidth(self):
    return self.x2 - self.x1

  def getHeight(self):
    return self.y2 - self.y1

  def getArea(self):
    a = Rectangle.getWidth(self)
    b = Rectangle.getHeight(self)
    return a*b

  def getperimeter(self):
    return Rectangle.getWidth(self)*2 + Rectangle.getHeight(self)*2

r1 = Rectangle(5,5,20,10)
a = r1.getArea()
p = r1.getperimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')

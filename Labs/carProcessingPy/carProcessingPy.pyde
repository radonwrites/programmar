# Even though there are multiple objects, we still only need one class. 
# No matter how many cookies we make, only one cookie cutter is needed.
class Car(object):
# The Constructor is defined with arguments.
    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c - 100
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        
    def display(self):
        if ((keyPressed) and (key == ' ')):
            myCar1.surprise()
            myCar2.surprise()
        else:
            stroke(0)
            fill(self.c)
            rectMode(CENTER)
            rect(self.xpos, self.ypos, 20, 10);
    
    def drive(self):
        self.xpos = self.xpos + self.xspeed;
        if self.xpos > width:
            self.xpos = 0
    
    def surprise(self):
        stroke(5)
        fill(self.c)
        ellipseMode(CORNER)
        ellipse(self.xpos, self.ypos, 20, 10);
        
class Friend(object):
    def __init__(self, c, xpos, ypos):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        
    def summon(self):
        s = createShape()
        s.beginShape()
        s.stroke(1)
        s.fill(self.c)
        s.vertex(5, 5)
        s.vertex(0, 25)
        s.vertex(40, 0)
        s.endShape()
        shape(s, self.xpos, self.ypos)
        
class Stuff(object):
    def __init__(self, c, xpos, ypos):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        
    def make(self):
        r = random(100)
        xpos = mouseX
        ypos = mouseY
        stroke(1)
        fill(self.c)
        ellipse(xpos, ypos, r, r)
        
class what(object):
    def __init__(self, c):
        self.c = c
        
    def tri(self):
        stroke(0)
        fill(self.c)
        triangle(30, 70, 20, 32, 50, 40)
        
    def squ(self):
        stroke(0)
        fill(self.c)
        square(12, 12, 10)
        
    def cir(self):
        stroke(0)
        fill(self.c)
        circle(66, 73, 10)
    
myCar1 = Car(color(255, 0, 0), 0, 100, 2)
myCar2 = Car(color(0, 255, 255), 0, 10, 1)

arr = []
for i in range(5):
    arr.append(Friend(color(random(225), random(225), random(225)), random(200), random(200)))

Sam = Friend(color(100,150,200), 50, 150)

Blob = Stuff(color(150,75,200), 40, 50)

isit = what(color(random(225), random(225), random(225)))
    
def setup():
    size(200,200)
    Sam.summon()

def draw():
  background(255)
  
  for i in arr:
      i.summon()
  if (mousePressed == True):
      Blob.make()
  if ((keyPressed) and (key == 'a')):
      isit.tri()
  if ((keyPressed) and (key == 'b')):
      isit.squ()
  if ((keyPressed) and (key == 'c')):
      isit.cir()
  myCar1.drive()
  myCar1.display()
  myCar2.drive()
  myCar2.display()
  fill(0)
  text('Press a, b, or c', 100, 180)
  
  

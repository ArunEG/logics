import simplegui
import random

#global Variables
display_text = "My python"
position = [200,200]
height = 500
width = 500

def tick():
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    position[0] = x
    position[1] = y
    print "hellooo"
    
    

def draw(canvas):
    canvas.draw_text(display_text, position, 36, "Red")
    

def input_handler(inp):
    global display_text
    display_text = inp


# create frame 

myf = simplegui.create_frame("Myframe",500,500)
myf.set_canvas_background("gray")
myf.add_input('',input_handler,100)
timer = simplegui.create_timer(2000,tick)
myf.start()
timer.start()
myf.set_draw_handler(draw)

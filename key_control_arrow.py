import simplegui



#global variable section
current_key = ''
width = 600
height = 600
ball_pos = [width/2,height/2]

#genaral funtion defanition section



#Event handler functions
def keydown(key):
    speed =20
    global current_key
    if key == simplegui.KEY_MAP["left"]:
        ball_pos[0] -= speed
    elif key == simplegui.KEY_MAP["right"]:
        ball_pos[0] += speed
    elif key == simplegui.KEY_MAP["up"]:
        ball_pos[1] -= speed
    elif key == simplegui.KEY_MAP["down"]:
        ball_pos[1] += speed
    else:
        print "Key is not operable"
        
    current_key = chr(key)
    
    
    
    
def keyup(key):
    global current_key
    current_key = ''
    
def draw(draw_handler):
    global ball_pos
    draw_handler.draw_circle(ball_pos,20,3,'red','blue')

#Frame creation 

myf = simplegui.create_frame('Home',500,500)
myf.set_canvas_background("gray")
myf.set_keydown_handler(keydown)
myf.set_keyup_handler(keyup)
myf.set_draw_handler(draw)
myf.start()

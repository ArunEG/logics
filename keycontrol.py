import simplegui


#global variable section
current_key = ''

#genaral funtion defanition section



#Event handler functions
def keydown(key):
    global current_key
    current_key = chr(key)
    
    
    
    
def keyup(key):
    global current_key
    current_key = ''
    
def draw(draw_handler):
    global current_key
    if current_key in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
        draw_handler.draw_text(current_key, [30, 100], 50, "Red")    

#Frame creation 

myf = simplegui.create_frame('Home',500,500)
myf.set_canvas_background("gray")
myf.set_keydown_handler(keydown)
myf.set_keyup_handler(keyup)
myf.set_draw_handler(draw)
myf.start()

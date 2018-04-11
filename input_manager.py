from pygame import K_RIGHT, K_LEFT, K_UP, K_DOWN, K_x, KEYUP, KEYDOWN

class InputStatus:
    def __init__(self):
        self.right_pressed = False
        self.left_pressed = False
        self.down_pressed = False
        self.up_pressed = False
        self.x_pressed = False
    
    def print(self):
        print("right: ", self.right_pressed)
        print("left: ", self.left_pressed)
        print("down: ", self.down_pressed)
        print("up: ", self.up_pressed)
        print("x: ", self.x_pressed)

input_status = InputStatus()

def get_input_status():
    return input_status

def process_event(event):
    if event.type == KEYDOWN:
        key = event.key
        if key == K_RIGHT:
            input_status.right_pressed = True
        elif key == K_LEFT:
            input_status.left_pressed = True
        elif key == K_DOWN:
            input_status.down_pressed = True 
        elif key == K_UP:
            input_status.up_pressed = True
        elif key == K_x:
            input_status.x_pressed = True
    elif event.type == KEYUP:
        key = event.key
        if key == K_RIGHT:
            input_status.right_pressed = False
        elif key == K_LEFT:
            input_status.left_pressed = False
        elif key == K_DOWN:
            input_status.down_pressed = False
        elif key == K_UP:
            input_status.up_pressed = False
        elif key == K_x:
            input_status.x_pressed = False
from pico2d import *
import  random
# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.size = random.randint(0, 1)
        self.wieght = random.randint(10,50)
        if self.size == 0:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')

    def update(self):
        if self.size == 0:
            if self.y <= 70:
                 self.y = 70
            else:
                 self.y -= self.wieght/5
        else:
            if self.y <= 80:
                 self.y = 80
            else:
                 self.y -= self.wieght/5

    def draw(self):
        self.image.draw(self.x,self.y)




def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

grass = Grass()
balls = [Ball() for i in range(1, 20+1)]
ball = Ball()

running = True
# game main loop code
while running:
    handle_events()
    #game logic
    for ball in balls:
        ball.update()
    #game drawing
    clear_canvas()
    grass.draw()
    for ball in balls:
        ball.draw()
    update_canvas()

    delay(0.05)

# finalization code
close_canvas()
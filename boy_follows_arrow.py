from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

hand_x=random.randint(0, 1280)
hand_y=random.randint(0, 1024)

def handle_events():
    global running
    global x, y, hand_x, hand_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

running=True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
sprite_col=0

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    frame=(frame+1)%8

    hand.draw(hand_x, hand_y)

    character.clip_draw(frame*100, 0, 100, 100, x, y)

    update_canvas()
    delay(0.05)
    handle_events()

close_canvas()
    

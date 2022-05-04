import wrap,time
wrap.world.create_world(900,500,200,200)
speed=10
wrap.world.set_back_color(1, 186, 238)
player=wrap.sprite.add("mario-1-big",20,250,"stand")
block=wrap.sprite.add("mario-items",450,250,"moving_platform2",visible=False)
wrap.sprite.set_angle(block,180)
wrap.sprite.show(block)

@wrap.on_key_always(wrap.K_RIGHT)
def right():
    wrap.sprite.move(player,10,0)

@wrap.always()
def walk():
    global speed
    wrap.sprite.move(block,0,speed)
    if wrap.sprite.get_top(block) <0:
        speed=10
    elif wrap.sprite.get_bottom(block) > 500:
        speed= -10
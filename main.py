import wrap,time,random
wrap.world.create_world(900,500,200,200)
speed=10
speeddef=10
shetcoin=0
wrap.world.set_back_color(1, 186, 238)
xcoin=random.randint(20,860)
ycoin=random.randint(20,460)
coin=wrap.sprite.add("mario-items",xcoin,ycoin,"coin")
star=wrap.sprite.add("mario-items",820,250,"star")
player=wrap.sprite.add("mario-1-big",20,250,"stand")
block=wrap.sprite.add("mario-items",450,250,"moving_platform2",visible=False)
wrap.sprite.set_angle(block,180)
wrap.sprite.show(block)

@wrap.on_key_always(wrap.K_RIGHT)
def right():
    global speeddef,shetcoin
    wrap.sprite.move(player,10,0)
    if wrap.sprite.is_collide_sprite(player, block) == True:
        wrap.sprite.move_to(player, 20, 250)
    elif wrap.sprite.is_collide_sprite(star,player) == True:
        wrap.sprite.move_to(player,20,250)
        speeddef=speeddef+10
    elif wrap.sprite.is_collide_sprite(coin,player) == True and wrap.sprite.is_visible(coin) == True:
        shetcoin=shetcoin+1
        wrap.sprite.hide(coin)
        print(shetcoin)

@wrap.on_key_always(wrap.K_LEFT)
def left():
    global shetcoin
    wrap.sprite.move(player,-10,0)
    if wrap.sprite.is_collide_sprite(player,block) == True:
        wrap.sprite.move_to(player,20,250)
    elif wrap.sprite.is_collide_sprite(coin,player) == True and wrap.sprite.is_visible(coin) == True:
        shetcoin=shetcoin+1
        wrap.sprite.hide(coin)
        print(shetcoin)
@wrap.on_key_always(wrap.K_UP)
def up():
    global speeddef,shetcoin
    wrap.sprite.move(player,0,-10)
    if wrap.sprite.is_collide_sprite(player,block) == True:
        wrap.sprite.move_to(player,20,250)
    elif wrap.sprite.is_collide_sprite(star,player) == True:
        wrap.sprite.move_to(player,20,250)
        speeddef=speeddef+10
    elif wrap.sprite.is_collide_sprite(coin, player) == True and wrap.sprite.is_visible(coin) == True:
        shetcoin = shetcoin + 1
        wrap.sprite.hide(coin)
        print(shetcoin)
@wrap.on_key_always(wrap.K_DOWN)
def down():
    global speeddef,shetcoin
    wrap.sprite.move(player,0,10)
    if wrap.sprite.is_collide_sprite(player,block) == True:
        wrap.sprite.move_to(player,20,250)
    elif wrap.sprite.is_collide_sprite(star,player) == True:
        wrap.sprite.move_to(player,20,250)
        speeddef=speeddef+10
    elif wrap.sprite.is_collide_sprite(coin,player) == True and wrap.sprite.is_visible(coin) == True:
        shetcoin=shetcoin+1
        wrap.sprite.hide(coin)
        print(shetcoin)
@wrap.always()
def walk():
    global speed
    wrap.sprite.move(block,0,speed)
    if wrap.sprite.get_top(block) <0:
        speed=speeddef
    elif wrap.sprite.get_bottom(block) > 500:
        speed= -speeddef


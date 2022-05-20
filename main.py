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
texst1coin = wrap.sprite.add_text("+1 coin", xcoin, ycoin, "Arial")
wrap.sprite.hide(texst1coin)
textschet = wrap.sprite.add_text(str(shetcoin), 450, 20, "Arial")
def manyifs():
    global speeddef,shetcoin,xcoin,ycoin,texst1coin,textschet

    if wrap.sprite.is_collide_sprite(player,block) == True:
        wrap.sprite.move_to(player,20,250)
    elif wrap.sprite.is_collide_sprite(star,player) == True:
        wrap.sprite.hide(texst1coin)
        wrap.sprite.move_to(player,20,250)
        xcoin = random.randint(20, 860)
        ycoin = random.randint(20, 460)
        wrap.sprite.move_to(texst1coin,xcoin,ycoin)
        wrap.sprite.show(coin)
        wrap.sprite.move_to(coin,xcoin,ycoin)
        speeddef=speeddef+10
    elif wrap.sprite.is_collide_sprite(coin,player) == True and wrap.sprite.is_visible(coin) == True:
        wrap.sprite.show(texst1coin)
        shetcoin=shetcoin+1
        wrap.sprite.hide(coin)
        wrap.sprite_text.set_text(textschet,str(shetcoin))

@wrap.on_key_always(wrap.K_RIGHT)
def right():
    wrap.sprite.move(player,10,0)
    manyifs()

@wrap.on_key_always(wrap.K_LEFT)
def left():
    wrap.sprite.move(player,-10,0)
    manyifs()
@wrap.on_key_always(wrap.K_UP)
def up():
    wrap.sprite.move(player,0,-10)
    manyifs()
@wrap.on_key_always(wrap.K_DOWN)
def down():
    wrap.sprite.move(player,0,10)
    manyifs()
@wrap.always()
def walk():
    global speed
    wrap.sprite.move(block,0,speed)
    if wrap.sprite.get_top(block) <0:
        speed=speeddef
    elif wrap.sprite.get_bottom(block) > 500:
        speed= -speeddef


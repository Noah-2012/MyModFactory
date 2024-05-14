### Hier werden die Module für python abgerufen. ###

from time import *
from Terminalmodul import *
import pygame
import subprocess
import json
import random
import sys

### Hier wird eine bestimmte .json datei 'a0' für verschiedene Variablen abgerufen. ###

with open('a0.json','r') as file:
    obj = json.load(file)
N = obj['StartText']['StartTextTrue']
with open('a0.json', 'r') as file:
    obj1 = json.load(file)
N2 = obj1['StartSignal']['StartSignalTrue']
with open('a0.json', 'r') as file:
    obj2 = json.load(file)
N3 = obj2['StartText']['StartTextColorTrue']
with open('a0.json','r') as file:
    obj3 = json.load(file)
N4 = obj3['StartSignal']['StartSignalDirectory']

### Hier wird das Startsignal abgespielt mit Pygame. ###

if N2 is True:
   pygame.init()
   my_sound = pygame.mixer.Sound(N4)
   my_sound.play()
sleep(4)

### Hier ist der Startanimationen teil. ###

wer = 0, 1
wer2 = random.choice(wer)

if N is True:
    if N3 is True:
        print("\33[31;5m" + "Python Terminal 3.4 All rights reserved.")
    else:
        print("Python Terminal 3.4 All rights reserved.")
    sleep(3)
    print("\33[37;5m" + "Starting Terminal" + "\n")
    progress_bar()
    print("\n")
    for i in range(101):
        print("Libary 1/6 is loading %d%%"%i, end ='\r')
        sleep(.01)
    print("\n" + "[" + "\033[32m" + "OK" + "\033[0m" + "]" + "\n")
    for i in range(101):
        print("Libary 2/6 is loading %d%%"%i, end ='\r')
        sleep(.01)
    if wer2 == 0:
        print("\n" + "[" + "\033[32m" + "OK" + "\033[0m" + "]" + "\n")
    elif wer2 == 1:
        print("\n" + "[" + "\033[31m" + "FAILED" + "\033[0m" + "]" + "\n")
        print("File in Directory not found.")
        sys.exit()
    for i in range(101):
        print("Libary 3/6 is loading %d%%"%i, end ='\r')
        sleep(.01)
    print("\n" + "[" + "\033[32m" + "OK" + "\033[0m" + "]" + "\n")
    for i in range(101):
        print("Libary 4/6 is loading %d%%"%i, end ='\r')
        sleep(.01)
    print("\n" + "[" + "\033[32m" + "OK" + "\033[0m" + "]" + "\n")
    for i in range(101):
        print("Libary 5/6 is loading %d%%"%i, end ='\r')
        sleep(.01)
    print("\n" + "[" + "\033[32m" + "OK" + "\033[0m" + "]" + "\n")
    for i in range(101):
        print("Libary 6/6 is loading %d%%"%i, end ='\r')
        sleep(.01)
    print("\n" + "[" + "\033[32m" + "OK" + "\033[0m" + "]" + "\n")

### Definition für reboot befehl. ###

def restart():
    import sys
    print("argv was",sys.argv)
    print("sys.executable was", sys.executable)
    print("restart now")
    import os
    os.execv(sys.executable, ['python'] + sys.argv)

### Hier ist die Eingabe für das Terminal eingerichtet. ###

c = 99999999999999999
input_count = 0
for x in range(0, c):
    a = str(input('~ '))
    if a == ("sudo insert"):
        input_count += 1
        b = str(input('Disk name: '))
        insert(b)
    elif a.isnumeric() is True:
        print(a)
    elif a == ("sudo exit"):
        input_count += 1
        print("Input Counter is", input_count,".")
        exit()
        break
    elif a == ("sudo cmd"):
        for i in range(100):
            print("Connection to cmd is established. %d%%"%i, end ='\r')
            sleep(0.1)
        print("Warning!\nBefore you can enter a command,\nyou have to type [command].\nThen you can enter the command in the cmd, so to speak.\nHave fun.")
        for x in range(0, c):
            s = str(input('>>> '))
            if s == ("exit"):
                break
            else:
                try:
                    subprocess.Popen(s, shell=True)
                except:
                    print("Command entered incorrectly or does not exist.")
    elif a == ("sudo reboot"):
        restart()
### Dass nächste Programm ist eine Minecraft nachmache mit ursina. ###
    elif a == ("ursina start(minecraft)"):
        app = Ursina()
        Sky()
### Define a Voxel class. ###
### By setting the parent to scene and the model to 'cube' it becomes a 3d button. ###
        
        gun = Entity(model='cube', parent=camera, position=(.5,-.25,.25), scale=(.3,.2,1), origin_z=-.5, color=color.red, on_cooldown=False)
        gun.muzzle_flash = Entity(parent=gun, z=1, world_scale=.5, model='quad', color=color.yellow, enabled=False)

        class Voxel(Button):
            def __init__(self, position=(0,0,0)):
                super().__init__(parent=scene,
                    position=position,
                    model='cube',
                    origin_y=.5,
                    texture='grass',
                    color=color.hsv(0, 0, random.uniform(.9, 1.0)),
                    highlight_color=color.lime,
                )

        class Voxel2(Button):
            def __init__(self, position=(0,0,0)):
                super().__init__(parent=scene,
                    position=position,
                    model='cube',
                    origin_y=.5,
                    texture='emerald_block',
                    color=color.hsv(0, 0, random.uniform(.9, 1.0)),
                    highlight_color=color.lime,
                )

        for z in range(32):
            for x in range(32):
                voxel = Voxel(position=(x,0,z))

        def update():
            if held_keys['q']:
                shoot()

        def shoot():
            if not gun.on_cooldown:
                # print('shoot')
                gun.on_cooldown = True
                gun.muzzle_flash.enabled=True
                from ursina.prefabs.ursfx import ursfx
                ursfx([(0.0, 0.0), (0.1, 0.9), (0.15, 0.75), (0.3, 0.14), (0.6, 0.0)], volume=0.5, wave='noise', pitch=random.uniform(-13,-12), pitch_change=-12, speed=3.0)
                invoke(gun.muzzle_flash.disable, delay=.05)
                invoke(setattr, gun, 'on_cooldown', False, delay=.15)
                if mouse.hovered_entity and hasattr(mouse.hovered_entity, 'hp'):
                    mouse.hovered_entity.hp -= 10
                    mouse.hovered_entity.blink(color.red)


        def input(key):
            if key == 'right mouse down':
                hit_info = raycast(camera.world_position, camera.forward, distance=5)
                if hit_info.hit:
                    Voxel2(position=hit_info.entity.position + hit_info.normal)
            if key == 'left mouse down' and mouse.hovered_entity:
                destroy(mouse.hovered_entity)


        player = FirstPersonController()
        app.run()
### Dass ist sozusagen ein inventar aus minecraft. ###
    elif a == ("ursina start(inventory)"):
        from ursina import *


        class Inventory(Entity):
            def __init__(self, width=5, height=8, **kwargs):
                super().__init__(
                    parent = camera.ui,
                    model = Quad(radius=.015),
                    texture = 'white_cube',
                    texture_scale = (width, height),
                    scale = (width*.1, height*.1),
                    origin = (-.5,.5),
                    position = (-.3,.4),
                    color = color.hsv(0, 0, .1, .9),
                    )

                self.width = width
                self.height = height

                for key, value in kwargs.items():
                    setattr(self, key, value)


            def find_free_spot(self):
                for y in range(self.height):
                    for x in range(self.width):
                        grid_positions = [(int(e.x*self.texture_scale[0]), int(e.y*self.texture_scale[1])) for e in self.children]
                        print(grid_positions)

                        if not (x, -y) in grid_positions:
                            print('found free spot:', x, y)
                            return x, y


            def append(self, item, x=0, y=0):
                print('add item:', item)

                if len(self.children) >= self.width*self.height:
                    print('inventory full')
                    error_message = Text('<red>Inventory is full!', origin=(0,-1.5), x=-.5, scale=2)
                    destroy(error_message, delay=1)
                    return

                x, y = self.find_free_spot()

                icon = Draggable(
                    parent = self,
                    model = 'quad',
                    texture = item,
                    color = color.white,
                    scale_x = 1/self.texture_scale[0],
                    scale_y = 1/self.texture_scale[1],
                    origin = (-.5,.5),
                    x = x * 1/self.texture_scale[0],
                    y = -y * 1/self.texture_scale[1],
                    z = -.5,
                    )
                name = item.replace('_', ' ').title()
    
                if random.random() < .25:
                    icon.color = color.gold
                    name = '<orange>Rare ' + name

                icon.tooltip = Tooltip(name)
                icon.tooltip.background.color = color.hsv(0,0,0,.8)


                def drag():
                    icon.org_pos = (icon.x, icon.y)
                    icon.z -= .01   # ensure the dragged item overlaps the rest

                def drop():
                    icon.x = int((icon.x + (icon.scale_x/2)) * self.width) / self.width
                    icon.y = int((icon.y - (icon.scale_y/2)) * self.height) / self.height
                    icon.z += .01

                # if outside, return to original position
                    if icon.x < 0 or icon.x >= 1 or icon.y > 0 or icon.y <= -1:
                        icon.position = (icon.org_pos)
                        return

                # if the spot is taken, swap positions
                    for c in self.children:
                        if c == icon:
                            continue

                        if c.x == icon.x and c.y == icon.y:
                            print('swap positions')
                            c.position = icon.org_pos

                icon.drag = drag
                icon.drop = drop



        if __name__ == '__main__':
            app = Ursina()

            inventory = Inventory()

            def add_item():
                inventory.append(random.choice(('bag', 'bow_arrow', 'gem', 'orb', 'sword')))

            add_item()
            add_item()
            add_item_button = Button(
                scale = (.1,.1),
                x = -.5,
                color = color.lime.tint(-.25),
                text = '+',
                tooltip = Tooltip('Add random item'),
                on_click = add_item
                )
            background = Entity(parent=camera.ui, model='quad', texture='shore', scale_x=camera.aspect_ratio, z=1)

            Cursor(texture='cursor', scale=.1)
            mouse.visible = False

        app.run()
    else:
        input_count += 1
        with open('b0.json', 'r') as file:
            obj4 = json.load(file)
        ErrnoInput = obj4['errorcodes']['InputNoOrderErrno']
        print("No Terminal input order." ,ErrnoInput)
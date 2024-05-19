import arcade
import random
import time
import math
import arcade.examples
import arcade.gui

window_name = "Bak_Sim"
window_width = 1540
window_height = 860
bac_feel = 200
bacteria_image = "bacteria1.jpg"
testures_list = ["bacteria1.jpg", "bacteria2.jpg", "bacteria3.jpg", "bacteria4.jpg", "bacteria5.jpg", "bacteria6.jpg", "bacteria7.jpg", "bacteria8.jpg", "bacteria9.jpg", "bacteria10.jpg", ]
food_image = "food.png"
anti_image = "anty_bac.png"

class Bacteria(arcade.Sprite):
    def __init__(self, life_time, spin_time, hungry_time, speed, spin_speed,image, max_energy, gen_code, energy, start_life_time, last_eat_time, start_time_spin, started_spin, mutation_chance, ganibal, food_like, life, eaten_anti, rodila):
        super().__init__(bacteria_image, 1, angle = 0)
        self.start_life_time = start_life_time
        self.life_time = life_time
        self.spin_time = spin_time
        self.hungry_time = hungry_time
        self.speed = speed
        self.spin_speed = spin_speed
        self.last_eat_time = last_eat_time
        self.start_time_spin = start_time_spin
        self.started_spin = started_spin
        self.mutation_chance = mutation_chance
        self.image = image
        self.gen_code = gen_code
        self.max_energy = max_energy
        self.energy = energy
        self.ganibal = ganibal
        self.food_like = food_like
        self.life = life
        self.eaten_anti = eaten_anti
        self.rodila = rodila

        self.start_life_time = time.time()
        self.texture = arcade.load_texture(self.image)


    def go(self):
        self.change_x = math.cos(self.angle/180 * 3.14) * self.speed
        self.change_y = math.sin(self.angle/180 * 3.14) * self.speed

    def mutation(self):
        self.gen_code[random.randint(0,5)] = random.randint(0,1000)
        self.life_time = (self.gen_code[0])
        self.spin_time = self.gen_code[1] / 100
        self.hungry_time = self.gen_code[2] / 10
        self.speed = (self.gen_code[3] / 100)
        self.spin_speed = self.gen_code[4]
        self.max_energy = self.gen_code[6]

        if random.randint(0, 10000) == 0:
            self.eaten_anti = False




class Food(arcade.Sprite):
    def __init__(self, anti_biot, exist):
        super().__init__(food_image, 1)

        self.anti_biot = anti_biot
        self.exist = exist

 



class Simular(arcade.Window):
    def __init__(self):
        super().__init__(window_width, window_height, window_name, fullscreen=True, resizable=True) #создаём окно 
        self.bacteria_image = "bacteria.jpg"
        self.background_image = "background.png"

        self.bak_list = arcade.SpriteList()
        self.food_list = arcade.SpriteList()

        self.new_life_time = 1000
        self.new_spin_time = 10
        self.new_hungry_time = 20
        self.new_speed = 1
        self.new_spin_speed = 1
        self.new_image = 0
        self.new_max_energy = 1000
        self.eat_tipe = 1
        self.new_scale = 1
        self.col_wo = 1
        self.food_col_wo = 5
        self.new_ganibal = False
        self.new_food_like = True

        self.pause = False
        self.hide = False

        self.ful_screen = True

        self.sum_food_like = 0
        self.sum_ganib = 0


        self.image_new_bac = arcade.Sprite()
        self.image_new_bac.set_position(150, 425)
        self.image_new_bac.texture = arcade.load_texture(testures_list[0])

        self.camera = arcade.Camera(window_width, window_height)

        self.manager_button_up = arcade.gui.UIManager()
        self.manager_button_up.enable()
        self.manager_v_up_box = arcade.gui.UIBoxLayout()

        self.button_up_life_time = arcade.gui.UIFlatButton(text="Life time up", width = 100, height = 75)
        self.manager_v_up_box.add(self.button_up_life_time.with_space_around(bottom=0))

        self.button_up_spin_time = arcade.gui.UIFlatButton(text="Spin time up", width=100, height = 75)
        self.manager_v_up_box.add(self.button_up_spin_time.with_space_around(bottom=0))

        self.button_up_hungry_time = arcade.gui.UIFlatButton(text="Hungry time up", width=100, height = 75)
        self.manager_v_up_box.add(self.button_up_hungry_time.with_space_around(bottom=0))

        self.button_up_speed = arcade.gui.UIFlatButton(text="Speed Up", width=100, height = 75)
        self.manager_v_up_box.add(self.button_up_speed.with_space_around(bottom=0))

        self.button_up_speed_spin = arcade.gui.UIFlatButton(text="Speed spin Up", width=100, height = 75)
        self.manager_v_up_box.add(self.button_up_speed_spin.with_space_around(bottom=0))

        self.button_image_up = arcade.gui.UIFlatButton(text="image number up", width=100, height = 75)
        self.manager_v_up_box.add(self.button_image_up.with_space_around(bottom=0))

        self.button_max_energy_up = arcade.gui.UIFlatButton(text="max energy up", width=100, height = 75)
        self.manager_v_up_box.add(self.button_max_energy_up.with_space_around(bottom=0))

        self.button_eat_tipe_up = arcade.gui.UIFlatButton(text="eat type up", width=100, height = 75)
        self.manager_v_up_box.add(self.button_eat_tipe_up.with_space_around(bottom=0))

        self.button_scale_up = arcade.gui.UIFlatButton(text="scale up", width=100, height = 75)
        self.manager_v_up_box.add(self.button_scale_up.with_space_around(bottom=0))

        self.button_col_wo_up = arcade.gui.UIFlatButton(text="amount up", width=100, height = 75)
        self.manager_v_up_box.add(self.button_col_wo_up.with_space_around(bottom=0))

        self.button_spawn = arcade.gui.UIFlatButton(text="spawn", width=100, height = 75)
        self.manager_v_up_box.add(self.button_spawn.with_space_around(bottom=0))


        self.manager_button_up.add(
            arcade.gui.UIAnchorWidget(
                anchor_x = "left",
                anchor_y="center_y",
                child=self.manager_v_up_box))




        self.manager_button_down = arcade.gui.UIManager()
        self.manager_button_down.enable()
        self.manager_v_down_box = arcade.gui.UIBoxLayout()

        self.button_down_life_time = arcade.gui.UIFlatButton(text="Life time down", width = 100, height = 75)
        self.manager_v_down_box.add(self.button_down_life_time.with_space_around(bottom=0))

        self.button_down_spin_time = arcade.gui.UIFlatButton(text="Spin time down", width=100, height = 75)
        self.manager_v_down_box.add(self.button_down_spin_time.with_space_around(bottom=0))

        self.button_down_hungry_time = arcade.gui.UIFlatButton(text="Hungry time down", width=100, height = 75)
        self.manager_v_down_box.add(self.button_down_hungry_time.with_space_around(bottom=0))

        self.button_down_speed = arcade.gui.UIFlatButton(text="Speed down", width=100, height = 75)
        self.manager_v_down_box.add(self.button_down_speed.with_space_around(bottom=0))

        self.button_down_speed_spin = arcade.gui.UIFlatButton(text="Speed spin down", width=100, height = 75)
        self.manager_v_down_box.add(self.button_down_speed_spin.with_space_around(bottom=0))

        self.button_image_down = arcade.gui.UIFlatButton(text="image number down", width=100, height = 75)
        self.manager_v_down_box.add(self.button_image_down.with_space_around(bottom=0))

        self.button_max_energy_down = arcade.gui.UIFlatButton(text="max energy down", width=100, height = 75)
        self.manager_v_down_box.add(self.button_max_energy_down.with_space_around(bottom=0))

        self.button_eat_tipe_down = arcade.gui.UIFlatButton(text="eat type down", width=100, height = 75)
        self.manager_v_down_box.add(self.button_eat_tipe_down.with_space_around(bottom=0))

        self.button_scale_down = arcade.gui.UIFlatButton(text="scale down", width=100, height = 75)
        self.manager_v_down_box.add(self.button_scale_down.with_space_around(bottom=0))

        self.button_col_wo_down = arcade.gui.UIFlatButton(text="amount down", width=100, height = 75)
        self.manager_v_down_box.add(self.button_col_wo_down.with_space_around(bottom=0))

        self.button_kill = arcade.gui.UIFlatButton(text="kill all bac", width=100, height = 75)
        self.manager_v_down_box.add(self.button_kill.with_space_around(bottom=0))

        self.manager_button_down.add(
            arcade.gui.UIAnchorWidget(
                anchor_x = "left",
                align_x= 200,
                anchor_y="center_y",
                child=self.manager_v_down_box))

        self.button_up_life_time.on_click = self.on_click_up_life_time

        self.button_up_spin_time.on_click = self.on_click_up_spin_time

        self.button_up_hungry_time.on_click = self.on_click_up_hungry_time

        self.button_up_speed.on_click = self.on_click_up_speed

        self.button_up_speed_spin.on_click = self.on_click_up_speed_spin

        self.button_image_up.on_click = self.on_click_image_up

        self.button_max_energy_up.on_click = self.on_click_max_energy_up

        self.button_eat_tipe_up.on_click = self.on_click_eat_tipe_up

        self.button_scale_up.on_click = self.on_click_scale_up

        self.button_col_wo_up.on_click = self.on_click_col_wo_up

        self.button_spawn.on_click = self.on_click_spawn


        self.button_down_life_time.on_click = self.on_click_down_life_time

        self.button_down_spin_time.on_click = self.on_click_down_spin_time

        self.button_down_hungry_time.on_click = self.on_click_down_hungry_time

        self.button_down_speed.on_click = self.on_click_down_speed

        self.button_down_speed_spin.on_click = self.on_click_down_speed_spin

        self.button_image_down.on_click = self.on_click_image_down

        self.button_max_energy_down.on_click = self.on_click_max_energy_down

        self.button_eat_tipe_down.on_click = self.on_click_eat_tipe_down

        self.button_scale_down.on_click = self.on_click_scale_down

        self.button_col_wo_down.on_click = self.on_click_col_wo_down

        self.button_kill.on_click = self.on_click_kill

        self.manager_menu = arcade.gui.UIManager()
        self.manager_menu.enable()
        self.manager_v_menu = arcade.gui.UIBoxLayout()

        self.button_pause = arcade.gui.UIFlatButton(text="pause", width=100, height = 75)
        self.manager_v_menu.add(self.button_pause.with_space_around(bottom=0))

        self.button_contin = arcade.gui.UIFlatButton(text="contin", width=100, height = 75)
        self.manager_v_menu.add(self.button_contin.with_space_around(bottom=0))

        self.button_hide = arcade.gui.UIFlatButton(text="hide", width=100, height = 75)
        self.manager_v_menu.add(self.button_hide.with_space_around(bottom=0))

        self.button_return = arcade.gui.UIFlatButton(text="return", width=100, height = 75)
        self.manager_v_menu.add(self.button_return.with_space_around(bottom=0))

        self.button_exit = arcade.gui.UIFlatButton(text="exit", width=100, height = 75)
        self.manager_v_menu.add(self.button_exit.with_space_around(bottom=0))

        self.manager_menu.add(
            arcade.gui.UIAnchorWidget(
                anchor_x = "left",
                align_x= 1440,
                anchor_y="center_y",
                child=self.manager_v_menu))

        self.button_pause.on_click = self.on_click_pause

        self.button_contin.on_click = self.on_click_contin

        self.button_hide.on_click = self.on_click_hide

        self.button_return.on_click = self.on_click_return

        self.button_exit.on_click = self.on_click_exit

        self.manager_food = arcade.gui.UIManager()
        self.manager_food.enable()
        self.manager_v_food_up = arcade.gui.UIBoxLayout()
        self.manager_v_food_down = arcade.gui.UIBoxLayout()
        self.manager_v_food_kill = arcade.gui.UIBoxLayout()

        self.button_food_col_up = arcade.gui.UIFlatButton(text="food up", width=100, height = 75)
        self.manager_v_food_up.add(self.button_food_col_up.with_space_around(bottom=0))

        self.button_spawn_food = arcade.gui.UIFlatButton(text="Spawn food", width=100, height = 75)
        self.manager_v_food_up.add(self.button_spawn_food.with_space_around(bottom=0))

        self.button_food_col_down = arcade.gui.UIFlatButton(text="food down", width=100, height = 75)
        self.manager_v_food_down.add(self.button_food_col_down.with_space_around(bottom=0))

        self.button_spawn_anti = arcade.gui.UIFlatButton(text="Spawn anti", width=100, height = 75)
        self.manager_v_food_down.add(self.button_spawn_anti.with_space_around(bottom=0))

        self.button_kill_food = arcade.gui.UIFlatButton(text="Kill food", width=100, height = 75)
        self.manager_v_food_kill.add(self.button_kill_food.with_space_around(bottom=0))

        self.button_kill_anti = arcade.gui.UIFlatButton(text="Kill anti", width=100, height = 75)
        self.manager_v_food_kill.add(self.button_kill_anti.with_space_around(bottom=0))

        self.manager_food.add(
            arcade.gui.UIAnchorWidget(
                anchor_x = "left",
                align_x= 1000,
                anchor_y="center_y",
                align_y= 340,
                child=self.manager_v_food_up))
        
        self.manager_food.add(
            arcade.gui.UIAnchorWidget(
                anchor_x = "left",
                align_x= 1200,
                anchor_y="center_y",
                align_y= 340,
                child=self.manager_v_food_down))
        
        self.manager_food.add(
            arcade.gui.UIAnchorWidget(
                anchor_x = "left",
                align_x= 1300,
                anchor_y="center_y",
                align_y= 340,
                child=self.manager_v_food_kill))
        
        self.button_food_col_up.on_click = self.on_click_food_col_up

        self.button_spawn_food.on_click = self.on_click_spawn_food

        self.button_food_col_down.on_click = self.on_click_food_col_down

        self.button_spawn_anti.on_click = self.on_click_spawn_anti

        self.button_kill_food.on_click = self.on_click_kill_food

        self.button_kill_anti.on_click = self.on_click_kill_anti


    def on_click_up_life_time(self, event):
        self.new_life_time += 10

    def on_click_up_spin_time(self, event):
        self.new_spin_time += 5

    def on_click_up_hungry_time(self, event):
        self.new_hungry_time += 5

    def on_click_up_speed(self, event):
        self.new_speed += 1

    def on_click_up_speed_spin(self, event):
        self.new_spin_speed += 1

    def on_click_image_up(self, event):
        self.new_image += 1

    def on_click_max_energy_up(self, event):
        self.new_max_energy += 100

    def on_click_eat_tipe_up(self, event):
        self.eat_tipe += 1

    def on_click_scale_up(self, event):
        self.new_scale += 0.1
        self.new_scale = round(self.new_scale,1)

    def on_click_col_wo_up(self, event):
        self.col_wo += 1

    def on_click_down_life_time(self, event):
        self.new_life_time -= 10

    def on_click_down_spin_time(self, event):
        self.new_spin_time -= 5

    def on_click_down_hungry_time(self, event):
        self.new_hungry_time -= 5

    def on_click_down_speed(self, event):
        self.new_speed -= 1

    def on_click_down_speed_spin(self, event):
        self.new_spin_speed -= 1

    def on_click_image_down(self, event):
        self.new_image -= 1

    def on_click_max_energy_down(self, event):
        self.new_max_energy -= 100

    def on_click_eat_tipe_down(self, event):
        self.eat_tipe -= 1

    def on_click_scale_down(self, event):
        self.new_scale -= 0.1
        self.new_scale = round(self.new_scale,1)

    def on_click_col_wo_down(self, event):
        self.col_wo -= 1

    def on_click_food_col_up(self, event):
        self.food_col_wo += 1

    def on_click_food_col_down(self, event):
        self.food_col_wo -= 1

    def on_click_spawn(self, event):
        num = 0
        while num < self.col_wo:
            self.x = random.randint(0, window_width)
            self.y = random.randint(0, window_height)
            self.bak = Bacteria(self.new_life_time, self.new_spin_time, self.new_hungry_time, self.new_speed, self.new_spin_speed, testures_list[self.new_image],self.new_max_energy, [self.new_life_time, self.new_spin_time, self.new_hungry_time, self.new_speed, self.new_spin_speed, self.new_image,self.new_max_energy], self.new_max_energy - 100, 0, 0, 0, 0, 0, self.new_ganibal, self.new_food_like, True, False, False)
            self.bak.last_eat_time = time.time()
            self.bak.angle = random.randint(0, 360)
            self.bak_list.append(self.bak)
            if not self.pause:
                self.bak.go()
            self.bak.scale = self.new_scale
            self.bak.set_position(self.x, self.y)

            if self.pause:
                self.bac.life_time = 9999999999
                self.bac.spin_time = 0
                self.bac.hungry_time = 99999999999
                self.bac.speed = 0
                self.bac.spin_speed = 0
                self.bac.stop()

            num += 1

    def on_click_spawn_anti(self, event):
        num = 0
        while num < self.food_col_wo:
            self.x1 = random.randint(0, window_width)
            self.y1 = random.randint(0, window_height)
            self.food = Food(True, True)
            self.food.set_position(self.x1, self.y1)
            self.food_list.append(self.food)
            self.food.texture = arcade.load_texture(anti_image)
            num += 1

    def on_click_spawn_food(self, event):
        num = 0
        while num < self.food_col_wo:
            self.x1 = random.randint(0, window_width)
            self.y1 = random.randint(0, window_height)
            self.food = Food(False, True)
            self.food.set_position(self.x1, self.y1)
            self.food_list.append(self.food)
            self.food.texture = arcade.load_texture(food_image)
            num += 1

    def on_click_kill(self, event):
        for x in self.bak_list:
            x.set_position(9999, 9999)
            x.life = False

    def on_click_kill_food(self, event):
        for f in self.food_list:
            if not f.anti_biot:
                f.set_position(9999, 9999)
                f.exist = False

    def on_click_kill_anti(self, event):
        for a in self.food_list:
            if a.anti_biot:
                a.set_position(9999, 9999)
                a.exist = False

    def on_click_pause(self, event):
        for p in self.bak_list:
            p.life_time = 9999999999
            p.spin_time = 0
            p.hungry_time = 99999999999
            p.speed = 0
            p.spin_speed = 0
            p.stop()

        self.pause = True


    def on_click_contin(self, event):
        for p in self.bak_list:
            p.life_time = p.gen_code[0]
            p.spin_time = p.gen_code[1] 
            p.hungry_time = p.gen_code[2] 
            p.speed = p.gen_code[3] 
            p.spin_speed = p.gen_code[4]
            p.max_energy = p.gen_code[6]
            p.go()


        self.pause = False

    def on_click_hide(self, event):
        self.manager_button_up.clear()
        self.manager_button_down.clear()
        self.manager_food.clear()

        self.manager_button_up.add(
            arcade.gui.UIAnchorWidget(
                anchor_x = "left",
                align_x= 9999,
                anchor_y="center_y",
                child=self.manager_v_up_box))
        
        self.manager_button_down.add(
            arcade.gui.UIAnchorWidget(
                anchor_x = "left",
                align_x= 9999,
                anchor_y="center_y",
                child=self.manager_v_down_box))
        
        self.manager_food.add(
            arcade.gui.UIAnchorWidget(
                anchor_x = "left",
                align_x= 10999,
                anchor_y="center_y",
                align_y= 340,
                child=self.manager_v_food_up))
        
        self.manager_food.add(
            arcade.gui.UIAnchorWidget(
                anchor_x = "left",
                align_x= 9999,
                anchor_y="center_y",
                align_y= 340,
                child=self.manager_v_food_down))
        
        self.manager_food.add(
            arcade.gui.UIAnchorWidget(
                anchor_x = "left",
                align_x= 9999,
                anchor_y="center_y",
                align_y= 340,
                child=self.manager_v_food_kill))

        self.image_new_bac.set_position(9999, 9999)
        self.hide = True

    def on_click_return(self, event):

        self.manager_button_up.clear()
        self.manager_button_down.clear()
        self.manager_food.clear()

        self.manager_button_up.add(
            arcade.gui.UIAnchorWidget(
                anchor_x = "left",
                anchor_y="center_y",
                child=self.manager_v_up_box))
        
        self.manager_button_down.add(
            arcade.gui.UIAnchorWidget(
                anchor_x = "left",
                align_x=200,
                anchor_y="center_y",
                child=self.manager_v_down_box))
        

        self.manager_food.add(
            arcade.gui.UIAnchorWidget(
                anchor_x = "left",
                align_x= 1000,
                anchor_y="center_y",
                align_y= 340,
                child=self.manager_v_food_up))
        
        self.manager_food.add(
            arcade.gui.UIAnchorWidget(
                anchor_x = "left",
                align_x= 1200,
                anchor_y="center_y",
                align_y= 340,
                child=self.manager_v_food_down))
        
        self.manager_food.add(
            arcade.gui.UIAnchorWidget(
                anchor_x = "left",
                align_x= 1300,
                anchor_y="center_y",
                align_y= 340,
                child=self.manager_v_food_kill))

        self.image_new_bac.set_position(150, 425)
        self.hide = False

    def on_click_exit(self, event):
        arcade.exit()

    def on_draw(self):
        arcade.start_render()
        self.clear()
        arcade.set_background_color(arcade.color.WHITE)
        self.food_list.draw()
        self.bak_list.draw()
        self.manager_button_up.draw()
        self.manager_button_down.draw()
        self.manager_menu.draw()
        self.manager_food.draw()
        self.image_new_bac.draw()
        self.camera.use()
        if not self.hide:
            arcade.draw_text(str(self.new_life_time), 110, 800, arcade.color.BLACK, font_size=25)
            arcade.draw_text(str(self.new_spin_time), 110, 725, arcade.color.BLACK, font_size=25)
            arcade.draw_text(str(self.new_hungry_time), 110, 650, arcade.color.BLACK, font_size=25)
            arcade.draw_text(str(self.new_speed), 110, 575, arcade.color.BLACK, font_size=25)
            arcade.draw_text(str(self.new_spin_speed), 110, 500, arcade.color.BLACK, font_size=25)
            arcade.draw_text(str(self.new_max_energy), 110, 350, arcade.color.BLACK, font_size=25)
            arcade.draw_text(str(self.eat_tipe), 110, 275, arcade.color.BLACK, font_size=25)
            arcade.draw_text(str(self.new_scale), 110, 200, arcade.color.BLACK, font_size=25)
            arcade.draw_text(str(self.col_wo), 110, 125, arcade.color.BLACK, font_size=25)
            arcade.draw_text(str(self.food_col_wo), 1125, 800, arcade.color.BLACK, font_size=25)
            arcade.draw_text(("хищники: ",str(self.sum_food_like)), 550, 800, arcade.color.RED, font_size=20)
            arcade.draw_text(("травоядные: ",str(self.sum_ganib)), 550, 750, arcade.color.RED, font_size=20)

    def update(self, delta_time: float):
        self.bak_list.update()
        self.food_list.update()
        self.image_new_bac.update()
        if self.new_image > -1 and self.new_image < 10:
            self.image_new_bac.texture = arcade.load_texture(testures_list[self.new_image])
        for i in self.bak_list:

            if i.life_time <= time.time() - i.start_life_time:
                    i.life = False

            if i.hungry_time <= time.time() - i.last_eat_time and not i.started_spin and not self.pause:
                i.stop()
                i.change_angle = i.spin_speed
                i.start_time_spin = time.time()
                i.started_spin = True

            if i.spin_time <= time.time() - i.start_time_spin and i.started_spin and not self.pause:
                i.change_angle = 0
                i.go()
                i.last_eat_time = time.time()
                i.started_spin = False

            if i.mutation_chance % 10 > 9:
                i.mutation()

            if i.mutation_chance % 10 > 9.5:
                i.rodila = False

            collide_food = arcade.check_for_collision_with_list(i, self.food_list)
            if collide_food and i.food_like and not self.pause:
                i.last_eat_time = time.time()
                i.change_angle = 0
                i.go()
                for j in collide_food:
                    j.set_position(9999, 9999)
                    if j.anti_biot:
                        i.eaten_anti = True
                    if not j.anti_biot:
                        i.energy += 400
                    j.kill()

            collide_bak = arcade.check_for_collision_with_list(i, self.bak_list)
            if collide_bak and not self.pause:
                for s in collide_bak:
                    num_1 = 0
                    num_2 = 0
                    if i.scale < s.scale and i.ganibal and i.energy <= i.max_energy / 1.3 and s.food_like:
                        s.set_position(9999, 9999)
                        i.energy += s.energy
                        i.last_eat_time = time.time()
                        while num_1 <= 2:
                            self.bak = Bacteria(i.life_time, i.spin_time, i.hungry_time, i.speed, i.spin_speed, i.image, i.max_energy, i.gen_code, i.max_energy, 0, 0, 0, False, 0, i.ganibal, i.food_like, True, i.eaten_anti, False)
                            self.bak.scale = s.scale / 1.5
                            self.bak.angle = random.randint(0, 360)
                            self.bak.last_eat_time = time.time()
                            self.bak.set_position(i.center_x, i.center_y)
                            self.bak.go()
                            self.bak_list.append(self.bak)
                            num_1 += 1
                        i.kill()
                        s.kill()

                    if i.scale > s.scale and s.ganibal and s.energy <= s.max_energy / 1.3 and i.food_like:
                        i.set_position(9999, 9999)
                        s.energy += i.energy
                        s.last_eat_time = time.time()
                        while num_2 <= 2:
                            self.bak = Bacteria(s.life_time, s.spin_time, s.hungry_time, s.speed, s.spin_speed, s.image, s.max_energy, s. gen_code, s.max_energy, 0, 0, 0, False, 0, s.ganibal, s.food_like, True, s.eaten_anti, False)
                            self.bak.scale = i.scale / 1.5
                            self.bak.angle = random.randint(0, 360)
                            self.bak.last_eat_time = time.time()
                            self.bak.set_position(s.center_x, s.center_y)
                            self.bak.go()
                            self.bak_list.append(self.bak)
                            num_2 += 1
                        s.kill()
                        i.kill()


            if i.energy >= i.max_energy:
                if not i.eaten_anti:
                    i.scale += 0.1
                i.speed += 1
                i.spin_speed += 1
                i.energy -= i.max_energy / 2
                energy_spend_var = random.randint(1, 2)
                if energy_spend_var == 2 and not i.eaten_anti and not i.rodila and i.food_like:
                    self.bak = Bacteria(i.life_time, i.spin_time, i.hungry_time, i.speed, i.spin_speed, i. image, i.max_energy, i. gen_code, i.max_energy / 2, 0, 0, 0, False, 0, i.ganibal, i.food_like, True, i.eaten_anti, True)
                    self.bak.scale = i.scale
                    self.bak.last_eat_time = time.time()
                    self.bak.angle = random.randint(0, 360)
                    self.bak.go()
                    self.bak.set_position(i.center_x, i.center_y)
                    self.bak_list.append(self.bak)
                    i.energy -= i.max_energy / 2
                    i.rodila = True

            if i.energy < 0:
                i.scale -= 0.2
                i.speed -= 1
                i.spin_speed -= 1
                i.energy += i.max_energy / 2

            if i.scale <= 0.1:
                i.life = False

            i.energy -= i.speed * i.speed * i.scale  / 100

            if i.right <= 0:
                i.set_position(window_width, i.center_y)

            if i.bottom >= window_height:
                i.set_position(i.center_x , 0)

            if i.left >= window_width:
                i.set_position(0, i.center_y)
                
            if i.top  <= 0:
                i.set_position(i.center_x, window_height)

            if not i.life:
                self.food = Food(False, True)
                self.food.scale = i.scale
                self.food.set_position(i.center_x, i.center_y)
                self.food_list.append(self.food)
                i.set_position(9999, 9999)
                i.kill()

            i.mutation_chance = time.time() - i.start_life_time

        if self.eat_tipe == 1:
            self.new_ganibal = True
            self.new_food_like = False

        if self.eat_tipe == 2:
            self.new_ganibal = False
            self.new_food_like = True

        if self.eat_tipe > 2:
            self.eat_tipe = 2

        if self.eat_tipe < 1:
            self.eat_tipe = 1

        if self.new_scale >= 5:
            self.new_scale = 4.9

        if self.new_scale <= 0.1:
            self.new_scale = 0.2

        if self.col_wo < 0:
            self.col_wo = 0

        if self.food_col_wo < 0:
            self.food_col_wo = 0

        if self.new_max_energy < 0:
            self.new_max_energy = 0

        if self.new_image < 0:
            self.new_image = 0

        if self.new_image > 9:
            self.new_image = 9

        if self.new_spin_speed < 0:
            self.new_spin_speed = 0

        if self.new_speed < 0:
            self.new_speed = 0  

        if self.new_hungry_time < 0:
            self.new_hungry_time = 0

        if self.new_spin_time < 0:
            self.new_spin_time = 0

        if self.new_life_time < 0:     
            self.new_life_time = 0

        if self.new_life_time > 1000:     
            self.new_life_time = 1000

        for a in self.food_list:
            if not a.exist:
                a.set_position(9999, 9999)
                a.kill()
            if len(self.bak_list) > 0:
                if i.food_like:
                    if ((i.center_x - a.center_x)**2 + (i.center_y - a.center_y)**2) ** 0.5 <= bac_feel:

                        if i.center_x > a.center_x and i.center_y > a.center_y and not a.anti_biot:
                            i.angle =  -1 * math.degrees(math.acos((i.center_y - a.center_y)/ ((i.center_x - a.center_x)**2 + (i.center_y - a.center_y)**2) ** 0.5)) - 90
                            i.go()

                        if i.center_x < a.center_x and i.center_y > a.center_y and not a.anti_biot:
                            i.angle =  math.degrees(math.acos((i.center_y - a.center_y)/ ((i.center_x - a.center_x)**2 + (i.center_y - a.center_y)**2) ** 0.5)) - 90
                            i.go()

                        if i.center_x < a.center_x and i.center_y < a.center_y and not a.anti_biot:
                            i.angle =  math.degrees(math.acos((i.center_y - a.center_y)/ ((i.center_x - a.center_x)**2 + (i.center_y - a.center_y)**2) ** 0.5))
                            i.go()

                        if i.center_x > a.center_x and i.center_y < a.center_y and not a.anti_biot:
                            i.angle =  math.degrees(math.acos((i.center_y - a.center_y)/ ((i.center_x - a.center_x)**2 + (i.center_y - a.center_y)**2) ** 0.5)) + 90
                            i.go()

                        if i.center_x > a.center_x and i.center_y > a.center_y and a.anti_biot:
                            i.angle =  -1 * math.degrees(math.acos((i.center_y - a.center_y)/ ((i.center_x - a.center_x)**2 + (i.center_y - a.center_y)**2) ** 0.5)) - 90 + 180
                            i.go()

                        if i.center_x < a.center_x and i.center_y > a.center_y and a.anti_biot:
                            i.angle =  math.degrees(math.acos((i.center_y - a.center_y)/ ((i.center_x - a.center_x)**2 + (i.center_y - a.center_y)**2) ** 0.5)) - 90 + 180
                            i.go()

                        if i.center_x < a.center_x and i.center_y < a.center_y and a.anti_biot:
                            i.angle =  math.degrees(math.acos((i.center_y - a.center_y)/ ((i.center_x - a.center_x)**2 + (i.center_y - a.center_y)**2) ** 0.5)) + 180
                            i.go()

                        if i.center_x > a.center_x and i.center_y < a.center_y and a.anti_biot:
                            i.angle =  math.degrees(math.acos((i.center_y - a.center_y)/ ((i.center_x - a.center_x)**2 + (i.center_y - a.center_y)**2) ** 0.5)) + 90 + 180
                            i.go()

        for bakt in self.bak_list:
            if len(self.bak_list) > 0:
                if bakt.food_like and i.ganibal:
                    if ((i.center_x - bakt.center_x)**2 + (i.center_y - bakt.center_y)**2) ** 0.5 <= bac_feel:

                        if i.center_x > bakt.center_x and i.center_y > bakt.center_y:
                            i.angle =  -1 * math.degrees(math.acos((i.center_y - bakt.center_y)/ ((i.center_x - bakt.center_x)**2 + (i.center_y - bakt.center_y)**2) ** 0.5)) - 90
                            bakt.angle = i.angle
                            i.go()
                            bakt.go()

                        if i.center_x < bakt.center_x and i.center_y > bakt.center_y:
                            i.angle =  math.degrees(math.acos((i.center_y - bakt.center_y)/ ((i.center_x - bakt.center_x)**2 + (i.center_y - bakt.center_y)**2) ** 0.5)) - 90
                            bakt.angle = i.angle
                            i.go()
                            bakt.go()

                        if i.center_x < bakt.center_x and i.center_y < bakt.center_y:
                            i.angle =  math.degrees(math.acos((i.center_y - bakt.center_y)/ ((i.center_x - bakt.center_x)**2 + (i.center_y - bakt.center_y)**2) ** 0.5))
                            bakt.angle = i.angle
                            i.go()
                            bakt.go()

                        if i.center_x > bakt.center_x and i.center_y < bakt.center_y:
                            i.angle =  math.degrees(math.acos((i.center_y - bakt.center_y)/ ((i.center_x - bakt.center_x)**2 + (i.center_y - bakt.center_y)**2) ** 0.5)) + 90
                            bakt.angle = i.angle
                            i.go()
                            bakt.go()
        itog_ganib = 0
        itog_food_like = 0
        for m in self.bak_list:
            if m.ganibal:
                itog_ganib += 1
            elif m.food_like:
                itog_food_like += 1

            self.sum_ganib = len(self.bak_list) - itog_ganib
            self.sum_food_like = len(self.bak_list) - itog_food_like


    def on_key_press(self, key, modifiers):
        if key == arcade.key.TAB and self.ful_screen:
            self.set_fullscreen(not self.ful_screen)
            self.ful_screen = False
            

        elif key == arcade.key.TAB and not self.ful_screen:
            self.set_fullscreen(not self.ful_screen)
            self.ful_screen = True

sim = Simular()
arcade.run()
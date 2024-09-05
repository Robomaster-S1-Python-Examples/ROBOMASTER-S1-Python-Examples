
# Use these Robomaster S1 RGB looping templates in your next
# Robomaster S1 Python programs. There are 40 RGB effects to
# choose from. This Robomaster S1 RGB looping template will
# also teach you that RGB looping with the Robomaster S1 is
# just so much fun!! Note: the gimbal RGBs cannot be separate;
# the next colour you choose will override the RGB led you did.
# If you used pink or whatever colour you choose, all the RGBs
# will go to the colour you chose next. The RGBs can be turned
# on and off separately, but they cannot be colour changed
# separately.

# Robomaster S1 RGB Looping Templates class version examples:

# Created by Joseph C. Richardson, GitHub.com

# Use these tuple index values to shorten all rgb Python commands.

led_set_top_bottom=(
    led_ctrl.set_top_led,    #index[0]
    led_ctrl.set_bottom_led, #index[1]
    led_ctrl.set_single_led, #index[2]
    led_ctrl.set_flash(rm_define.armor_all,6)) #index[3]

gun_led_on_off=(
    led_ctrl.gun_led_off, #index[0]
    led_ctrl.gun_led_on)  #index[1]

define_armor_top_bottom_all=(
    rm_define.armor_top_all,    #index[0]
    rm_define.armor_bottom_all, #index[1]
    rm_define.armor_all)        #index[2]

define_armor_top_right_left=(
    rm_define.armor_top_right, #index[0]
    rm_define.armor_top_left)  #index[1]

define_armor_bottom_right_left=(
    rm_define.armor_bottom_right, #index[0]
    rm_define.armor_bottom_left)  #index[1]

define_armor_bottom_front_back=(
    rm_define.armor_bottom_front, #index[0]
    rm_define.armor_bottom_back)  #index[1]

define_effect=(
    rm_define.effect_always_off, #index[0]
    rm_define.effect_always_on,  #index[1]
    rm_define.effect_flash,      #index[2]
    rm_define.effect_breath,     #index[3]
    rm_define.effect_marquee)    #index[4]

led_ctrl.turn_off(rm_define.armor_all)

rgb1,rgb2=0,255 # dim and change all rgb colours by changing the values: '0' and '255'
delay=.000000001,.1,.5

RGB_COLOURS=[
    [],               # empty list box
    [rgb2,rgb2,rgb2], # RGB White
    [rgb2,rgb1,rgb1], # RGB Red
    [rgb2,rgb2,rgb1], # RGB Yellow
    [rgb1,rgb1,rgb2], # RGB Blue
    [rgb1,rgb2,rgb1], # RGB Green
    [rgb2,rgb1,rgb2], # RGB Pink
    [rgb1,rgb2,rgb2], # RGB Cyan
    ]

RGB_RY=[
    [],               # empty list box
    [rgb2,rgb1,rgb1], # RGB Red
    [rgb2,rgb2,rgb1], # RGB Yellow
    [rgb2,rgb1,rgb1], # RGB Red
    [rgb2,rgb2,rgb1], # RGB Yellow
    [rgb2,rgb1,rgb1], # RGB Red
    [rgb2,rgb2,rgb1], # RGB Yellow
    [rgb2,rgb1,rgb1], # RGB Red
    [rgb2,rgb2,rgb1], # RGB Yellow
    ]

RGB_YR=[
    [],               # empty list box
    [rgb2,rgb2,rgb1], # RGB Yellow
    [rgb2,rgb1,rgb1], # RGB Red
    [rgb2,rgb2,rgb1], # RGB Yellow
    [rgb2,rgb1,rgb1], # RGB Red
    [rgb2,rgb2,rgb1], # RGB Yellow
    [rgb2,rgb1,rgb1], # RGB Red
    [rgb2,rgb2,rgb1], # RGB Yellow
    [rgb2,rgb1,rgb1], # RGB Red
    ]

RGB_BG=[
    [],               # empty list box
    [rgb1,rgb1,rgb2], # RGB Blue
    [rgb1,rgb2,rgb1], # RGB Green
    [rgb1,rgb1,rgb2], # RGB Blue
    [rgb1,rgb2,rgb1], # RGB Green
    [rgb1,rgb1,rgb2], # RGB Blue
    [rgb1,rgb2,rgb1], # RGB Green
    [rgb1,rgb1,rgb2], # RGB Blue
    [rgb1,rgb2,rgb1], # RGB Green
    ]

RGB_GB=[
    [],               # empty list box
    [rgb1,rgb2,rgb1], # RGB Green
    [rgb1,rgb1,rgb2], # RGB Blue
    [rgb1,rgb2,rgb1], # RGB Green
    [rgb1,rgb1,rgb2], # RGB Blue
    [rgb1,rgb2,rgb1], # RGB Green
    [rgb1,rgb1,rgb2], # RGB Blue
    [rgb1,rgb2,rgb1], # RGB Green
    [rgb1,rgb1,rgb2], # RGB Blue
    ]

RGB_PC=[
    [],               # empty list box
    [rgb2,rgb1,rgb2], # RGB Pink
    [rgb1,rgb2,rgb2], # RGB Cyan
    [rgb2,rgb1,rgb2], # RGB Pink
    [rgb1,rgb2,rgb2], # RGB Cyan
    [rgb2,rgb1,rgb2], # RGB Pink
    [rgb1,rgb2,rgb2], # RGB Cyan
    [rgb2,rgb1,rgb2], # RGB Pink
    [rgb1,rgb2,rgb2], # RGB Cyan
    ]

RGB_CP=[
    [],               # empty list box
    [rgb1,rgb2,rgb2], # RGB Cyan
    [rgb2,rgb1,rgb2], # RGB Pink
    [rgb1,rgb2,rgb2], # RGB Cyan
    [rgb2,rgb1,rgb2], # RGB Pink
    [rgb1,rgb2,rgb2], # RGB Cyan
    [rgb2,rgb1,rgb2], # RGB Pink
    [rgb1,rgb2,rgb2], # RGB Cyan
    [rgb2,rgb1,rgb2], # RGB Pink
    ]

RGB_RYBG=[
    [],               # empty list box
    [rgb2,rgb1,rgb1], # RGB Red
    [rgb2,rgb2,rgb1], # RGB Yellow
    [rgb1,rgb1,rgb2], # RGB Blue
    [rgb1,rgb2,rgb1], # RGB Green
    [rgb2,rgb1,rgb1], # RGB Red
    [rgb2,rgb2,rgb1], # RGB Yellow
    [rgb1,rgb1,rgb2], # RGB Blue
    [rgb1,rgb2,rgb1], # RGB Green
    ]
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def start():

    def rgb_single_red_yellow_colour_spin_forward():

        while True:
            gun_led_on_off[1]()
            for i in range(8):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_RY[i+1][0],RGB_RY[i+1][1],RGB_RY[i+1][2],define_effect[0])
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i+1],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_RY[i+1][0],RGB_RY[i+1][1],RGB_RY[i+1][2],define_effect[1])
                time.sleep(delay[1])
                gun_led_on_off[0]()
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_single_blue_green_colour_spin_forward():

        while True:
            gun_led_on_off[1]()
            for i in range(8):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_BG[i+1][0],RGB_BG[i+1][1],RGB_BG[i+1][2],define_effect[0])
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i+1],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_BG[i+1][0],RGB_BG[i+1][1],RGB_BG[i+1][2],define_effect[1])
                time.sleep(delay[1])
                gun_led_on_off[0]()
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_single_pink_cyan_colour_spin_forward():

        while True:
            gun_led_on_off[1]()
            for i in range(8):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_PC[i+1][0],RGB_PC[i+1][1],RGB_PC[i+1][2],define_effect[0])
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i+1],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_PC[i+1][0],RGB_PC[i+1][1],RGB_PC[i+1][2],define_effect[1])
                time.sleep(delay[1])
                gun_led_on_off[0]()
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_single_red_yellow_colour_spin_reverse():

        while True:
            gun_led_on_off[1]()
            for i in range(8,0,-1):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_RY[i][0],RGB_RY[i][1],RGB_RY[i][2],define_effect[0])
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_RY[i][0],RGB_RY[i][1],RGB_RY[i][2],define_effect[1])
                time.sleep(delay[1])
                gun_led_on_off[0]()
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_single_blue_green_colour_spin_reverse():

        while True:
            gun_led_on_off[1]()
            for i in range(8,0,-1):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_BG[i][0],RGB_BG[i][1],RGB_BG[i][2],define_effect[0])
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_BG[i][0],RGB_BG[i][1],RGB_BG[i][2],define_effect[1])
                time.sleep(delay[1])
                gun_led_on_off[0]()
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_single_pink_cyan_colour_spin_reverse():

        while True:
            gun_led_on_off[1]()
            for i in range(8,0,-1):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_PC[i][0],RGB_PC[i][1],RGB_PC[i][2],define_effect[0])
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_PC[i][0],RGB_PC[i][1],RGB_PC[i][2],define_effect[1])
                time.sleep(delay[1])
                gun_led_on_off[0]()
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_double_red_yellow_colour_spin_forward():

        while True:
            gun_led_on_off[1]()
            for i in range(4):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_RY[i+1][0],RGB_RY[i+1][1],RGB_RY[i+1][2],define_effect[0])
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i+1,i+5],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_RY[i+1][0],RGB_RY[i+1][1],RGB_RY[i+1][2],define_effect[1])
                time.sleep(delay[1])
                gun_led_on_off[0]()
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_double_blue_green_colour_spin_forward():

        while True:
            gun_led_on_off[1]()
            for i in range(4):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_BG[i+1][0],RGB_BG[i+1][1],RGB_BG[i+1][2],define_effect[0])
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i+1,i+5],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_BG[i+1][0],RGB_BG[i+1][1],RGB_BG[i+1][2],define_effect[1])
                time.sleep(delay[1])
                gun_led_on_off[0]()
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_double_pink_cyan_colour_spin_forward():

        while True:
            gun_led_on_off[1]()
            for i in range(4):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_PC[i+1][0],RGB_PC[i+1][1],RGB_PC[i+1][2],define_effect[0])
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i+1,i+5],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_PC[i+1][0],RGB_PC[i+1][1],RGB_PC[i+1][2],define_effect[1])
                time.sleep(delay[1])
                gun_led_on_off[0]()
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_double_red_yellow_colour_spin_reverse():

        while True:
            gun_led_on_off[1]()
            for i in range(4,0,-1):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_RY[i][0],RGB_RY[i][1],RGB_RY[i][2],define_effect[0])
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i,i+4],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_RY[i][0],RGB_RY[i][1],RGB_RY[i][2],define_effect[1])
                time.sleep(delay[1])
                gun_led_on_off[0]()
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_double_blue_green_colour_spin_reverse():

        while True:
            gun_led_on_off[1]()
            for i in range(4,0,-1):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_BG[i][0],RGB_BG[i][1],RGB_BG[i][2],define_effect[0])
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i,i+4],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_BG[i][0],RGB_BG[i][1],RGB_BG[i][2],define_effect[1])
                time.sleep(delay[1])
                gun_led_on_off[0]()
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_double_pink_cyan_colour_spin_reverse():

        while True:
            gun_led_on_off[1]()
            for i in range(4,0,-1):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_PC[i][0],RGB_PC[i][1],RGB_PC[i][2],define_effect[0])
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i,i+4],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_PC[i][0],RGB_PC[i][1],RGB_PC[i][2],define_effect[1])
                time.sleep(delay[1])
                gun_led_on_off[0]()
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_quad_red_yellow_colour_rotate_forward_reverse():

        led_set_top_bottom[3]
        while True:
            for i in range(1,3):
                gun_led_on_off[1]()
                led_set_top_bottom[1](define_armor_top_bottom_all[1],rgb2,rgb1,rgb1,define_effect[3])
                led_set_top_bottom[0](define_armor_top_bottom_all[0],rgb2,rgb1,rgb1,define_effect[0])
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i,i+2,i+4,i+6],define_effect[1])
                time.sleep(delay[1])

            for i in range(2,0,-1):
                gun_led_on_off[0]()
                led_set_top_bottom[1](define_armor_top_bottom_all[1],rgb2,rgb2,rgb1,define_effect[3])
                led_set_top_bottom[0](define_armor_top_bottom_all[0],rgb2,rgb2,rgb1,define_effect[0])
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i,i+2,i+4,i+6],define_effect[1])
                time.sleep(delay[1])
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_quad_blue_green_colour_rotate_forward_reverse():

        led_set_top_bottom[3]
        while True:
            gun_led_on_off[1]()
            for i in range(1,3):
                led_set_top_bottom[1](define_armor_top_bottom_all[1],rgb1,rgb1,rgb2,define_effect[3])
                led_set_top_bottom[0](define_armor_top_bottom_all[0],rgb1,rgb1,rgb2,define_effect[0])
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i,i+2,i+4,i+6],define_effect[1])
                time.sleep(delay[1])

            gun_led_on_off[0]()
            for i in range(2,0,-1):
                led_set_top_bottom[1](define_armor_top_bottom_all[1],rgb1,rgb2,rgb1,define_effect[3])
                led_set_top_bottom[0](define_armor_top_bottom_all[0],rgb1,rgb2,rgb1,define_effect[0])
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i,i+2,i+4,i+6],define_effect[1])
                time.sleep(delay[1])
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_quad_pink_cyan_colour_rotate_forward_reverse():

        led_set_top_bottom[3]
        while True:
            gun_led_on_off[1]()
            for i in range(1,3):
                led_set_top_bottom[1](define_armor_top_bottom_all[1],rgb2,rgb1,rgb2,define_effect[3])
                led_set_top_bottom[0](define_armor_top_bottom_all[0],rgb2,rgb1,rgb2,define_effect[0])
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i,i+2,i+4,i+6],define_effect[1])
                time.sleep(delay[1])

            gun_led_on_off[0]()
            for i in range(2,0,-1):
                led_set_top_bottom[1](define_armor_top_bottom_all[1],rgb1,rgb2,rgb2,define_effect[3])
                led_set_top_bottom[0](define_armor_top_bottom_all[0],rgb1,rgb2,rgb2,define_effect[0])
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i,i+2,i+4,i+6],define_effect[1])
                time.sleep(delay[1])
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_flash_colour_changers_forward_reverse():

        while True:
            for i in range(1,8):
                gun_led_on_off[1]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_COLOURS[i][0],RGB_COLOURS[i][1],RGB_COLOURS[i][2],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_COLOURS[i][0],RGB_COLOURS[i][1],RGB_COLOURS[i][2],define_effect[1])
                time.sleep(delay[1])

            for i in range(6,1,-1):
                gun_led_on_off[0]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_COLOURS[i][0],RGB_COLOURS[i][1],RGB_COLOURS[i][2],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_COLOURS[i][0],RGB_COLOURS[i][1],RGB_COLOURS[i][2],define_effect[1])
                time.sleep(delay[1])
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_flash_flip_red_yellow_colour_changer():

        while True:
            gun_led_on_off[1]()
            led_set_top_bottom[0](define_armor_top_right_left[0],rgb2,rgb1,rgb1,define_effect[1])
            led_set_top_bottom[0](define_armor_top_right_left[1],rgb2,rgb2,rgb1,define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_front_back[0],rgb2,rgb2,rgb1,define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_right_left[0],rgb2,rgb2,rgb1,define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_front_back[1],rgb2,rgb1,rgb1,define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_right_left[1],rgb2,rgb1,rgb1,define_effect[1])
            time.sleep(delay[1])
            gun_led_on_off[0]()

            led_set_top_bottom[0](define_armor_top_right_left[0],rgb2,rgb2,rgb1,define_effect[1])
            led_set_top_bottom[0](define_armor_top_right_left[1],rgb2,rgb1,rgb1,define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_front_back[0],rgb2,rgb1,rgb1,define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_right_left[0],rgb2,rgb1,rgb1,define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_front_back[1],rgb2,rgb2,rgb1,define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_right_left[1],rgb2,rgb2,rgb1,define_effect[1])
            time.sleep(delay[1])
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_flash_flip_blue_green_colour_changer():

        while True:
            gun_led_on_off[1]()
            led_set_top_bottom[0](define_armor_top_right_left[0],rgb1,rgb1,rgb2,define_effect[1])
            led_set_top_bottom[0](define_armor_top_right_left[1],rgb1,rgb2,rgb1,define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_front_back[0],rgb1,rgb2,rgb1,define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_right_left[0],rgb1,rgb2,rgb1,define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_front_back[1],rgb1,rgb1,rgb2,define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_right_left[1],rgb1,rgb1,rgb2,define_effect[1])
            time.sleep(delay[1])
            gun_led_on_off[0]()

            led_set_top_bottom[0](define_armor_top_right_left[0],rgb1,rgb2,rgb1,define_effect[1])
            led_set_top_bottom[0](define_armor_top_right_left[1],rgb1,rgb1,rgb2,define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_front_back[0],rgb1,rgb1,rgb2,define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_right_left[0],rgb1,rgb1,rgb2,define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_front_back[1],rgb1,rgb2,rgb1,define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_right_left[1],rgb1,rgb2,rgb1,define_effect[1])
            time.sleep(delay[1])
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_flash_flip_pink_cyan_colour_changer():

        while True:
            gun_led_on_off[1]()
            led_set_top_bottom[0](define_armor_top_right_left[0],rgb2,rgb1,rgb2,define_effect[1])
            led_set_top_bottom[0](define_armor_top_right_left[1],rgb1,rgb2,rgb2,define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_front_back[0],rgb1,rgb2,rgb2,define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_right_left[0],rgb1,rgb2,rgb2,define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_front_back[1],rgb2,rgb1,rgb2,define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_right_left[1],rgb2,rgb1,rgb2,define_effect[1])
            time.sleep(delay[1])
            gun_led_on_off[0]()

            led_set_top_bottom[0](define_armor_top_right_left[0],rgb1,rgb2,rgb2,define_effect[1])
            led_set_top_bottom[0](define_armor_top_right_left[1],rgb2,rgb1,rgb2,define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_front_back[0],rgb2,rgb1,rgb2,define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_right_left[0],rgb2,rgb1,rgb2,define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_front_back[1],rgb1,rgb2,rgb2,define_effect[1])
            led_set_top_bottom[1](define_armor_bottom_right_left[1],rgb1,rgb2,rgb2,define_effect[1])
            time.sleep(delay[1])
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_red_yellow_colour_flipper():

        while True:
            gun_led_on_off[1]()
            led_set_top_bottom[0](define_armor_top_bottom_all[0],
            RGB_RY[1][0],RGB_RY[1][1],RGB_RY[1][2],define_effect[0])
            led_set_top_bottom[2](define_armor_top_bottom_all[0],[1,2,3,4],define_effect[1])
            led_set_top_bottom[1](define_armor_top_bottom_all[1],
            RGB_RY[1][0],RGB_RY[1][1],RGB_RY[1][2],define_effect[1])
            time.sleep(delay[2])

            gun_led_on_off[0]()
            led_set_top_bottom[0](define_armor_top_bottom_all[0],
            RGB_YR[1][0],RGB_YR[1][1],RGB_YR[1][2],define_effect[0])
            led_set_top_bottom[2](define_armor_top_bottom_all[0],[5,6,7,8],define_effect[1])
            led_set_top_bottom[1](define_armor_top_bottom_all[1],
            RGB_YR[1][0],RGB_YR[1][1],RGB_YR[1][2],define_effect[1])
            time.sleep(delay[2])
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_blue_green_colour_flipper():

        while True:
            gun_led_on_off[1]()
            led_set_top_bottom[0](define_armor_top_bottom_all[0],
            RGB_BG[1][0],RGB_BG[1][1],RGB_BG[1][2],define_effect[0])
            led_set_top_bottom[2](define_armor_top_bottom_all[0],[1,2,3,4],define_effect[1])
            led_set_top_bottom[1](define_armor_top_bottom_all[1],
            RGB_BG[1][0],RGB_BG[1][1],RGB_BG[1][2],define_effect[1])
            time.sleep(delay[2])

            gun_led_on_off[0]()
            led_set_top_bottom[0](define_armor_top_bottom_all[0],
            RGB_GB[1][0],RGB_GB[1][1],RGB_GB[1][2],define_effect[0])
            led_set_top_bottom[2](define_armor_top_bottom_all[0],[5,6,7,8],define_effect[1])
            led_set_top_bottom[1](define_armor_top_bottom_all[1],
            RGB_GB[1][0],RGB_GB[1][1],RGB_GB[1][2],define_effect[1])
            time.sleep(delay[2])
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_pink_cyan_colour_flipper():

        while True:
            gun_led_on_off[1]()
            led_set_top_bottom[0](define_armor_top_bottom_all[0],
            RGB_PC[1][0],RGB_PC[1][1],RGB_PC[1][2],define_effect[0])
            led_set_top_bottom[2](define_armor_top_bottom_all[0],[1,2,3,4],define_effect[1])
            led_set_top_bottom[1](define_armor_top_bottom_all[1],
            RGB_PC[1][0],RGB_PC[1][1],RGB_PC[1][2],define_effect[1])
            time.sleep(delay[2])

            gun_led_on_off[0]()
            led_set_top_bottom[0](define_armor_top_bottom_all[0],
            RGB_CP[1][0],RGB_CP[1][1],RGB_CP[1][2],define_effect[0])
            led_set_top_bottom[2](define_armor_top_bottom_all[0],[5,6,7,8],define_effect[1])
            led_set_top_bottom[1](define_armor_top_bottom_all[1],
            RGB_CP[1][0],RGB_CP[1][1],RGB_CP[1][2],define_effect[1])
            time.sleep(delay[2])
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_colour_trail_blazer_forward():

        while True:
            for i in range(1,8):
                gun_led_on_off[1]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],RGB_COLOURS[i][0],
                RGB_COLOURS[i][1],RGB_COLOURS[i][2],define_effect[0])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],RGB_COLOURS[i][0],
                RGB_COLOURS[i][1],RGB_COLOURS[i][2],define_effect[2])

                for j in range(1,9):
                    led_set_top_bottom[2](define_armor_top_bottom_all[0],[j],define_effect[1])
                    time.sleep(delay[1])

                for j in range(1,9):
                    gun_led_on_off[0]()
                    led_set_top_bottom[2](define_armor_top_bottom_all[0],[j],define_effect[0])
                    time.sleep(delay[1])
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_colour_trail_blazer_reverse():

        while True:
            for i in range(1,8):
                gun_led_on_off[1]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],RGB_COLOURS[i][0],
                RGB_COLOURS[i][1],RGB_COLOURS[i][2],define_effect[0])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],RGB_COLOURS[i][0],
                RGB_COLOURS[i][1],RGB_COLOURS[i][2],define_effect[2])

                for j in range(8,0,-1):
                    led_set_top_bottom[2](define_armor_top_bottom_all[0],[j],define_effect[1])
                    time.sleep(delay[1])

                for j in range(8,0,-1):
                    gun_led_on_off[0]()
                    led_set_top_bottom[2](define_armor_top_bottom_all[0],[j],define_effect[0])
                    time.sleep(delay[1])
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_smooth_shift_colour_change_contrast():

        while True:
            for i in range(255,0,-2):
                gun_led_on_off[1]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],rgb2,i,i,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],rgb2,rgb2,i,define_effect[1])
                time.sleep(delay[0])
            time.sleep(delay[2])

            for i in range(255):
                gun_led_on_off[0]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],rgb2,i,i,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],rgb2,rgb2,i,define_effect[1])
                time.sleep(delay[0])

            for i in range(255,0,-2):
                gun_led_on_off[1]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],i,i,rgb2,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],i,rgb2,i,define_effect[1])
                time.sleep(delay[0])
            time.sleep(delay[2])

            for i in range(255):
                gun_led_on_off[0]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],i,i,rgb2,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],i,rgb2,i,define_effect[1])
                time.sleep(delay[0])

            for i in range(255,0,-2):
                gun_led_on_off[1]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],rgb2,i,rgb2,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],i,rgb2,rgb2,define_effect[1])
                time.sleep(delay[0])
            time.sleep(delay[2])

            for i in range(255):
                gun_led_on_off[0]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],rgb2,i,rgb2,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],i,rgb2,rgb2,define_effect[1])
                time.sleep(delay[0])
            time.sleep(delay[2])
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_white_colour_dimmer():

        while True:
            for i in range(0,rgb2):
                gun_led_on_off[1]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],i,i,i,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],i,i,i,define_effect[1])

            for i in range(rgb2,-1,-2):
                gun_led_on_off[0]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],i,i,i,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],i,i,i,define_effect[1])
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_red_colour_dimmer():

        while True:
            for i in range(0,rgb2):
                gun_led_on_off[1]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],i,rgb1,rgb1,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],i,rgb1,rgb1,define_effect[1])

            for i in range(rgb2,-1,-2):
                gun_led_on_off[0]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],i,rgb1,rgb1,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],i,rgb1,rgb1,define_effect[1])
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_yellow_colour_dimmer():

        while True:
            for i in range(0,rgb2):
                gun_led_on_off[1]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],i,i,rgb1,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],i,i,rgb1,define_effect[1])

            for i in range(rgb2,-1,-2):
                gun_led_on_off[0]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],i,i,rgb1,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],i,i,rgb1,define_effect[1])
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_blue_colour_dimmer():

        while True:
            for i in range(0,rgb2):
                gun_led_on_off[1]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],rgb1,rgb1,i,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],rgb1,rgb1,i,define_effect[1])

            for i in range(rgb2,-1,-2):
                gun_led_on_off[0]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],rgb1,rgb1,i,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],rgb1,rgb1,i,define_effect[1])
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_green_colour_dimmer():

        while True:
            for i in range(0,rgb2):
                gun_led_on_off[1]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],rgb1,i,rgb1,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],rgb1,i,rgb1,define_effect[1])

            for i in range(rgb2,-1,-2):
                gun_led_on_off[0]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],rgb1,i,rgb1,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],rgb1,i,rgb1,define_effect[1])
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_pink_colour_dimmer():

        while True:
            for i in range(0,rgb2):
                gun_led_on_off[1]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],i,rgb1,i,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],i,rgb1,i,define_effect[1])

            for i in range(rgb2,-1,-2):
                gun_led_on_off[0]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],i,rgb1,i,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],i,rgb1,i,define_effect[1])
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_cyan_colour_dimmer():

        while True:
            for i in range(0,rgb2):
                gun_led_on_off[1]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],rgb1,i,i,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],rgb1,i,i,define_effect[1])

            for i in range(rgb2,-1,-2):
                gun_led_on_off[0]()
                led_set_top_bottom[0](define_armor_top_bottom_all[0],rgb1,i,i,define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],rgb1,i,i,define_effect[1])
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_single_red_yellow_colour_spin_forward_reverse_random():

        while True:
            randcount=random.randint(0,4)
            for i in range(randcount):
                gun_led_on_off[1]()
                for j in range(8):
                    led_set_top_bottom[0](define_armor_top_bottom_all[0],
                    RGB_RY[j+1][0],RGB_RY[j+1][1],RGB_RY[j+1][2],define_effect[0])
                    led_set_top_bottom[2](define_armor_top_bottom_all[0],[j+1],define_effect[1])
                    led_set_top_bottom[1](define_armor_top_bottom_all[1],
                    RGB_RY[j+1][0],RGB_RY[j+1][1],RGB_RY[j+1][2],define_effect[1])
                    time.sleep(delay[1])
                    gun_led_on_off[0]()

            for i in range(randcount):
                gun_led_on_off[1]()
                for j in range(8,0,-1):
                    led_set_top_bottom[0](define_armor_top_bottom_all[0],
                    RGB_RY[j][0],RGB_RY[j][1],RGB_RY[j][2],define_effect[0])
                    led_set_top_bottom[2](define_armor_top_bottom_all[0],[j],define_effect[1])
                    led_set_top_bottom[1](define_armor_top_bottom_all[1],
                    RGB_RY[j][0],RGB_RY[j][1],RGB_RY[j][2],define_effect[1])
                    time.sleep(delay[1])
                    gun_led_on_off[0]()
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_single_blue_green_colour_spin_forward_reverse_random():

        while True:
            randcount=random.randint(0,4)
            for i in range(randcount):
                gun_led_on_off[1]()
                for j in range(8):
                    led_set_top_bottom[0](define_armor_top_bottom_all[0],
                    RGB_BG[j+1][0],RGB_BG[j+1][1],RGB_BG[j+1][2],define_effect[0])
                    led_set_top_bottom[2](define_armor_top_bottom_all[0],[j+1],define_effect[1])
                    led_set_top_bottom[1](define_armor_top_bottom_all[1],
                    RGB_BG[j+1][0],RGB_BG[j+1][1],RGB_BG[j+1][2],define_effect[1])
                    time.sleep(delay[1])
                    gun_led_on_off[0]()

            for i in range(randcount):
                gun_led_on_off[1]()
                for j in range(8,0,-1):
                    led_set_top_bottom[0](define_armor_top_bottom_all[0],
                    RGB_BG[j][0],RGB_BG[j][1],RGB_BG[j][2],define_effect[0])
                    led_set_top_bottom[2](define_armor_top_bottom_all[0],[j],define_effect[1])
                    led_set_top_bottom[1](define_armor_top_bottom_all[1],
                    RGB_BG[j][0],RGB_BG[j][1],RGB_BG[j][2],define_effect[1])
                    time.sleep(delay[1])
                    gun_led_on_off[0]()
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_single_pink_cyan_colour_spin_forward_reverse_random():

        while True:
            randcount=random.randint(0,4)
            for i in range(randcount):
                gun_led_on_off[1]()
                for j in range(8):
                    led_set_top_bottom[0](define_armor_top_bottom_all[0],
                    RGB_PC[j+1][0],RGB_PC[j+1][1],RGB_PC[j+1][2],define_effect[0])
                    led_set_top_bottom[2](define_armor_top_bottom_all[0],[j+1],define_effect[1])
                    led_set_top_bottom[1](define_armor_top_bottom_all[1],
                    RGB_PC[j+1][0],RGB_PC[j+1][1],RGB_PC[j+1][2],define_effect[1])
                    time.sleep(delay[1])
                    gun_led_on_off[0]()

            for i in range(randcount):
                gun_led_on_off[1]()
                for j in range(8,0,-1):
                    led_set_top_bottom[0](define_armor_top_bottom_all[0],
                    RGB_PC[j][0],RGB_PC[j][1],RGB_PC[j][2],define_effect[0])
                    led_set_top_bottom[2](define_armor_top_bottom_all[0],[j],define_effect[1])
                    led_set_top_bottom[1](define_armor_top_bottom_all[1],
                    RGB_PC[j][0],RGB_PC[j][1],RGB_PC[j][2],define_effect[1])
                    time.sleep(delay[1])
                    gun_led_on_off[0]()
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_double_red_yellow_colour_spin_forward_reverse_random():

        while True:
            randcount=random.randint(0,8)
            for i in range(randcount):
                gun_led_on_off[1]()
                for j in range(4):
                    led_set_top_bottom[0](define_armor_top_bottom_all[0],
                    RGB_RY[j+1][0],RGB_RY[j+1][1],RGB_RY[j+1][2],define_effect[0])
                    led_set_top_bottom[2](define_armor_top_bottom_all[0],[j+1,j+5],define_effect[1])
                    led_set_top_bottom[1](define_armor_top_bottom_all[1],
                    RGB_RY[j+1][0],RGB_RY[j+1][1],RGB_RY[j+1][2],define_effect[1])
                    time.sleep(delay[1])
                    gun_led_on_off[0]()

            for i in range(randcount):
                gun_led_on_off[1]()
                for j in range(4,0,-1):
                    led_set_top_bottom[0](define_armor_top_bottom_all[0],
                    RGB_RY[j][0],RGB_RY[j][1],RGB_RY[j][2],define_effect[0])
                    led_set_top_bottom[2](define_armor_top_bottom_all[0],[j,j+4],define_effect[1])
                    led_set_top_bottom[1](define_armor_top_bottom_all[1],
                    RGB_RY[j][0],RGB_RY[j][1],RGB_RY[j][2],define_effect[1])
                    time.sleep(delay[1])
                    gun_led_on_off[0]()
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_double_blue_green_colour_spin_forward_reverse_random():

        while True:
            randcount=random.randint(0,8)
            for i in range(randcount):
                gun_led_on_off[1]()
                for j in range(4):
                    led_set_top_bottom[0](define_armor_top_bottom_all[0],
                    RGB_BG[j+1][0],RGB_BG[j+1][1],RGB_BG[j+1][2],define_effect[0])
                    led_set_top_bottom[2](define_armor_top_bottom_all[0],[j+1,j+5],define_effect[1])
                    led_set_top_bottom[1](define_armor_top_bottom_all[1],
                    RGB_BG[j+1][0],RGB_BG[j+1][1],RGB_BG[j+1][2],define_effect[1])
                    time.sleep(delay[1])
                    gun_led_on_off[0]()

            for i in range(randcount):
                gun_led_on_off[1]()
                for j in range(4,0,-1):
                    led_set_top_bottom[0](define_armor_top_bottom_all[0],
                    RGB_BG[j][0],RGB_BG[j][1],RGB_BG[j][2],define_effect[0])
                    led_set_top_bottom[2](define_armor_top_bottom_all[0],[j,j+4],define_effect[1])
                    led_set_top_bottom[1](define_armor_top_bottom_all[1],
                    RGB_BG[j][0],RGB_BG[j][1],RGB_BG[j][2],define_effect[1])
                    time.sleep(delay[1])
                    gun_led_on_off[0]()
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_double_pink_cyan_colour_spin_forward_reverse_random():

        while True:
            randcount=random.randint(0,8)
            for i in range(randcount):
                gun_led_on_off[1]()
                for j in range(4):
                    led_set_top_bottom[0](define_armor_top_bottom_all[0],
                    RGB_PC[j+1][0],RGB_PC[j+1][1],RGB_PC[j+1][2],define_effect[0])
                    led_set_top_bottom[2](define_armor_top_bottom_all[0],[j+1,j+5],define_effect[1])
                    led_set_top_bottom[1](define_armor_top_bottom_all[1],
                    RGB_PC[j+1][0],RGB_PC[j+1][1],RGB_PC[j+1][2],define_effect[1])
                    time.sleep(delay[1]);
                    gun_led_on_off[0]()

            for i in range(randcount):
                gun_led_on_off[1]()
                for j in range(4,0,-1):
                    led_set_top_bottom[0](define_armor_top_bottom_all[0],
                    RGB_PC[j][0],RGB_PC[j][1],RGB_PC[j][2],define_effect[0])
                    led_set_top_bottom[2](define_armor_top_bottom_all[0],[j,j+4],define_effect[1])
                    led_set_top_bottom[1](define_armor_top_bottom_all[1],
                    RGB_PC[j][0],RGB_PC[j][1],RGB_PC[j][2],define_effect[1])
                    time.sleep(delay[1])
                    gun_led_on_off[0]()
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_colour_trail_blazer_red_yellow_forward_reverse_random():

        led_set_top_bottom[3]
        while True:
            randcount=random.randint(1,9)
            led_set_top_bottom[1](define_armor_top_bottom_all[1],rgb2,rgb1,rgb1,define_effect[2])
            led_set_top_bottom[0](define_armor_top_bottom_all[0],rgb2,rgb1,rgb1,define_effect[0])
            for i in range(1,randcount):
                gun_led_on_off[1]()
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i],define_effect[1])
                time.sleep(delay[1])

            for i in range(1,randcount):
                gun_led_on_off[0]()
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i],define_effect[0])
                time.sleep(delay[1])

            led_set_top_bottom[1](define_armor_top_bottom_all[1],rgb2,rgb2,rgb1,define_effect[2])
            led_set_top_bottom[0](define_armor_top_bottom_all[0],rgb2,rgb2,rgb1,define_effect[0])
            for i in range(randcount-1,0,-1):
                gun_led_on_off[1]()
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i],define_effect[1])
                time.sleep(delay[1])

            for i in range(randcount-1,0,-1):
                gun_led_on_off[0]()
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i],define_effect[0])
                time.sleep(delay[1])
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_colour_trail_blazer_blue_green_forward_reverse_random():

        led_set_top_bottom[3]
        while True:
            randcount=random.randint(1,9)
            led_set_top_bottom[1](define_armor_top_bottom_all[1],rgb1,rgb1,rgb2,define_effect[2])
            led_set_top_bottom[0](define_armor_top_bottom_all[0],rgb1,rgb1,rgb2,define_effect[0])
            for i in range(1,randcount):
                gun_led_on_off[1]()
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i],define_effect[1])
                time.sleep(delay[1])

            for i in range(1,randcount):
                gun_led_on_off[0]()
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i],define_effect[0])
                time.sleep(delay[1])

            led_set_top_bottom[1](define_armor_top_bottom_all[1],rgb1,rgb2,rgb1,define_effect[2])
            led_set_top_bottom[0](define_armor_top_bottom_all[0],rgb1,rgb2,rgb1,define_effect[0])
            for i in range(randcount-1,0,-1):
                gun_led_on_off[1]()
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i],define_effect[1])
                time.sleep(delay[1])

            for i in range(randcount-1,0,-1):
                gun_led_on_off[0]()
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i],define_effect[0])
                time.sleep(delay[1])
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_colour_trail_blazer_pink_cyan_forward_reverse_random():

        led_set_top_bottom[3]
        while True:
            randcount=random.randint(1,9)
            led_set_top_bottom[1](define_armor_top_bottom_all[1],rgb2,rgb1,rgb2,define_effect[2])
            led_set_top_bottom[0](define_armor_top_bottom_all[0],rgb2,rgb1,rgb2,define_effect[0])
            for i in range(1,randcount):
                gun_led_on_off[1]()
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i],define_effect[1])
                time.sleep(delay[1])

            for i in range(1,randcount):
                gun_led_on_off[0]()
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i],define_effect[0])
                time.sleep(delay[1])

            led_set_top_bottom[1](define_armor_top_bottom_all[1],rgb1,rgb2,rgb2,define_effect[2])
            led_set_top_bottom[0](define_armor_top_bottom_all[0],rgb1,rgb2,rgb2,define_effect[0])
            for i in range(randcount-1,0,-1):
                gun_led_on_off[1]()
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i],define_effect[1])
                time.sleep(delay[1])

            for i in range(randcount-1,0,-1):
                gun_led_on_off[0]()
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i],define_effect[0])
                time.sleep(delay[1])
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    class RGB_single_colour_spin_forward:
    
        def __init__(self,
        rgb_single_red_yellow_colour_spin_forward,
        rgb_single_blue_green_colour_spin_forward,
        rgb_single_pink_cyan_colour_spin_forward):
            
            self.rgb1=rgb_single_red_yellow_colour_spin_forward
            self.rgb2=rgb_single_blue_green_colour_spin_forward
            self.rgb3=rgb_single_pink_cyan_colour_spin_forward

    a=RGB_single_colour_spin_forward(
    rgb_single_red_yellow_colour_spin_forward,
    rgb_single_blue_green_colour_spin_forward,
    rgb_single_pink_cyan_colour_spin_forward)
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    class RGB_single_colour_spin_reverse:
    
        def __init__(self,
        rgb_single_red_yellow_colour_spin_reverse,
        rgb_single_blue_green_colour_spin_reverse,
        rgb_single_pink_cyan_colour_spin_reverse):
            
            self.rgb1=rgb_single_red_yellow_colour_spin_reverse
            self.rgb2=rgb_single_blue_green_colour_spin_reverse
            self.rgb3=rgb_single_pink_cyan_colour_spin_reverse

    b=RGB_single_colour_spin_reverse(
    rgb_single_red_yellow_colour_spin_reverse,
    rgb_single_blue_green_colour_spin_reverse,
    rgb_single_pink_cyan_colour_spin_reverse)
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    class RGB_double_colour_spin_forward:
    
        def __init__(self,
        rgb_double_red_yellow_colour_spin_forward,
        rgb_double_blue_green_colour_spin_forward,
        rgb_double_pink_cyan_colour_spin_forward):
            
            self.rgb1=rgb_double_red_yellow_colour_spin_forward
            self.rgb2=rgb_double_blue_green_colour_spin_forward
            self.rgb3=rgb_double_pink_cyan_colour_spin_forward

    c=RGB_double_colour_spin_forward(
    rgb_double_red_yellow_colour_spin_forward,
    rgb_double_blue_green_colour_spin_forward,
    rgb_double_pink_cyan_colour_spin_forward)
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    class RGB_double_colour_spin_reverse:
    
        def __init__(self,
        rgb_double_red_yellow_colour_spin_reverse,
        rgb_double_blue_green_colour_spin_reverse,
        rgb_double_pink_cyan_colour_spin_reverse):
            
            self.rgb1=rgb_double_red_yellow_colour_spin_reverse
            self.rgb2=rgb_double_blue_green_colour_spin_reverse
            self.rgb3=rgb_double_pink_cyan_colour_spin_reverse

    d=RGB_double_colour_spin_forward(
    rgb_double_red_yellow_colour_spin_reverse,
    rgb_double_blue_green_colour_spin_reverse,
    rgb_double_pink_cyan_colour_spin_reverse)
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    class RGB_quad_colour_rotate_forward_reverse:

        def __init__(self,
        rgb_quad_red_yellow_colour_rotate_forward_reverse,
        rgb_quad_blue_green_colour_rotate_forward_reverse,
        rgb_quad_pink_cyan_colour_rotate_forward_reverse):

            self.rgb1=rgb_quad_red_yellow_colour_rotate_forward_reverse
            self.rgb2=rgb_quad_blue_green_colour_rotate_forward_reverse
            self.rgb3=rgb_quad_pink_cyan_colour_rotate_forward_reverse

    e=RGB_quad_colour_rotate_forward_reverse(
    rgb_quad_red_yellow_colour_rotate_forward_reverse,
    rgb_quad_blue_green_colour_rotate_forward_reverse,
    rgb_quad_pink_cyan_colour_rotate_forward_reverse)
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    class RGB_flash_colour_changers_and_smooth_shift_colour_change_contrast:
        def __init__(self,
        rgb_flash_colour_changers_forward_reverse,
        rgb_smooth_shift_colour_change_contrast):

            self.rgb1=rgb_flash_colour_changers_forward_reverse
            self.rgb2=rgb_smooth_shift_colour_change_contrast

    f=RGB_flash_colour_changers_and_smooth_shift_colour_change_contrast(
    rgb_flash_colour_changers_forward_reverse,
    rgb_smooth_shift_colour_change_contrast)
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    class RGB_flash_flip_colour_changer:

        def __init__(self,
        rgb_flash_flip_red_yellow_colour_changer,
        rgb_flash_flip_blue_green_colour_changer,
        rgb_flash_flip_pink_cyan_colour_changer):

            self.rgb1=rgb_flash_flip_red_yellow_colour_changer
            self.rgb2=rgb_flash_flip_blue_green_colour_changer
            self.rgb3=rgb_flash_flip_pink_cyan_colour_changer

    g=RGB_flash_flip_colour_changer(
    rgb_flash_flip_red_yellow_colour_changer,
    rgb_flash_flip_blue_green_colour_changer,
    rgb_flash_flip_pink_cyan_colour_changer)
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    class RGB_colour_flipper:

        def __init__(self,
        rgb_red_yellow_colour_flipper,
        rgb_blue_green_colour_flipper,
        rgb_pink_cyan_colour_flipper):

            self.rgb1=rgb_red_yellow_colour_flipper
            self.rgb2=rgb_blue_green_colour_flipper
            self.rgb3=rgb_pink_cyan_colour_flipper

    h=RGB_colour_flipper(
    rgb_red_yellow_colour_flipper,
    rgb_blue_green_colour_flipper,
    rgb_pink_cyan_colour_flipper)
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    class RGB_colour_trail_blazer_forward_reverse:

        def __init__(self,
        rgb_colour_trail_blazer_forward,
        rgb_colour_trail_blazer_reverse):

            self.rgb1=rgb_colour_trail_blazer_forward
            self.rgb2=rgb_colour_trail_blazer_reverse

    i=RGB_colour_trail_blazer_forward_reverse(
    rgb_colour_trail_blazer_forward,
    rgb_colour_trail_blazer_reverse)
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    class RGB_colour_dimmer:

        def __init__(self,
        rgb_white_colour_dimmer,
        rgb_red_colour_dimmer,
        rgb_yellow_colour_dimmer,
        rgb_blue_colour_dimmer,
        rgb_green_colour_dimmer,
        rgb_pink_colour_dimmer,
        rgb_cyan_colour_dimmer):

            self.rgb1=rgb_white_colour_dimmer
            self.rgb2=rgb_red_colour_dimmer
            self.rgb3=rgb_yellow_colour_dimmer
            self.rgb4=rgb_blue_colour_dimmer
            self.rgb5=rgb_green_colour_dimmer
            self.rgb6=rgb_pink_colour_dimmer
            self.rgb7=rgb_cyan_colour_dimmer

    j=RGB_colour_dimmer(
    rgb_white_colour_dimmer,
    rgb_red_colour_dimmer,
    rgb_yellow_colour_dimmer,
    rgb_blue_colour_dimmer,
    rgb_green_colour_dimmer,
    rgb_pink_colour_dimmer,
    rgb_cyan_colour_dimmer)
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    class RGB_single_colour_spin_forward_reverse_random:

        def __init__(self,
        rgb_single_red_yellow_colour_spin_forward_reverse_random,
        rgb_single_blue_green_colour_spin_forward_reverse_random,
        rgb_single_pink_cyan_colour_spin_forward_reverse_random):

            self.rgb1=rgb_single_red_yellow_colour_spin_forward_reverse_random
            self.rgb2=rgb_single_blue_green_colour_spin_forward_reverse_random
            self.rgb3=rgb_single_pink_cyan_colour_spin_forward_reverse_random

    k=RGB_single_colour_spin_forward_reverse_random(
    rgb_single_red_yellow_colour_spin_forward_reverse_random,
    rgb_single_blue_green_colour_spin_forward_reverse_random,
    rgb_single_pink_cyan_colour_spin_forward_reverse_random)
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    class RGB_double_colour_spin_forward_reverse_random:

        def __init__(self,
        rgb_double_red_yellow_colour_spin_forward_reverse_random,
        rgb_double_blue_green_colour_spin_forward_reverse_random,
        rgb_double_pink_cyan_colour_spin_forward_reverse_random):

            self.rgb1=rgb_double_red_yellow_colour_spin_forward_reverse_random
            self.rgb2=rgb_double_blue_green_colour_spin_forward_reverse_random
            self.rgb3=rgb_double_pink_cyan_colour_spin_forward_reverse_random

    l=RGB_double_colour_spin_forward_reverse_random(
    rgb_double_red_yellow_colour_spin_forward_reverse_random,
    rgb_double_blue_green_colour_spin_forward_reverse_random,
    rgb_double_pink_cyan_colour_spin_forward_reverse_random)
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    class RGB_colour_trail_blazer_forward_reverse_random:

        def __init__(self,
        rgb_colour_trail_blazer_red_yellow_forward_reverse_random,
        rgb_colour_trail_blazer_blue_green_forward_reverse_random,
        rgb_colour_trail_blazer_pink_cyan_forward_reverse_random):

            self.rgb1=rgb_colour_trail_blazer_red_yellow_forward_reverse_random
            self.rgb2=rgb_colour_trail_blazer_blue_green_forward_reverse_random
            self.rgb3=rgb_colour_trail_blazer_pink_cyan_forward_reverse_random

    m=RGB_colour_trail_blazer_forward_reverse_random(
    rgb_colour_trail_blazer_red_yellow_forward_reverse_random,
    rgb_colour_trail_blazer_blue_green_forward_reverse_random,
    rgb_colour_trail_blazer_pink_cyan_forward_reverse_random)
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    # each class creates different RGB looping effects
    
    RGB_single_colour_spin_forward=a.rgb1,a.rgb2,a.rgb3
    RGB_single_colour_spin_reverse=b.rgb1,b.rgb2,b.rgb3

    RGB_double_colour_spin_forward=c.rgb1,c.rgb2,c.rgb3
    RGB_double_colour_spin_reverse=d.rgb1,d.rgb2,d.rgb3

    RGB_quad_colour_rotate_forward_reverse=e.rgb1,e.rgb2,e.rgb3

    RGB_flash_colour_changers_and_smooth_shift_colour_change_contrast=f.rgb1,f.rgb2

    RGB_flash_flip_colour_changer=g.rgb1,g.rgb2,g.rgb3

    RGB_colour_flipper=h.rgb1,h.rgb2,h.rgb3

    RGB_colour_trail_blazer_forward_reverse=i.rgb1,i.rgb2

    RGB_colour_dimmer=j.rgb1,j.rgb2,j.rgb3,j.rgb4,j.rgb5,j.rgb6,j.rgb7

    RGB_single_colour_spin_forward_reverse_random=k.rgb1,k.rgb2,k.rgb3

    RGB_double_colour_spin_forward_reverse_random=l.rgb1,l.rgb2,l.rgb3

    RGB_colour_trail_blazer_forward_reverse_random=m.rgb1,m.rgb2,m.rgb3
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    # RGB colour value range: rgb1, rgb2, rgb3

    # red_yellow = rgb1
    # blue_green = rgb2
    # pink_cyan: = rgb3

    # select a class along with its colour index[n] value range:
    # 0 through 1, 0 through 2 and 0 through 7

    # Create a try and except handler that will execute when a class name and/or index[n] value exceeds
    # the range limit, which then executes the very first class name and index[n] value: 0. Note: index[n]
    # values always start at index[0] through index[n]. Note: the try and except handler needs no except:
    # handler type; the Robomaster S1 app has no, such except: handler types at all.

    try:
        RGB_double_colour_spin_forward[2]() # choose your RGB template class and colour index[n] value
    except:
        print('class name and/or index[n] value not found:')
        RGB_single_colour_spin_forward[0]() # class name defaults back to RGB_single_colour_spin_forward[0]

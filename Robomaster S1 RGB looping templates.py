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

    def rgb_single_red_yellow_spin_forward(): # function index[0]

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
    def rgb_single_blue_green_spin_forward(): # function index[1]

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
    def rgb_single_pink_cyan_spin_forward(): # function index[2]

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
    def rgb_single_red_yellow_spin_reverse(): # function index[3]

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
    def rgb_single_blue_green_spin_reverse(): # function index[4]

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
    def rgb_single_pink_cyan_spin_reverse(): # function index[5]

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
    def rgb_double_red_yellow_spin_forward(): # function index[6]

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
    def rgb_double_blue_green_spin_forward(): # function index[7]

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
    def rgb_double_pink_cyan_spin_forward(): # function index[8]

        while True:
            gun_led_on_off[1]()
            for i in range(4):
                led_set_top_bottom[0](define_armor_top_bottom_all[0],
                RGB_PC[i+1][0],RGB_PC[i+1][1],RGB_PC[i+1][2],define_effect[0])
                led_set_top_bottom[2](define_armor_top_bottom_all[0],[i+1,i+5],define_effect[1])
                led_set_top_bottom[1](define_armor_top_bottom_all[1],
                RGB_PC[i+1][0],RGB_PC[i+1][1],RGB_PC[i+1][2],define_effect[1])
                time.sleep(delay[1]);
                gun_led_on_off[0]()
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def rgb_double_red_yellow_spin_reverse(): # function index[9]

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
    def rgb_double_blue_green_spin_reverse(): # function index[10]

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
    def rgb_double_pink_cyan_spin_reverse():  # function index[11]

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
    def rgb_quad_red_yellow_rotate_forward_reverse(): # function index[12]

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
    def rgb_quad_blue_green_rotate_forward_reverse(): # function index[13]

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
    def rgb_quad_pink_cyan_rotate_forward_reverse(): # function index[14]

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
    def rgb_flash_colour_changers_forward_reverse(): # function index[15]

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
    def rgb_flash_flip_red_yellow_changer(): # function index[16]

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
    def rgb_flash_flip_blue_green_changer(): # function index[17]

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
    def rgb_flash_flip_pink_cyan_changer(): # function index[18]

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
    def rgb_red_yellow_flipper(): # function index[19]

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
    def rgb_blue_green_flipper(): # function index[20]

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
    def rgb_pink_cyan_flipper(): # function index[21]

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
    def rgb_colour_trail_chasers_forward(): # function index[22]

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
    def rgb_colour_trail_chasers_reverse(): # function index[23]

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
    def rgb_smooth_shift_colour_change_contrast(): # function index[24]

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
    def rgb_white_dimmer(): # function index[25]

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
    def rgb_red_dimmer(): # function index[26]

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
    def rgb_yellow_dimmer(): # function index[27]

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
    def rgb_blue_dimmer(): # function index[28]

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
    def rgb_green_dimmer(): # function index[29]

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
    def rgb_pink_dimmer(): # function index[30]

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
    def rgb_cyan_dimmer(): # function index[31]

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
    def rgb_single_red_yellow_spin_forward_reverse_random(): # function index[32]

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
    def rgb_single_blue_green_spin_forward_reverse_random(): # function index[33]

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
    def rgb_single_pink_cyan_spin_forward_reverse_random(): # function index[34]

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
    def rgb_double_red_yellow_spin_forward_reverse_random(): # function index[35]

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
    def rgb_double_blue_green_spin_forward_reverse_random(): # function index[36]

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
    def rgb_double_pink_cyan_spin_forward_reverse_random(): # function index[37]

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
    def rgb_trail_chasers_red_yellow_forward_reverse_random(): # function index[38]

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
    def rgb_trail_chasers_blue_green_forward_reverse_random(): # function index[39]

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
    def rgb_trail_chasers_pink_cyan_forward_reverse_random(): # function index[40]

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

    RGB_template_function_tuple=(
        rgb_single_red_yellow_spin_forward, # function index[0]
        rgb_single_blue_green_spin_forward, # function index[1]
        rgb_single_pink_cyan_spin_forward,  # function index[2]

        rgb_single_red_yellow_spin_reverse, # function index[3]
        rgb_single_blue_green_spin_reverse, # function index[4]
        rgb_single_pink_cyan_spin_reverse,  # function index[5]

        rgb_double_red_yellow_spin_forward, # function index[6]
        rgb_double_blue_green_spin_forward, # function index[7]
        rgb_double_pink_cyan_spin_forward,  # function index[8]

        rgb_double_red_yellow_spin_reverse, # function index[9]
        rgb_double_blue_green_spin_reverse, # function index[10]
        rgb_double_pink_cyan_spin_reverse,  # function index[11]

        rgb_quad_red_yellow_rotate_forward_reverse, # function index[12]
        rgb_quad_blue_green_rotate_forward_reverse, # function index[13]
        rgb_quad_pink_cyan_rotate_forward_reverse,  # function index[14]

        rgb_flash_colour_changers_forward_reverse, # function index[15]

        rgb_flash_flip_red_yellow_changer, # function index[16]
        rgb_flash_flip_blue_green_changer, # function index[17]
        rgb_flash_flip_pink_cyan_changer,  # function index[18]

        rgb_red_yellow_flipper, # function index[19]
        rgb_blue_green_flipper, # function index[20]
        rgb_pink_cyan_flipper,  # function index[21]

        rgb_colour_trail_chasers_forward, # function index[22]
        rgb_colour_trail_chasers_reverse, # function index[23]

        rgb_smooth_shift_colour_change_contrast, # function index[24]

        rgb_white_dimmer,  # function index[25]
        rgb_red_dimmer,    # function index[26]
        rgb_yellow_dimmer, # function index[27]
        rgb_blue_dimmer,   # function index[28]
        rgb_green_dimmer,  # function index[29]
        rgb_pink_dimmer,   # function index[30]
        rgb_cyan_dimmer,   # function index[31]

        rgb_single_red_yellow_spin_forward_reverse_random, # function index[32]
        rgb_single_blue_green_spin_forward_reverse_random, # function index[33]
        rgb_single_pink_cyan_spin_forward_reverse_random,  # function index[34]

        rgb_double_red_yellow_spin_forward_reverse_random, # function index[35]
        rgb_double_blue_green_spin_forward_reverse_random, # function index[36]
        rgb_double_pink_cyan_spin_forward_reverse_random,  # function index[37]

        rgb_trail_chasers_red_yellow_forward_reverse_random, # function index[38]
        rgb_trail_chasers_blue_green_forward_reverse_random, # function index[39]
        rgb_trail_chasers_pink_cyan_forward_reverse_random)  # function index[40]

    RGB_template_function_tuple[40]() # choose your RGB template tuple index[n]

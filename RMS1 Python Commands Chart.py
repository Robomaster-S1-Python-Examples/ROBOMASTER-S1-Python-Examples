# For advanced Python programmers only:

# Here is a complete Robomaster S1 Python commands chart
# for easier access. Turn these Robomaster S1 Python command
# sets into tuples( ), lists( ) and dictionaries{ }. Note: some of
# these Robomaster S1 Python commands will activate parts of
# the robot, without actually executing any Python code, such as
# flashing RGBs for example; the RGBs will blink, even though
# the Python commands are not used, but if you create a Python
# program, the RGBs are not affected by the blink rate Python
# commands, as long as the robot is executing Python code.
# Some of these Python commands also activate the chassis
# and the gimbal, without actually turning them on; just the
# commands alone activate parts of the robot. If you use this
# Robomaster S1 chart with tuples, lists and dictionaries, be
# vigilant of how the robot acts, during execution time. You
# might also find that some of this chart could create a conflict
# between the gimbal and the chassis Python command sets.
# Do not use such commands in tuples, lists or dictionaries if
# you find that the robot is not responding to the gimbal and
# chassis Python commands. The gimbal and the chassis
# cannot be activated together; one always overrides the other.
# Do not use Python threading for the robot's physical parts;
# you might get unwanted results, or even cause damage to the
# unit. Therefore, I do not recommend using Python threading
# for any of Robomaster S1's physical parts, including the RGBs.

# Note: do not remove the tripple quote marks. if you do,
# the Python commands will execute when you run your program.
# Only copy and paste them into actual Pythn code, do not
# remove any tripple quote marks...
'''
robot_ctrl.set_mode(rm_define.robot_mode_free)
robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)

rmexit()

armor_ctrl.set_hit_sensitivity(5)

armor_ctrl.cond_wait(rm_define.cond_ir_hit_detection)
armor_ctrl.cond_wait(rm_define.cond_armor_hit)
armor_ctrl.cond_wait(rm_define.cond_armor_bottom_front_hit)
armor_ctrl.cond_wait(rm_define.cond_armor_bottom_back_hit)
armor_ctrl.cond_wait(rm_define.cond_armor_bottom_left_hit)
armor_ctrl.cond_wait(rm_define.cond_armor_bottom_right_hit)

armor_ctrl.cond_wait(rm_define.cond_armor_top_left_hit)
armor_ctrl.cond_wait(rm_define.cond_armor_top_right_hit)

rm_define.armor_top_all
rm_define.armor_bottom_all
rm_define.armor_all

rm_define.armor_top_right
rm_define.armor_top_left)

rm_define.armor_bottom_right
rm_define.armor_bottom_left)
rm_define.armor_bottom_front
rm_define.armor_bottom_back

rm_define.effect_always_off
rm_define.effect_always_on
rm_define.effect_flash
rm_define.effect_breath
rm_define.effect_marquee

sensor_adapter_ctrl.cond_wait(rm_define.cond_sensor_adapter1_port1_low_event)
sensor_adapter_ctrl.cond_wait(rm_define.cond_sensor_adapter1_port1_high_event)

tools.timer_ctrl(rm_define.timer_start)
tools.timer_ctrl(rm_define.timer_stop)
tools.timer_ctrl(rm_define.timer_reset)

chassis_ctrl.set_pwm_value(rm_define.pwm_all,7.5)
chassis_ctrl.set_pwm_value(rm_define.pwm1,7.5)
chassis_ctrl.set_pwm_value(rm_define.pwm2,7.5)
chassis_ctrl.set_pwm_value(rm_define.pwm3,7.5)
chassis_ctrl.set_pwm_value(rm_define.pwm4,7.5)
chassis_ctrl.set_pwm_value(rm_define.pwm5,7.5)
chassis_ctrl.set_pwm_value(rm_define.pwm6,7.5)

gimbal_ctrl.enable_stick_overlay()
gimbal_ctrl.disable_stick_overlay()
chassis_ctrl.enable_stick_overlay()
chassis_ctrl.disable_stick_overlay()

chassis_ctrl.set_follow_gimbal_offset(0)
chassis_ctrl.set_trans_speed(0.5)
chassis_ctrl.set_rotate_speed(30)
chassis_ctrl.set_wheel_speed(100,100,100,100)

chassis_ctrl.set_wheel_speed(
100, Front Left
100, Front Right
100, Back Left
100) Back Right

chassis_ctrl.move(0),
chassis_ctrl.move_with_time(0,1)
chassis_ctrl.move_with_distance(0,1)
chassis_ctrl.move_with_speed(0.5,0.5,30)
chassis_ctrl.move_degree_with_speed(0.5,0)
chassis_ctrl.move_and_rotate(0,rm_define.clockwise)
chassis_ctrl.move_and_rotate(0,rm_define.anticlockwise)

chassis_ctrl.rotate(rm_define.clockwise)
chassis_ctrl.rotate(rm_define.anticlockwise)
chassis_ctrl.rotate_with_time(rm_define.clockwise,0)
chassis_ctrl.rotate_with_time(rm_define.anticlockwise,0)
chassis_ctrl.rotate_with_degree(rm_define.clockwise,0)
chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,0)
chassis_ctrl.rotate_with_speed(rm_define.clockwise,30)
chassis_ctrl.rotate_with_speed(rm_define.anticlockwise,30)

gimbal_ctrl.set_follow_chassis_offset(0)
gimbal_ctrl.set_rotate_speed(30)
gimbal_ctrl.rotate_with_speed(30,30)

gimbal_ctrl.recenter()
gimbal_ctrl.stop()
gimbal_ctrl.suspend()
gimbal_ctrl.resume()

gimbal_ctrl.rotate(rm_define.gimbal_up)
gimbal_ctrl.rotate(rm_define.gimbal_down)
gimbal_ctrl.rotate(rm_define.gimbal_left)
gimbal_ctrl.rotate(rm_define.gimbal_right)

gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up,0)
gimbal_ctrl.rotate_with_degree(rm_define.gimbal_down,0)
gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left,0)
gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right,0)

gimbal_ctrl.yaw_ctrl(0)
gimbal_ctrl.pitch_ctrl(0)
gimbal_ctrl.angle_ctrl(0,0)

gun_ctrl.fire_once()
gun_ctrl.fire_continuous()
gun_ctrl.stop()

ir_blaster_ctrl.set_fire_count(1)
ir_blaster_ctrl.fire_once()
ir_blaster_ctrl.fire_continuous()
ir_blaster_ctrl.stop()

led_ctrl.set_top_led
led_ctrl.set_bottom_led
led_ctrl.set_single_led
led_ctrl.turn_off(rm_define.armor_all)
led_ctrl.set_flash(rm_define.armor_all,6)

led_ctrl.gun_led_off
led_ctrl.gun_led_on

vision_ctrl.enable_detection(rm_define.vision_detection_marker)
vision_ctrl.enable_detection(rm_define.vision_detection_pose)
vision_ctrl.enable_detection(rm_define.vision_detection_people)
vision_ctrl.enable_detection(rm_define.vision_detection_car)
vision_ctrl.disable_detection(rm_define.vision_detection_marker)
vision_ctrl.disable_detection(rm_define.vision_detection_pose)
vision_ctrl.disable_detection(rm_define.vision_detection_people)
vision_ctrl.disable_detection(rm_define.vision_detection_car)
vision_ctrl.enable_detection(rm_define.vision_detection_line)
vision_ctrl.disable_detection(rm_define.vision_detection_line)

vision_ctrl.set_marker_detection_distance(1)
vision_ctrl.marker_detection_color_set(rm_define.marker_detection_color_red)
vision_ctrl.marker_detection_color_set(rm_define.marker_detection_color_blue)
vision_ctrl.marker_detection_color_set(rm_define.marker_detection_color_green)

vision_ctrl.line_follow_color_set(rm_define.line_follow_color_blue)
vision_ctrl.line_follow_color_set(rm_define.line_follow_color_red)
vision_ctrl.line_follow_color_set(rm_define.line_follow_color_green)

vision_ctrl.detect_marker_and_aim(rm_define.marker_trans_red_heart)
vision_ctrl.detect_marker_and_aim(rm_define.marker_trans_target)
vision_ctrl.detect_marker_and_aim(rm_define.marker_trans_dice)
vision_ctrl.detect_marker_and_aim(rm_define.marker_number_zero)
vision_ctrl.detect_marker_and_aim(rm_define.marker_number_one)
vision_ctrl.detect_marker_and_aim(rm_define.marker_number_two)
vision_ctrl.detect_marker_and_aim(rm_define.marker_number_three)
vision_ctrl.detect_marker_and_aim(rm_define.marker_number_four)
vision_ctrl.detect_marker_and_aim(rm_define.marker_number_five)
vision_ctrl.detect_marker_and_aim(rm_define.marker_number_six)
vision_ctrl.detect_marker_and_aim(rm_define.marker_number_seven)
vision_ctrl.detect_marker_and_aim(rm_define.marker_number_eight)
vision_ctrl.detect_marker_and_aim(rm_define.marker_number_nine)

vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_A)
vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_B)
vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_C)
vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_D)
vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_E)
vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_F)
vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_G)
vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_H)
vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_I)
vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_J)
vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_K)
vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_L)
vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_M)
vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_N)
vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_O)
vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_P)
vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_Q)
vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_R)
vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_S)
vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_T)
vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_U)
vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_V)
vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_W)
vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_X)
vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_Y)
vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_Z)

vision_ctrl.cond_wait(rm_define.cond_recognized_people)
vision_ctrl.cond_wait(rm_define.cond_recognized_car)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_trans_all)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_trans_left)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_trans_right)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_trans_forward)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_trans_stop)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_trans_red_heart)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_trans_target)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_trans_dice)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_number_all)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_number_zero)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_number_one)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_number_two)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_number_three)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_number_four)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_number_five)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_number_six)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_number_seven)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_number_eight)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_number_nine)

vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_all)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_A)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_B)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_C)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_D)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_E)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_F)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_G)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_H)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_I)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_J)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_K)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_L)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_M)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_N)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_O)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_P)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_Q)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_R)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_S)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_T)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_U)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_V)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_W)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_X)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_Y)
vision_ctrl.cond_wait(rm_define.cond_recognized_marker_letter_Z)

media_ctrl.enable_sound_recognition(rm_define.sound_detection_applause)
media_ctrl.disable_sound_recognition(rm_define.sound_detection_applause)
media_ctrl.cond_wait(rm_define.cond_sound_recognized_applause_twice)
media_ctrl.cond_wait(rm_define.cond_sound_recognized_applause_thrice)
media_ctrl.exposure_value_update(rm_define.exposure_value_large)
media_ctrl.exposure_value_update(rm_define.exposure_value_medium)
media_ctrl.exposure_value_update(rm_define.exposure_value_small)

media_ctrl.play_sound(rm_define.media_sound_solmization_1C)
media_ctrl.play_sound(rm_define.media_sound_solmization_1D)
media_ctrl.play_sound(rm_define.media_sound_solmization_1E)
media_ctrl.play_sound(rm_define.media_sound_solmization_1F)
media_ctrl.play_sound(rm_define.media_sound_solmization_1G)
media_ctrl.play_sound(rm_define.media_sound_solmization_1A)
media_ctrl.play_sound(rm_define.media_sound_solmization_1B)
media_ctrl.play_sound(rm_define.media_sound_solmization_2C)
media_ctrl.play_sound(rm_define.media_sound_solmization_2D)
media_ctrl.play_sound(rm_define.media_sound_solmization_2E)
media_ctrl.play_sound(rm_define.media_sound_solmization_2F)
media_ctrl.play_sound(rm_define.media_sound_solmization_2G)
media_ctrl.play_sound(rm_define.media_sound_solmization_2A)
media_ctrl.play_sound(rm_define.media_sound_solmization_2B)
media_ctrl.play_sound(rm_define.media_sound_solmization_3C)
media_ctrl.play_sound(rm_define.media_sound_solmization_3D)
media_ctrl.play_sound(rm_define.media_sound_solmization_3E)
media_ctrl.play_sound(rm_define.media_sound_solmization_3F)
media_ctrl.play_sound(rm_define.media_sound_solmization_3G)
media_ctrl.play_sound(rm_define.media_sound_solmization_3A)
media_ctrl.play_sound(rm_define.media_sound_solmization_3B)

media_ctrl.play_sound(rm_define.media_sound_solmization_3B)
media_ctrl.play_sound(rm_define.media_sound_solmization_3A)
media_ctrl.play_sound(rm_define.media_sound_solmization_3G)
media_ctrl.play_sound(rm_define.media_sound_solmization_3F)
media_ctrl.play_sound(rm_define.media_sound_solmization_3E)
media_ctrl.play_sound(rm_define.media_sound_solmization_3D)
media_ctrl.play_sound(rm_define.media_sound_solmization_3C)
media_ctrl.play_sound(rm_define.media_sound_solmization_2B)
media_ctrl.play_sound(rm_define.media_sound_solmization_2A)
media_ctrl.play_sound(rm_define.media_sound_solmization_2G)
media_ctrl.play_sound(rm_define.media_sound_solmization_2F)
media_ctrl.play_sound(rm_define.media_sound_solmization_2E)
media_ctrl.play_sound(rm_define.media_sound_solmization_2D)
media_ctrl.play_sound(rm_define.media_sound_solmization_2C)
media_ctrl.play_sound(rm_define.media_sound_solmization_1B)
media_ctrl.play_sound(rm_define.media_sound_solmization_1A)
media_ctrl.play_sound(rm_define.media_sound_solmization_1G)
media_ctrl.play_sound(rm_define.media_sound_solmization_1F)
media_ctrl.play_sound(rm_define.media_sound_solmization_1E)
media_ctrl.play_sound(rm_define.media_sound_solmization_1D)
media_ctrl.play_sound(rm_define.media_sound_solmization_1C)

media_ctrl.play_sound(rm_define.media_sound_solmization_3ASharp)
media_ctrl.play_sound(rm_define.media_sound_solmization_3GSharp)
media_ctrl.play_sound(rm_define.media_sound_solmization_3FSharp)
media_ctrl.play_sound(rm_define.media_sound_solmization_3DSharp)
media_ctrl.play_sound(rm_define.media_sound_solmization_3CSharp)
media_ctrl.play_sound(rm_define.media_sound_solmization_2ASharp)
media_ctrl.play_sound(rm_define.media_sound_solmization_2GSharp)
media_ctrl.play_sound(rm_define.media_sound_solmization_2FSharp)
media_ctrl.play_sound(rm_define.media_sound_solmization_2DSharp)
media_ctrl.play_sound(rm_define.media_sound_solmization_2CSharp)
media_ctrl.play_sound(rm_define.media_sound_solmization_1ASharp)
media_ctrl.play_sound(rm_define.media_sound_solmization_1GSharp)
media_ctrl.play_sound(rm_define.media_sound_solmization_1FSharp)
media_ctrl.play_sound(rm_define.media_sound_solmization_1DSharp)
media_ctrl.play_sound(rm_define.media_sound_solmization_1CSharp)

media_ctrl.play_sound(rm_define.media_sound_attacked)
media_ctrl.play_sound(rm_define.media_sound_shoot)
media_ctrl.play_sound(rm_define.media_sound_scanning)
media_ctrl.play_sound(rm_define.media_sound_recognize_success)
media_ctrl.play_sound(rm_define.media_sound_gimbal_rotate)
media_ctrl.play_sound(rm_define.media_sound_count_down)
media_ctrl.play_sound(rm_define.media_custom_audio_undefined)

media_ctrl.capture()

media_ctrl.record(1)
media_ctrl.record(0)

media_ctrl.zoom_value_update(1)
media_ctrl.zoom_value_update(2)
media_ctrl.zoom_value_update(3)
media_ctrl.zoom_value_update(4)

if armor_ctrl.check_condition(rm_define.cond_armor_hit):
  pass

if armor_ctrl.check_condition(rm_define.cond_armor_bottom_front_hit):
  pass

if armor_ctrl.check_condition(rm_define.cond_armor_bottom_back_hit):
  pass

if armor_ctrl.check_condition(rm_define.cond_armor_bottom_left_hit):
  pass

if armor_ctrl.check_condition(rm_define.cond_armor_bottom_right_hit):
  pass

if armor_ctrl.check_condition(rm_define.cond_armor_top_left_hit):
  pass

if armor_ctrl.check_condition(rm_define.cond_armor_top_right_hit):
  pass

if armor_ctrl.check_condition(rm_define.cond_ir_hit_detection):
  pass

media_ctrl.play_sound(rm_define.media_sound_attacked,wait_for_complete_flag=True)
media_ctrl.play_sound(rm_define.media_sound_shoot,wait_for_complete_flag=True)
media_ctrl.play_sound(rm_define.media_sound_scanning,wait_for_complete_flag=True)
media_ctrl.play_sound(rm_define.media_sound_recognize_success,wait_for_complete_flag=True)
media_ctrl.play_sound(rm_define.media_sound_gimbal_rotate,wait_for_complete_flag=True)
media_ctrl.play_sound(rm_define.media_sound_count_down,wait_for_complete_flag=True)
media_ctrl.play_sound(rm_define.media_custom_audio_undefined,wait_for_complete_flag=True)

def armor_hit_detection_all(msg):
    pass

def armor_hit_detection_bottom_front(msg):
    pass

def armor_hit_detection_bottom_back(msg):
    pass

def armor_hit_detection_bottom_left(msg):
    pass

def armor_hit_detection_bottom_right(msg):
    pass

def armor_hit_detection_top_left(msg):
    pass

def armor_hit_detection_top_right(msg):
    pass

def ir_hit_detection_event(msg):
    pass

def ir_distance_1_ge_10_event(msg):
    pass

def ir_distance_1_le_10_event(msg):
    pass

def sensor_adapter1_port1_high_event(msg):
    pass

def sensor_adapter1_port1_low_event(msg):
    pass

# RGB tuple items with their tuple indexes:

led_set_top_bottom=(
    led_ctrl.set_top_led,    #index[0]
    led_ctrl.set_bottom_led, #index[1]
    led_ctrl.set_single_led, #index[2]
    led_ctrl.turn_off(rm_define.armor_all),    #index[3]
    led_ctrl.set_flash(rm_define.armor_all,6)) #index[4]

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
'''
# RGB Tuple Colour Guide:

rgb1,rgb2=0,255 # dim and change all rgb colours by changing the values: '0' and '255'

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

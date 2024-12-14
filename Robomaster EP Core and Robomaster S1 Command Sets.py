# Robomaster EP Core Robot and Robomaster S1 Robot Command Sets

# Created by Joseph C. Richardson, GitHub.com

# System

robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)

robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)

robot_ctrl.set_mode(rm_define.robot_mode_free)


tools.timer_ctrl(rm_define.timer_start)

tools.timer_ctrl(rm_define.timer_stop)

tools.timer_ctrl(rm_define.timer_reset)

media_ctrl.zoom_value_update(4)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# LED Effects

led_ctrl.set_flash(rm_define.armor_all,10)

led_ctrl.set_flash(rm_define.armor_bottom_front,10)

led_ctrl.set_flash(rm_define.armor_bottom_back,10)

led_ctrl.set_flash(rm_define.armor_bottom_left,10)

led_ctrl.set_flash(rm_define.armor_bottom_right,10)

led_ctrl.set_flash(rm_define.armor_top_left,10)

led_ctrl.set_flash(rm_define.armor_top_right,10)


led_ctrl.set_bottom_led(rm_define.armor_bottom_all,69,215,255,rm_define.effect_always_on)

led_ctrl.set_bottom_led(rm_define.armor_bottom_all,69,215,255,rm_define.effect_always_off)

led_ctrl.set_bottom_led(rm_define.armor_bottom_all,69,215,255,rm_define.effect_breath)

led_ctrl.set_bottom_led(rm_define.armor_bottom_all,69,215,255,rm_define.effect_flash)


led_ctrl.set_bottom_led(rm_define.armor_bottom_front,69,215,255,rm_define.effect_always_on)

led_ctrl.set_bottom_led(rm_define.armor_bottom_front,69,215,255,rm_define.effect_always_off)

led_ctrl.set_bottom_led(rm_define.armor_bottom_front,69,215,255,rm_define.effect_breath)

led_ctrl.set_bottom_led(rm_define.armor_bottom_front,69,215,255,rm_define.effect_flash)


led_ctrl.set_bottom_led(rm_define.armor_bottom_back,69,215,255,rm_define.effect_always_on)

led_ctrl.set_bottom_led(rm_define.armor_bottom_back,69,215,255,rm_define.effect_always_off)

led_ctrl.set_bottom_led(rm_define.armor_bottom_back,69,215,255,rm_define.effect_breath)

led_ctrl.set_bottom_led(rm_define.armor_bottom_back,69,215,255,rm_define.effect_flash)


led_ctrl.set_bottom_led(rm_define.armor_bottom_left,69,215,255,rm_define.effect_always_on)

led_ctrl.set_bottom_led(rm_define.armor_bottom_left,69,215,255,rm_define.effect_always_off)

led_ctrl.set_bottom_led(rm_define.armor_bottom_left,69,215,255,rm_define.effect_breath)

led_ctrl.set_bottom_led(rm_define.armor_bottom_left,69,215,255,rm_define.effect_flash)


led_ctrl.set_bottom_led(rm_define.armor_bottom_right,69,215,255,rm_define.effect_always_on)

led_ctrl.set_bottom_led(rm_define.armor_bottom_right,69,215,255,rm_define.effect_always_off)

led_ctrl.set_bottom_led(rm_define.armor_bottom_right,69,215,255,rm_define.effect_breath)

led_ctrl.set_bottom_led(rm_define.armor_bottom_right,69,215,255,rm_define.effect_flash)


led_ctrl.set_top_led(rm_define.armor_top_all,69,215,255,rm_define.effect_always_on)

led_ctrl.set_top_led(rm_define.armor_top_all,69,215,255,rm_define.effect_always_off)

led_ctrl.set_top_led(rm_define.armor_top_all,69,215,255,rm_define.effect_breath)

led_ctrl.set_top_led(rm_define.armor_top_all,69,215,255,rm_define.effect_flash)


led_ctrl.set_top_led(rm_define.armor_top_left,69,215,255,rm_define.effect_always_on)

led_ctrl.set_top_led(rm_define.armor_top_left,69,215,255,rm_define.effect_always_off)

led_ctrl.set_top_led(rm_define.armor_top_left,69,215,255,rm_define.effect_breath)

led_ctrl.set_top_led(rm_define.armor_top_left,69,215,255,rm_define.effect_flash)


led_ctrl.set_top_led(rm_define.armor_top_right,69,215,255,rm_define.effect_always_on)

led_ctrl.set_top_led(rm_define.armor_top_right,69,215,255,rm_define.effect_always_off)

led_ctrl.set_top_led(rm_define.armor_top_right,69,215,255,rm_define.effect_breath)

led_ctrl.set_top_led(rm_define.armor_top_right,69,215,255,rm_define.effect_flash)


led_ctrl.set_single_led(rm_define.armor_top_all,[1,8],rm_define.effect_always_on)

led_ctrl.set_single_led(rm_define.armor_top_all,[1,8],rm_define.effect_always_off)


led_ctrl.set_single_led(rm_define.armor_top_left,[1,8],rm_define.effect_always_on)

led_ctrl.set_single_led(rm_define.armor_top_left,[1,8],rm_define.effect_always_off)


led_ctrl.set_single_led(rm_define.armor_top_right,[1,8],rm_define.effect_always_on)

led_ctrl.set_single_led(rm_define.armor_top_right,[1,8],rm_define.effect_always_off)


led_ctrl.turn_off(rm_define.armor_all)

led_ctrl.turn_off(rm_define.armor_bottom_front)

led_ctrl.turn_off(rm_define.armor_bottom_back)

led_ctrl.turn_off(rm_define.armor_bottom_left)

led_ctrl.turn_off(rm_define.armor_bottom_right)


led_ctrl.turn_off(rm_define.armor_top_left)

led_ctrl.turn_off(rm_define.armor_top_right)


led_ctrl.gun_led_on()

led_ctrl.gun_led_off()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Chassis

chassis_ctrl.set_pwm_value(rm_define.pwm_all, 7.5)

chassis_ctrl.set_pwm_value(rm_define.pwm1, 7.5)

chassis_ctrl.set_pwm_value(rm_define.pwm2, 7.5)

chassis_ctrl.set_pwm_value(rm_define.pwm3, 7.5)

chassis_ctrl.set_pwm_value(rm_define.pwm4, 7.5)

chassis_ctrl.set_pwm_value(rm_define.pwm5, 7.5)

chassis_ctrl.set_pwm_value(rm_define.pwm6, 7.5)


chassis_ctrl.enable_stick_overlay()

chassis_ctrl.disable_stick_overlay()


chassis_ctrl.set_follow_gimbal_offset(90)

chassis_ctrl.set_trans_speed(0.5)

chassis_ctrl.set_rotate_speed(30)

chassis_ctrl.set_wheel_speed(100,100,100,100)


chassis_ctrl.move(0)

chassis_ctrl.move_with_time(0,1)

chassis_ctrl.move_with_distance(0,1)

chassis_ctrl.move_degree_with_speed(0.5,0)


chassis_ctrl.rotate(rm_define.clockwise)

chassis_ctrl.rotate(rm_define.anticlockwise)

chassis_ctrl.rotate_with_time(rm_define.clockwise, 1)

chassis_ctrl.rotate_with_time(rm_define.anticlockwise, 1)

chassis_ctrl.rotate_with_time(rm_define.clockwise, 1)

chassis_ctrl.rotate_with_time(rm_define.anticlockwise, 1)

chassis_ctrl.rotate_with_degree(rm_define.clockwise,0)

chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,0)

chassis_ctrl.rotate_with_speed(rm_define.clockwise,30)


chassis_ctrl.move_with_speed(0.5,0.5,30)

chassis_ctrl.stop()

def chassis_impact_detection(msg):
    pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Gimbal

gimbal_ctrl.disable_stick_overlay()

gimbal_ctrl.enable_stick_overlay()

gimbal_ctrl.set_follow_chassis_offset(0)

gimbal_ctrl.set_rotate_speed(30)

gimbal_ctrl.recenter()

gimbal_ctrl.rotate(rm_define.gimbal_up)

gimbal_ctrl.rotate(rm_define.gimbal_down)

gimbal_ctrl.rotate(rm_define.gimbal_left)

gimbal_ctrl.rotate(rm_define.gimbal_right)

gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up,0)

gimbal_ctrl.yaw_ctrl(0)

gimbal_ctrl.pitch_ctrl(0)

gimbal_ctrl.angle_ctrl(0, 0)

gimbal_ctrl.rotate_with_speed(30,30)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Blaster Gun

gun_ctrl.set_fire_count(1)

gun_ctrl.fire_once()

gun_ctrl.fire_continuous()

gun_ctrl.stop()


ir_blaster_ctrl.set_fire_count(1)

ir_blaster_ctrl.fire_once()

ir_blaster_ctrl.fire_continuous()

ir_blaster_ctrl.stop()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Extension Module

gripper_ctrl.open()

gripper_ctrl.close()

gripper_ctrl.stop()


obotic_arm_ctrl.move(50,0, wait_for_complete=True)

robotic_arm_ctrl.move(-50,0,wait_for_complete=True)

robotic_arm_ctrl.move(0,50,wait_for_complete=True)

robotic_arm_ctrl.move(0,-50,wait_for_complete=True)

robotic_arm_ctrl.move(50,0,wait_for_complete=True)

robotic_arm_ctrl.move(-50,0,wait_for_complete=True)

robotic_arm_ctrl.move(0,50,wait_for_complete=True)

robotic_arm_ctrl.move(0,-50,wait_for_complete=True)

robotic_arm_ctrl.moveto(50,50,wait_for_complete=True)

robotic_arm_ctrl.moveto(50,50,wait_for_complete=True)

robotic_arm_ctrl.recenter(wait_for_complete=True)


servo_ctrl.set_angle(1,90,wait_for_complete=True)

servo_ctrl.set_angle(2,90,wait_for_complete=True)

servo_ctrl.set_angle(3,90,wait_for_complete=True)

servo_ctrl.recenter(1, wait_for_complete=True)

servo_ctrl.set_speed(1, 10)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Smart

vision_ctrl.enable_detection(rm_define.vision_detection_marker)

vision_ctrl.disable_detection(rm_define.vision_detection_marker)


vision_ctrl.enable_detection(rm_define.vision_detection_pose)

vision_ctrl.disable_detection(rm_define.vision_detection_pose)


vision_ctrl.enable_detection(rm_define.vision_detection_people)

vision_ctrl.disable_detection(rm_define.vision_detection_people)


vision_ctrl.enable_detection(rm_define.vision_detection_car)

vision_ctrl.disable_detection(rm_define.vision_detection_car)


vision_ctrl.enable_detection(rm_define.vision_detection_line)

vision_ctrl.disable_detection(rm_define.vision_detection_line)


media_ctrl.enable_sound_recognition(rm_define.sound_detection_applause)

media_ctrl.disable_sound_recognition(rm_define.sound_detection_applause)


vision_ctrl.set_marker_detection_distance(1)


vision_ctrl.marker_detection_color_set(rm_define.marker_detection_color_red)

vision_ctrl.marker_detection_color_set(rm_define.marker_detection_color_blue)

vision_ctrl.marker_detection_color_set(rm_define.marker_detection_color_green)


vision_ctrl.line_follow_color_set(rm_define.line_follow_color_blue)

vision_ctrl.line_follow_color_set(rm_define.line_follow_color_red)

vision_ctrl.line_follow_color_set(rm_define.line_follow_color_green)


media_ctrl.exposure_value_update(rm_define.exposure_value_large)

media_ctrl.exposure_value_update(rm_define.exposure_value_medium)

media_ctrl.exposure_value_update(rm_define.exposure_value_small)


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


vision_ctrl.cond_wait(rm_define.cond_recognized_pose_all)

vision_ctrl.cond_wait(rm_define.cond_recognized_pose_victory)

vision_ctrl.cond_wait(rm_define.cond_recognized_pose_give_in)

vision_ctrl.cond_wait(rm_define.cond_recognized_pose_capture)


media_ctrl.cond_wait(rm_define.cond_sound_recognized_applause_twice)

media_ctrl.cond_wait(rm_define.cond_sound_recognized_applause_thrice)


def vision_recognized_people(msg):
    pass

def sound_recognized_applause_twice(msg):
    pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Armor

armor_ctrl.set_hit_sensitivity(5)

armor_ctrl.cond_wait(rm_define.cond_armor_hit)

armor_ctrl.cond_wait(rm_define.cond_armor_bottom_front_hit)

armor_ctrl.cond_wait(rm_define.cond_armor_bottom_back_hit)

armor_ctrl.cond_wait(rm_define.cond_armor_bottom_left_hit)

armor_ctrl.cond_wait(rm_define.cond_armor_bottom_right_hit)

armor_ctrl.cond_wait(rm_define.cond_armor_top_left_hit)

armor_ctrl.cond_wait(rm_define.cond_armor_top_right_hit)

armor_ctrl.cond_wait(rm_define.cond_ir_hit_detection)

armor_ctrl.cond_wait(rm_define.cond_armor_top_right_hit)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Sensors

ir_distance_sensor_ctrl.enable_measure(4)

ir_distance_sensor_ctrl.disable_measure(4)

ir_distance_sensor_ctrl.cond_wait("ir_distance_4_ge_10")

ir_distance_sensor_ctrl.cond_wait("ir_distance_4_le_10")

def ir_distance_1_ge_10_event(msg):
    pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Sensor Adapter

sensor_adapter_ctrl.cond_wait(rm_define.cond_sensor_adapter6_port2_high_event)


def sensor_adapter1_port1_high_event(msg):
    pass
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Media

media_ctrl.play_sound(rm_define.media_sound_solmization_3C)

media_ctrl.play_sound(rm_define.media_sound_attacked)

media_ctrl.play_sound(rm_define.media_sound_shoot)

media_ctrl.play_sound(rm_define.media_sound_scanning)

media_ctrl.play_sound(rm_define.media_sound_recognize_success)

media_ctrl.play_sound(rm_define.media_sound_gimbal_rotate)

media_ctrl.play_sound(rm_define.media_sound_count_down)


media_ctrl.play_sound(rm_define.media_sound_attacked,wait_for_complete_flag=True)

media_ctrl.play_sound(rm_define.media_sound_shoot,wait_for_complete_flag=True)

media_ctrl.play_sound(rm_define.media_sound_scanning,wait_for_complete_flag=True)

media_ctrl.play_sound(rm_define.media_sound_recognize_success,wait_for_complete_flag=True)

media_ctrl.play_sound(rm_define.media_sound_gimbal_rotate,wait_for_complete_flag=True)

media_ctrl.play_sound(rm_define.media_sound_count_down,wait_for_complete_flag=True)


media_ctrl.play_sound(rm_define.media_custom_audio_undefined)

media_ctrl.play_sound(rm_define.media_custom_audio_undefined,wait_for_complete_flag=True)


media_ctrl.capture()

media_ctrl.record(0)

media_ctrl.record(1)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Commands

time.sleep(1)


for count in range(10):
    pass


while True:
    pass

if False:
    pass


if False:
    pass
else:
    pass


while not False:
    pass


rmexit()

# I am almost a complete Walking Human Computer Science Research
# Laboratory Machine on Two Legs...

Auto = 0

def on_pin_pressed_p0():
    global Auto
    Auto = Auto + 1
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_pin_pressed_p1():
    global Auto
    Auto = Auto - 1
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_forever():
    pins.digital_write_pin(DigitalPin.P0, 0)
    if Auto <= 30:
        servos.P0.set_angle(90)
    else:
        servos.P0.set_angle(180)
    basic.show_number(Auto)
    if Auto <= 30:
        pins.digital_write_pin(DigitalPin.P10, 0)
        pins.digital_write_pin(DigitalPin.P5, 1)
    else:
        pins.digital_write_pin(DigitalPin.P5, 0)
        pins.digital_write_pin(DigitalPin.P10, 1)
basic.forever(on_forever)

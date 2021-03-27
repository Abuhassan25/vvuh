let Auto = 0
input.onPinPressed(TouchPin.P0, function () {
    Auto = Auto + 1
})
input.onPinPressed(TouchPin.P1, function () {
    Auto = Auto - 1
})
basic.forever(function () {
    pins.digitalWritePin(DigitalPin.P0, 0)
    if (Auto <= 30) {
        servos.P0.setAngle(90)
    } else {
        servos.P0.setAngle(180)
    }
    basic.showNumber(Auto)
    if (Auto <= 30) {
        pins.digitalWritePin(DigitalPin.P10, 0)
        pins.digitalWritePin(DigitalPin.P5, 1)
    } else {
        pins.digitalWritePin(DigitalPin.P5, 0)
        pins.digitalWritePin(DigitalPin.P10, 1)
    }
})

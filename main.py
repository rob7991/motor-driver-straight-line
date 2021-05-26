def turnLeft():
    kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR1,
        kitronik_klip_motor.MotorDirection.REVERSE,
        80)
    kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR2,
        kitronik_klip_motor.MotorDirection.FORWARD,
        80)
    basic.show_leds("""
        . . # . .
        . # . # #
        # . . . .
        . # . # #
        . . # . .
        """)
def stop():
    kitronik_klip_motor.motor_off(kitronik_klip_motor.Motors.MOTOR1)
    kitronik_klip_motor.motor_off(kitronik_klip_motor.Motors.MOTOR2)
    basic.show_leds("""
        # . # . #
        . # . # .
        # . # . #
        . # . # .
        # . # . #
        """)

def on_button_pressed_a():
    global prettyLights
    prettyLights = kitronik_klip_motor.create_zip_string(5)
    prettyLights.show_rainbow()
    prettyLights.show()
    driveforward()
    basic.pause(travelDistance)
    turnLeft()
    basic.pause(turnTime)
    driveforward()
    basic.pause(travelDistance)
    turnLeft()
    basic.pause(turnTime)
    driveforward()
    basic.pause(travelDistance)
    turnLeft()
    basic.pause(turnTime)
    driveforward()
    basic.pause(travelDistance)
    stop()
input.on_button_pressed(Button.A, on_button_pressed_a)

def driveforward():
    kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR1,
        kitronik_klip_motor.MotorDirection.FORWARD,
        80)
    kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR2,
        kitronik_klip_motor.MotorDirection.FORWARD,
        80)
    basic.show_leds("""
        . # . # .
        . # . # .
        # . . . #
        . # . # .
        . . # . .
        """)
prettyLights: kitronik_klip_motor.ZIPString = None
travelDistance = 5000
turnTime = 150
bluetooth.start_magnetometer_service()
bluetooth.start_led_service()
degrees = input.compass_heading()
basic.show_string("COMPASS")

def on_forever():
    global degrees
    degrees = input.compass_heading()
    if degrees < 45 or degrees > 315:
        basic.show_string("N")
    elif degrees < 135:
        basic.show_string("E")
    elif degrees < 225:
        basic.show_string("S")
    else:
        basic.show_string("W")
basic.forever(on_forever)

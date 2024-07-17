import uinput

events = (
    uinput.BTN_JOYSTICK,
    uinput.ABS_X + (0, 255, 0, 0),
    uinput.ABS_Y + (0, 255, 0, 0),
    )
with uinput.Device(events) as device:
    device.emit(uinput.ABS_X, 5, syn=False)
    device.emit(uinput.ABS_Y, 5)
    device.emit_click(uinput.BTN_JOYSTICK)

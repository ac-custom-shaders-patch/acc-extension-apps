try:
    import ac
    import acsys
    import traceback
    import time
except ImportError:
    pass

app = 0
error = 0
rainStrengthValue = 0
rainWiperSpeedValue = 0
timer = 0.0

def acMain(ac_version):
    global app, rainStrengthValue, rainWiperSpeedValue
    app = ac.newApp("Shaders Patch Rain")
    ac.setTitle(app, "Rain")
    ac.setSize(app, 174, 108)

    y = 40
    rainStrengthLabel = ac.addLabel(app, "Strength")
    ac.setPosition(rainStrengthLabel, 110, y)
    rainStrengthValue = ac.addLabel(app, "")
    ac.setPosition(rainStrengthValue, 48, y)
    rainStrengthDownButton = ac.addButton(app, "-")
    ac.setPosition(rainStrengthDownButton, 16, y)
    ac.setSize(rainStrengthDownButton, 24, 24)
    ac.setFontSize(rainStrengthDownButton, 14)
    ac.addOnClickedListener(rainStrengthDownButton, rainStrengthDown)
    rainStrengthUpButton = ac.addButton(app, "+")
    ac.setPosition(rainStrengthUpButton, 80, y)
    ac.setSize(rainStrengthUpButton, 24, 24)
    ac.setFontSize(rainStrengthUpButton, 14)
    ac.addOnClickedListener(rainStrengthUpButton, rainStrengthUp)

    y = 72
    rainWiperSpeedLabel = ac.addLabel(app, "Wiper")
    ac.setPosition(rainWiperSpeedLabel, 110, y)
    rainWiperSpeedValue = ac.addLabel(app, "")
    ac.setPosition(rainWiperSpeedValue, 48, y)
    rainWiperSpeedDownButton = ac.addButton(app, "-")
    ac.setPosition(rainWiperSpeedDownButton, 16, y)
    ac.setSize(rainWiperSpeedDownButton, 24, 24)
    ac.setFontSize(rainWiperSpeedDownButton, 14)
    ac.addOnClickedListener(rainWiperSpeedDownButton, rainWiperSpeedDown)

    rainWiperSpeedUpButton = ac.addButton(app, "+")
    ac.setPosition(rainWiperSpeedUpButton, 80, y)
    ac.setSize(rainWiperSpeedUpButton, 24, 24)
    ac.setFontSize(rainWiperSpeedUpButton, 14)
    ac.addOnClickedListener(rainWiperSpeedUpButton, rainWiperSpeedUp)
    return "AccExtRain"

def rainStrengthDown(*args):
    try:
        ac.ext_rainParamsAdjust(-0.1, 0.0)
    except:
        ac.setText(debug, "AccExtRain: Shaders Patch not active? : \n" + traceback.format_exc())

def rainStrengthUp(*args):
    try:
        ac.ext_rainParamsAdjust(0.1, 0.0)
    except:
        ac.setText(debug, "AccExtRain: Shaders Patch not active? : \n" + traceback.format_exc())

def rainWiperSpeedDown(*args):
    try:
        ac.ext_rainParamsAdjust(0.0, -1.0)
    except:
        ac.setText(debug, "AccExtRain: Shaders Patch not active? : \n" + traceback.format_exc())

def rainWiperSpeedUp(*args):
    try:
        ac.ext_rainParamsAdjust(0.0, 1.0)
    except:
        ac.setText(debug, "AccExtRain: Shaders Patch not active? : \n" + traceback.format_exc())

def acUpdate(delta_t):
    global error, rainStrengthValue, rainWiperSpeedValue, debug
    global timer
    timer += delta_t
    if timer > 0.25:
        timer = 0.0
        if error < 1:
            try:
                params = ac.ext_rainParams()
                ac.setText(rainStrengthValue, str(round(params[0], 1)))
                ac.setText(rainWiperSpeedValue, str(round(params[1], 1)))
            except:
                error+=1
                ac.log("AccExtRain: Shaders Patch not active?\n\n" + traceback.format_exc())
                # ac.setText(debug, "AccExtRain: Shaders Patch not active? : \n" + traceback.format_exc())

def acShutdown(*args):
    return

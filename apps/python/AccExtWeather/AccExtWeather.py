try:
    import ac
    import acsys
    import traceback
    import random
    import time
except ImportError:
    pass

app = 0
label = 0
timeOffsetMinusSmallerButton = 0
timeOffsetPlusSmallerButton = 0
timeOffsetMinusSmallButton = 0
timeOffsetPlusSmallButton = 0
timeOffsetMinusBigButton = 0
timeOffsetPlusBigButton = 0
timeOffsetMinusHugeButton = 0
timeOffsetPlusHugeButton = 0
timeOffsetMinusPlayButton = 0
timeOffsetPlusPlayButton = 0
timeOffsetMinusPlaySmallButton = 0
timeOffsetPlusPlaySmallButton = 0
error = 0
timer = 0

def acMain(ac_version):
    global app, label, stepBackButton
    global timeOffsetMinusSmallButton, timeOffsetPlusSmallButton, timeOffsetMinusBigButton, timeOffsetPlusBigButton, timeOffsetMinusHugeButton, timeOffsetPlusHugeButton, timeOffsetMinusPlayButton, timeOffsetPlusPlayButton
    global timeOffsetMinusSmallerButton, timeOffsetPlusSmallerButton, timeOffsetMinusPlaySmallButton, timeOffsetPlusPlaySmallButton
    global doorToggleButton, driverToggleButton

    try:
        app = ac.newApp("Shaders Patch Weather")
        ac.setTitle(app, "   Weather FX")
        ac.setSize(app, 420, 360)

        label = ac.addLabel(app, "")
        ac.setFontSize(label, 11)
        ac.setPosition(label, 5, 30)

        timeOffsetMinusSmallerButton = ac.addButton(app, "−5min")
        ac.setPosition(timeOffsetMinusSmallerButton, 8, 300)
        ac.setSize(timeOffsetMinusSmallerButton, 40, 22)
        ac.setFontSize(timeOffsetMinusSmallerButton, 14)
        ac.addOnClickedListener(timeOffsetMinusSmallerButton, timeOffsetMinusSmaller)

        timeOffsetPlusSmallerButton = ac.addButton(app, "+5min")
        ac.setPosition(timeOffsetPlusSmallerButton, 58, 300)
        ac.setSize(timeOffsetPlusSmallerButton, 40, 22)
        ac.setFontSize(timeOffsetPlusSmallerButton, 14)
        ac.addOnClickedListener(timeOffsetPlusSmallerButton, timeOffsetPlusSmaller)



        timeOffsetMinusSmallButton = ac.addButton(app, "−45min")
        ac.setPosition(timeOffsetMinusSmallButton, 8, 330)
        ac.setSize(timeOffsetMinusSmallButton, 40, 22)
        ac.setFontSize(timeOffsetMinusSmallButton, 14)
        ac.addOnClickedListener(timeOffsetMinusSmallButton, timeOffsetMinusSmall)

        timeOffsetPlusSmallButton = ac.addButton(app, "+45min")
        ac.setPosition(timeOffsetPlusSmallButton, 58, 330)
        ac.setSize(timeOffsetPlusSmallButton, 40, 22)
        ac.setFontSize(timeOffsetPlusSmallButton, 14)
        ac.addOnClickedListener(timeOffsetPlusSmallButton, timeOffsetPlusSmall)

        timeOffsetMinusBigButton = ac.addButton(app, "−6hr")
        ac.setPosition(timeOffsetMinusBigButton, 108, 330)
        ac.setSize(timeOffsetMinusBigButton, 40, 22)
        ac.setFontSize(timeOffsetMinusBigButton, 14)
        ac.addOnClickedListener(timeOffsetMinusBigButton, timeOffsetMinusBig)

        timeOffsetPlusBigButton = ac.addButton(app, "+6hr")
        ac.setPosition(timeOffsetPlusBigButton, 158, 330)
        ac.setSize(timeOffsetPlusBigButton, 40, 22)
        ac.setFontSize(timeOffsetPlusBigButton, 14)
        ac.addOnClickedListener(timeOffsetPlusBigButton, timeOffsetPlusBig)

        timeOffsetMinusHugeButton = ac.addButton(app, "−day")
        ac.setPosition(timeOffsetMinusHugeButton, 208, 330)
        ac.setSize(timeOffsetMinusHugeButton, 40, 22)
        ac.setFontSize(timeOffsetMinusHugeButton, 14)
        ac.addOnClickedListener(timeOffsetMinusHugeButton, timeOffsetMinusHuge)

        timeOffsetPlusHugeButton = ac.addButton(app, "+day")
        ac.setPosition(timeOffsetPlusHugeButton, 258, 330)
        ac.setSize(timeOffsetPlusHugeButton, 40, 22)
        ac.setFontSize(timeOffsetPlusHugeButton, 14)
        ac.addOnClickedListener(timeOffsetPlusHugeButton, timeOffsetPlusHuge)

        timeOffsetMinusPlayButton = ac.addButton(app, "- 10x")
        ac.setPosition(timeOffsetMinusPlayButton, 308, 330)
        ac.setSize(timeOffsetMinusPlayButton, 40, 22)
        ac.setFontSize(timeOffsetMinusPlayButton, 14)
        ac.addOnClickedListener(timeOffsetMinusPlayButton, timeOffsetMinusPlay)

        timeOffsetPlusPlayButton = ac.addButton(app, "+ 10x")
        ac.setPosition(timeOffsetPlusPlayButton, 358, 330)
        ac.setSize(timeOffsetPlusPlayButton, 40, 22)
        ac.setFontSize(timeOffsetPlusPlayButton, 14)
        ac.addOnClickedListener(timeOffsetPlusPlayButton, timeOffsetPlusPlay)

        timeOffsetMinusPlaySmallButton = ac.addButton(app, "- 2x")
        ac.setPosition(timeOffsetMinusPlaySmallButton, 308, 300)
        ac.setSize(timeOffsetMinusPlaySmallButton, 40, 22)
        ac.setFontSize(timeOffsetMinusPlaySmallButton, 14)
        ac.addOnClickedListener(timeOffsetMinusPlaySmallButton, timeOffsetMinusPlaySmall)

        timeOffsetPlusPlaySmallButton = ac.addButton(app, "+ 2x")
        ac.setPosition(timeOffsetPlusPlaySmallButton, 358, 300)
        ac.setSize(timeOffsetPlusPlaySmallButton, 40, 22)
        ac.setFontSize(timeOffsetPlusPlaySmallButton, 14)
        ac.addOnClickedListener(timeOffsetPlusPlaySmallButton, timeOffsetPlusPlaySmall)
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

def timeOffsetMinusSmaller(*args):
    try:
        ac.ext_weatherTimeOffset(-5 * 60)
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

def timeOffsetPlusSmaller(*args):
    try:
        ac.ext_weatherTimeOffset(5 * 60)
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

def timeOffsetMinusSmall(*args):
    try:
        ac.ext_weatherTimeOffset(-45 * 60)
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

def timeOffsetPlusSmall(*args):
    try:
        ac.ext_weatherTimeOffset(45 * 60)
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

def timeOffsetMinusBig(*args):
    try:
        ac.ext_weatherTimeOffset(-6 * 60 * 60)
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

def timeOffsetPlusBig(*args):
    try:
        ac.ext_weatherTimeOffset(6 * 60 * 60)
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

def timeOffsetMinusHuge(*args):
    try:
        ac.ext_weatherTimeOffset(-24 * 60 * 60)
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

def timeOffsetPlusHuge(*args):
    try:
        ac.ext_weatherTimeOffset(24 * 60 * 60)
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

speed = 0
day_offset = 0

def timeOffsetMinusPlay(*args):
    global speed
    speed -= 10

def timeOffsetPlusPlay(*args):
    global speed
    speed += 10

def timeOffsetMinusPlaySmall(*args):
    global speed
    speed -= 2

def timeOffsetPlusPlaySmall(*args):
    global speed
    speed += 2

def acUpdate(delta_t):
    global error, timer, day_offset
    timer += delta_t

    day_offset += speed * delta_t
    if abs(day_offset) > 1:
        try:
            ac.ext_weatherTimeOffset(24 * 60 * 60 * day_offset / abs(day_offset))
        except:
            ac.log("Unexpected error:" + traceback.format_exc())
        day_offset = 0

    if timer > 0.05:
        timer = 0.0
        try:
            ac.setText(label, ac.ext_weatherDebugText())
        except:
            if error < 10:
                ac.log("Unexpected error:" + traceback.format_exc())
            ac.setText(label, "Unexpected error:" + traceback.format_exc())

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
timeOffsetMinusMonthButton = 0
timeOffsetPlusMonthButton = 0
timeOffsetMinusYearButton = 0
timeOffsetPlusYearButton = 0
error = 0
timer = 0

def acMain(ac_version):
    global app, label, stepBackButton
    global timeOffsetMinusSmallButton, timeOffsetPlusSmallButton, timeOffsetMinusBigButton, timeOffsetPlusBigButton, timeOffsetMinusHugeButton, timeOffsetPlusHugeButton, timeOffsetMinusPlayButton, timeOffsetPlusPlayButton
    global timeOffsetMinusSmallerButton, timeOffsetPlusSmallerButton, timeOffsetMinusPlaySmallButton, timeOffsetPlusPlaySmallButton
    global timeOffsetMinusMonthButton, timeOffsetPlusMonthButton, timeOffsetMinusYearButton, timeOffsetPlusYearButton
    global doorToggleButton, driverToggleButton

    try:
        app = ac.newApp("Shaders Patch Weather")
        ac.setTitle(app, "   Weather FX")
        ac.setSize(app, 340, 360)

        label = ac.addLabel(app, "")
        ac.setFontSize(label, 11)
        ac.setPosition(label, 5, 30)

        timeOffsetMinusSmallerButton = ac.addButton(app, "−5min")
        ac.setPosition(timeOffsetMinusSmallerButton, 8, 303)
        ac.setSize(timeOffsetMinusSmallerButton, 50, 15)
        ac.setFontSize(timeOffsetMinusSmallerButton, 12)
        ac.addOnClickedListener(timeOffsetMinusSmallerButton, timeOffsetMinusSmaller)

        timeOffsetPlusSmallerButton = ac.addButton(app, "+5min")
        ac.setPosition(timeOffsetPlusSmallerButton, 58, 303)
        ac.setSize(timeOffsetPlusSmallerButton, 50, 15)
        ac.setFontSize(timeOffsetPlusSmallerButton, 12)
        ac.addOnClickedListener(timeOffsetPlusSmallerButton, timeOffsetPlusSmaller)

        timeOffsetMinusSmallButton = ac.addButton(app, "−45min")
        ac.setPosition(timeOffsetMinusSmallButton, 8, 320)
        ac.setSize(timeOffsetMinusSmallButton, 50, 15)
        ac.setFontSize(timeOffsetMinusSmallButton, 12)
        ac.addOnClickedListener(timeOffsetMinusSmallButton, timeOffsetMinusSmall)

        timeOffsetPlusSmallButton = ac.addButton(app, "+45min")
        ac.setPosition(timeOffsetPlusSmallButton, 58, 320)
        ac.setSize(timeOffsetPlusSmallButton, 50, 15)
        ac.setFontSize(timeOffsetPlusSmallButton, 12)
        ac.addOnClickedListener(timeOffsetPlusSmallButton, timeOffsetPlusSmall)

        timeOffsetMinusBigButton = ac.addButton(app, "−6hr")
        ac.setPosition(timeOffsetMinusBigButton, 8, 337)
        ac.setSize(timeOffsetMinusBigButton, 50, 15)
        ac.setFontSize(timeOffsetMinusBigButton, 12)
        ac.addOnClickedListener(timeOffsetMinusBigButton, timeOffsetMinusBig)

        timeOffsetPlusBigButton = ac.addButton(app, "+6hr")
        ac.setPosition(timeOffsetPlusBigButton, 58, 337)
        ac.setSize(timeOffsetPlusBigButton, 50, 15)
        ac.setFontSize(timeOffsetPlusBigButton, 12)
        ac.addOnClickedListener(timeOffsetPlusBigButton, timeOffsetPlusBig)



        timeOffsetMinusHugeButton = ac.addButton(app, "−day")
        ac.setPosition(timeOffsetMinusHugeButton, 118, 303)
        ac.setSize(timeOffsetMinusHugeButton, 50, 15)
        ac.setFontSize(timeOffsetMinusHugeButton, 12)
        ac.addOnClickedListener(timeOffsetMinusHugeButton, timeOffsetMinusHuge)

        timeOffsetPlusHugeButton = ac.addButton(app, "+day")
        ac.setPosition(timeOffsetPlusHugeButton, 168, 303)
        ac.setSize(timeOffsetPlusHugeButton, 50, 15)
        ac.setFontSize(timeOffsetPlusHugeButton, 12)
        ac.addOnClickedListener(timeOffsetPlusHugeButton, timeOffsetPlusHuge)

        timeOffsetMinusMonthButton = ac.addButton(app, "−month")
        ac.setPosition(timeOffsetMinusMonthButton, 118, 320)
        ac.setSize(timeOffsetMinusMonthButton, 50, 15)
        ac.setFontSize(timeOffsetMinusMonthButton, 12)
        ac.addOnClickedListener(timeOffsetMinusMonthButton, timeOffsetMinusMonth)

        timeOffsetPlusMonthButton = ac.addButton(app, "+month")
        ac.setPosition(timeOffsetPlusMonthButton, 168, 320)
        ac.setSize(timeOffsetPlusMonthButton, 50, 15)
        ac.setFontSize(timeOffsetPlusMonthButton, 12)
        ac.addOnClickedListener(timeOffsetPlusMonthButton, timeOffsetPlusMonth)

        timeOffsetMinusYearButton = ac.addButton(app, "−year")
        ac.setPosition(timeOffsetMinusYearButton, 118, 337)
        ac.setSize(timeOffsetMinusYearButton, 50, 15)
        ac.setFontSize(timeOffsetMinusYearButton, 12)
        ac.addOnClickedListener(timeOffsetMinusYearButton, timeOffsetMinusYear)

        timeOffsetPlusYearButton = ac.addButton(app, "+year")
        ac.setPosition(timeOffsetPlusYearButton, 168, 337)
        ac.setSize(timeOffsetPlusYearButton, 50, 15)
        ac.setFontSize(timeOffsetPlusYearButton, 12)
        ac.addOnClickedListener(timeOffsetPlusYearButton, timeOffsetPlusYear)




        timeOffsetMinusPlaySmallButton = ac.addButton(app, "- 1x")
        ac.setPosition(timeOffsetMinusPlaySmallButton, 228, 303)
        ac.setSize(timeOffsetMinusPlaySmallButton, 50, 15)
        ac.setFontSize(timeOffsetMinusPlaySmallButton, 12)
        ac.addOnClickedListener(timeOffsetMinusPlaySmallButton, timeOffsetMinusPlaySmall)

        timeOffsetPlusPlaySmallButton = ac.addButton(app, "+ 1x")
        ac.setPosition(timeOffsetPlusPlaySmallButton, 278, 303)
        ac.setSize(timeOffsetPlusPlaySmallButton, 50, 15)
        ac.setFontSize(timeOffsetPlusPlaySmallButton, 12)
        ac.addOnClickedListener(timeOffsetPlusPlaySmallButton, timeOffsetPlusPlaySmall)

        timeOffsetMinusPlayButton = ac.addButton(app, "- 10x")
        ac.setPosition(timeOffsetMinusPlayButton, 228, 320)
        ac.setSize(timeOffsetMinusPlayButton, 50, 15)
        ac.setFontSize(timeOffsetMinusPlayButton, 12)
        ac.addOnClickedListener(timeOffsetMinusPlayButton, timeOffsetMinusPlay)

        timeOffsetPlusPlayButton = ac.addButton(app, "+ 10x")
        ac.setPosition(timeOffsetPlusPlayButton, 278, 320)
        ac.setSize(timeOffsetPlusPlayButton, 50, 15)
        ac.setFontSize(timeOffsetPlusPlayButton, 12)
        ac.addOnClickedListener(timeOffsetPlusPlayButton, timeOffsetPlusPlay)

        timeOffsetMinusPlayBigButton = ac.addButton(app, "- 50x")
        ac.setPosition(timeOffsetMinusPlayBigButton, 228, 337)
        ac.setSize(timeOffsetMinusPlayBigButton, 50, 15)
        ac.setFontSize(timeOffsetMinusPlayBigButton, 12)
        ac.addOnClickedListener(timeOffsetMinusPlayBigButton, timeOffsetMinusBigPlay)

        timeOffsetPlusPlayBigButton = ac.addButton(app, "+ 50x")
        ac.setPosition(timeOffsetPlusPlayBigButton, 278, 337)
        ac.setSize(timeOffsetPlusPlayBigButton, 50, 15)
        ac.setFontSize(timeOffsetPlusPlayBigButton, 12)
        ac.addOnClickedListener(timeOffsetPlusPlayBigButton, timeOffsetPlusBigPlay)

        ac.setVisible(app,1)

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

def timeOffsetMinusMonth(*args):
    try:
        ac.ext_weatherTimeOffset(-30 * 24 * 60 * 60)
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

def timeOffsetPlusMonth(*args):
    try:
        ac.ext_weatherTimeOffset(30 * 24 * 60 * 60)
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

def timeOffsetMinusYear(*args):
    try:
        ac.ext_weatherTimeOffset(-365 * 24 * 60 * 60)
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

def timeOffsetPlusYear(*args):
    try:
        ac.ext_weatherTimeOffset(365 * 24 * 60 * 60)
    except:
        ac.log("Unexpected error:" + traceback.format_exc())


speed = 0
day_offset = 0

def timeOffsetMinusPlaySmall(*args):
    global speed
    speed -= 1

def timeOffsetPlusPlaySmall(*args):
    global speed
    speed += 1

def timeOffsetMinusPlay(*args):
    global speed
    speed -= 10

def timeOffsetPlusPlay(*args):
    global speed
    speed += 10

def timeOffsetMinusBigPlay(*args):
    global speed
    speed -= 50

def timeOffsetPlusBigPlay(*args):
    global speed
    speed += 50

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

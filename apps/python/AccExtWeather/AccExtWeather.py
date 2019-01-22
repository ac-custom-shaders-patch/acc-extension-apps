try:
    import ac
    import acsys
    import os
    import traceback
    import random
    import time
    import configparser
except ImportError:
    pass

# option
bIs4k = False

# vars
app = 0
label = 0
error = 0
timer = 0
sizeToggle = 0
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

settingsFilePath = "apps\\python\\AccExtWeather\\settings\\settings.ini"
documentSectionGeneral = "GENERAL"

def appCreateMyself():
    global app, label
    global timeOffsetMinusSmallButton, timeOffsetPlusSmallButton, timeOffsetMinusBigButton, timeOffsetPlusBigButton, timeOffsetMinusHugeButton, timeOffsetPlusHugeButton, timeOffsetMinusPlayButton, timeOffsetPlusPlayButton
    global timeOffsetMinusSmallerButton, timeOffsetPlusSmallerButton, timeOffsetMinusPlaySmallButton, timeOffsetPlusPlaySmallButton
    global timeOffsetMinusMonthButton, timeOffsetPlusMonthButton, timeOffsetMinusYearButton, timeOffsetPlusYearButton
    global sizeToggle
    global bIs4k

    mult=1
    dx=50
    dy=15
    fntsize=12
    if bIs4k==True:
        dx=100
        dy=30
        mult=2
        fntsize=16

    app = ac.newApp("Shaders Patch Weather")
    ac.setTitle(app, "   Weather FX")
    ac.setSize(app, 335*mult, 420*mult)

    # ac.setVisible(app,1)

    label = ac.addLabel(app, "")
    ac.setFontSize(label, fntsize-1)
    ac.setPosition(label, 10, dy*3+25)

    xpos=10
    ypos=25
    timeOffsetMinusSmallerButton = ac.addButton(app, "−5min")
    ac.setPosition(timeOffsetMinusSmallerButton, xpos, ypos)
    ac.setSize(timeOffsetMinusSmallerButton, 50*mult, dy-1)
    ac.setFontSize(timeOffsetMinusSmallerButton, fntsize)
    ac.addOnClickedListener(timeOffsetMinusSmallerButton, timeOffsetMinusSmaller)
    xpos+=dx
    timeOffsetPlusSmallerButton = ac.addButton(app, "+5min")
    ac.setPosition(timeOffsetPlusSmallerButton, xpos, ypos)
    ac.setSize(timeOffsetPlusSmallerButton, 50*mult, dy-1)
    ac.setFontSize(timeOffsetPlusSmallerButton, fntsize)
    ac.addOnClickedListener(timeOffsetPlusSmallerButton, timeOffsetPlusSmaller)
    xpos+=dx+10*mult
    timeOffsetMinusHugeButton = ac.addButton(app, "−day")
    ac.setPosition(timeOffsetMinusHugeButton, xpos, ypos)
    ac.setSize(timeOffsetMinusHugeButton, 50*mult, dy-1)
    ac.setFontSize(timeOffsetMinusHugeButton, fntsize)
    ac.addOnClickedListener(timeOffsetMinusHugeButton, timeOffsetMinusHuge)
    xpos+=dx
    timeOffsetPlusHugeButton = ac.addButton(app, "+day")
    ac.setPosition(timeOffsetPlusHugeButton, xpos, ypos)
    ac.setSize(timeOffsetPlusHugeButton, 50*mult, dy-1)
    ac.setFontSize(timeOffsetPlusHugeButton, fntsize)
    ac.addOnClickedListener(timeOffsetPlusHugeButton, timeOffsetPlusHuge)
    xpos+=dx+10*mult
    timeOffsetMinusPlaySmallButton = ac.addButton(app, "- 1x")
    ac.setPosition(timeOffsetMinusPlaySmallButton, xpos, ypos)
    ac.setSize(timeOffsetMinusPlaySmallButton, 50*mult, dy-1)
    ac.setFontSize(timeOffsetMinusPlaySmallButton, fntsize)
    ac.addOnClickedListener(timeOffsetMinusPlaySmallButton, timeOffsetMinusPlaySmall)
    xpos+=dx
    timeOffsetPlusPlaySmallButton = ac.addButton(app, "+ 1x")
    ac.setPosition(timeOffsetPlusPlaySmallButton, xpos, ypos)
    ac.setSize(timeOffsetPlusPlaySmallButton, 50*mult, dy-1)
    ac.setFontSize(timeOffsetPlusPlaySmallButton, fntsize)
    ac.addOnClickedListener(timeOffsetPlusPlaySmallButton, timeOffsetPlusPlaySmall)
    ac.setVisible(app,1)


    xpos=10
    ypos=25+dy
    timeOffsetMinusSmallButton = ac.addButton(app, "−45min")
    ac.setPosition(timeOffsetMinusSmallButton, xpos, ypos)
    ac.setSize(timeOffsetMinusSmallButton, 50*mult, dy-1)
    ac.setFontSize(timeOffsetMinusSmallButton, fntsize)
    ac.addOnClickedListener(timeOffsetMinusSmallButton, timeOffsetMinusSmall)
    xpos+=dx
    timeOffsetPlusSmallButton = ac.addButton(app, "+45min")
    ac.setPosition(timeOffsetPlusSmallButton, xpos, ypos)
    ac.setSize(timeOffsetPlusSmallButton, 50*mult, dy-1)
    ac.setFontSize(timeOffsetPlusSmallButton, fntsize)
    ac.addOnClickedListener(timeOffsetPlusSmallButton, timeOffsetPlusSmall)
    xpos+=dx+10*mult
    timeOffsetMinusMonthButton = ac.addButton(app, "−month")
    ac.setPosition(timeOffsetMinusMonthButton, xpos, ypos)
    ac.setSize(timeOffsetMinusMonthButton, 50*mult, dy-1)
    ac.setFontSize(timeOffsetMinusMonthButton, fntsize)
    ac.addOnClickedListener(timeOffsetMinusMonthButton, timeOffsetMinusMonth)
    xpos+=dx
    timeOffsetPlusMonthButton = ac.addButton(app, "+month")
    ac.setPosition(timeOffsetPlusMonthButton, xpos, ypos)
    ac.setSize(timeOffsetPlusMonthButton, 50*mult, dy-1)
    ac.setFontSize(timeOffsetPlusMonthButton, fntsize)
    ac.addOnClickedListener(timeOffsetPlusMonthButton, timeOffsetPlusMonth)
    xpos+=dx+10*mult
    timeOffsetMinusPlayButton = ac.addButton(app, "- 10x")
    ac.setPosition(timeOffsetMinusPlayButton, xpos, ypos)
    ac.setSize(timeOffsetMinusPlayButton, 50*mult, dy-1)
    ac.setFontSize(timeOffsetMinusPlayButton, fntsize)
    ac.addOnClickedListener(timeOffsetMinusPlayButton, timeOffsetMinusPlay)
    xpos+=dx
    timeOffsetPlusPlayButton = ac.addButton(app, "+ 10x")
    ac.setPosition(timeOffsetPlusPlayButton, xpos, ypos)
    ac.setSize(timeOffsetPlusPlayButton, 50*mult, dy-1)
    ac.setFontSize(timeOffsetPlusPlayButton, fntsize)
    ac.addOnClickedListener(timeOffsetPlusPlayButton, timeOffsetPlusPlay)


    xpos=10
    ypos=25+dy*2
    timeOffsetMinusBigButton = ac.addButton(app, "−6hr")
    ac.setPosition(timeOffsetMinusBigButton, xpos, ypos)
    ac.setSize(timeOffsetMinusBigButton, 50*mult, dy-1)
    ac.setFontSize(timeOffsetMinusBigButton, fntsize)
    ac.addOnClickedListener(timeOffsetMinusBigButton, timeOffsetMinusBig)
    xpos+=dx
    timeOffsetPlusBigButton = ac.addButton(app, "+6hr")
    ac.setPosition(timeOffsetPlusBigButton, xpos, ypos)
    ac.setSize(timeOffsetPlusBigButton, 50*mult, dy-1)
    ac.setFontSize(timeOffsetPlusBigButton, fntsize)
    ac.addOnClickedListener(timeOffsetPlusBigButton, timeOffsetPlusBig)
    xpos+=dx+10*mult
    timeOffsetMinusYearButton = ac.addButton(app, "−year")
    ac.setPosition(timeOffsetMinusYearButton, xpos, ypos)
    ac.setSize(timeOffsetMinusYearButton, 50*mult, dy-1)
    ac.setFontSize(timeOffsetMinusYearButton, fntsize)
    ac.addOnClickedListener(timeOffsetMinusYearButton, timeOffsetMinusYear)
    xpos+=dx
    timeOffsetPlusYearButton = ac.addButton(app, "+year")
    ac.setPosition(timeOffsetPlusYearButton, xpos, ypos)
    ac.setSize(timeOffsetPlusYearButton, 50*mult, dy-1)
    ac.setFontSize(timeOffsetPlusYearButton, fntsize)
    ac.addOnClickedListener(timeOffsetPlusYearButton, timeOffsetPlusYear)
    xpos+=dx+10*mult
    timeOffsetMinusPlayBigButton = ac.addButton(app, "- 50x")
    ac.setPosition(timeOffsetMinusPlayBigButton, xpos, ypos)
    ac.setSize(timeOffsetMinusPlayBigButton, 50*mult, dy-1)
    ac.setFontSize(timeOffsetMinusPlayBigButton, fntsize)
    ac.addOnClickedListener(timeOffsetMinusPlayBigButton, timeOffsetMinusBigPlay)
    xpos+=dx
    timeOffsetPlusPlayBigButton = ac.addButton(app, "+ 50x")
    ac.setPosition(timeOffsetPlusPlayBigButton, xpos, ypos)
    ac.setSize(timeOffsetPlusPlayBigButton, 50*mult, dy-1)
    ac.setFontSize(timeOffsetPlusPlayBigButton, fntsize)
    ac.addOnClickedListener(timeOffsetPlusPlayBigButton, timeOffsetPlusBigPlay)

def getSettingsValue(parser, section, option, value, boolean = False):
    if parser.has_option(str(section), str(option)):
        if boolean:
            return parser.getboolean(str(section), option)
        else:
            return parser.get(str(section), str(option))
    else:
        return setSettingsValue(parser, section, option, value)

def appReadSettings():
    global bIs4k, settingsFilePath, documentSectionGeneral
    try:
        if not os.path.isfile(settingsFilePath):
            with open(settingsFilePath, "w") as sf:
                ac.log("AccExtWeatherFX: Settings file created")
        settingsParser = configparser.ConfigParser()
        settingsParser.optionxform = str
        settingsParser.read(settingsFilePath)
        bIs4k = getSettingsValue(settingsParser, documentSectionGeneral, "uiDoubleSized", False, True)
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
    if timer > 0.05:
        timer = 0.0
        if abs(day_offset) > 1:
            try:
                ac.ext_weatherTimeOffset(24 * 60 * 60 * day_offset / abs(day_offset))
            except:
                ac.log("Unexpected error:" + traceback.format_exc())
            day_offset = 0
        try:
            ac.setText(label, ac.ext_weatherDebugText())
        except:
            if error < 10:
                ac.log("Unexpected error:" + traceback.format_exc())
            ac.setText(label, "Unexpected error:" + traceback.format_exc())

def acMain(ac_version):
    try:
        appReadSettings()
        appCreateMyself()
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

def acShutdown(*args):
    ac.removeItem(app)

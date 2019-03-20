# AccExtWeather.py - by x4fab, leBluem, Blamer, demonized
# v.99 - added time acceleration by demonized
# v1 - format
# v1.1 added reading start multiplier from race.ini, added 5x buttons
# v1.2+3 silly error corrections, only work with offset, not real values...
# v1.4 added stop time button, added "Hide title option" in CM, performance fixes
# v1.5 + and - time buttons fixed with time accel, days/s and weeks/s behaviour fixed

sVer = "1.5"

try:
    import ac
    import acsys
    import os
    import platform
    import traceback
    import random
    import time
    import configparser
    import re
    import threading
except ImportError:
    pass

# options read from
settingsFilePath = "apps\\python\\AccExtWeather\\settings\\settings.ini"
documentSectionGeneral = "GENERAL"
gWrapDebugText = False
gHideBG = False
gHideWeather = False
gAppsize = 1.0
gAppShowOnStart = False
gHideTitle = False

# vars
app = 0
label = 0
labeldate = 0
error = 0
timer = 0
speed = 0
day_offset = 0
accel = 0
accel_offset = 0
accel_orig = 0
t = 0

#buttons
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
timeAccelUpButton = 0
timeAccelDownButton = 0
timeAccelUpFasterButton = 0
timeAccelDownFasterButton = 0
timeAccelResetButton = 0
timeAccelStopButton = 0

def appCreateMyself():
    global app, label, labeldate
    global timeOffsetMinusSmallButton, timeOffsetPlusSmallButton, timeOffsetMinusBigButton, timeOffsetPlusBigButton, timeOffsetMinusHugeButton, timeOffsetPlusHugeButton, timeOffsetMinusPlayButton, timeOffsetPlusPlayButton
    global timeOffsetMinusSmallerButton, timeOffsetPlusSmallerButton, timeOffsetMinusPlaySmallButton, timeOffsetPlusPlaySmallButton
    global timeOffsetMinusMonthButton, timeOffsetPlusMonthButton, timeOffsetMinusYearButton, timeOffsetPlusYearButton
    global timeAccelDownButton, timeAccelUpButton, timeAccelUpFasterButton, timeAccelDownFasterButton, timeAccelResetButton, timeAccelStopButton
    global sizeToggle, gAppsize, gHideBG, gHideWeather, gAppShowOnStart, gHideTitle

    xpos=10
    dx=50
    dy=16
    yposBase=35
    fntsize=12
    mult=1.0
    if gAppsize>=0.5 and gAppsize<=4.0:
        mult=gAppsize
        dx=dx*mult
        dy=dy*mult
        fntsize=fntsize*mult

    app = ac.newApp("Shaders Patch Weather")
    if gHideWeather==True:
        ac.setSize(app, 360*mult, 120*mult)
    else:
        ac.setSize(app, 360*mult, 420*mult)

    if gAppShowOnStart==True:
        ac.setVisible(app,1)

    if gHideTitle==True:
        ac.setTitle(app, "")
        ac.setIconPosition(app, 0, -20000)
        yposBase=10
    else:
        try:
            ac.setTitle(app, "  WeatherFX " + sVer + " - patch "+str(ac.ext_patchVersion()))
        except:
            ac.setTitle(app, "  !Weather FX not active")
    ypos=yposBase

    label = ac.addLabel(app, "")
    ac.setFontSize(label, fntsize-1)
    ac.setPosition(label, 10, ypos+dy*4+2)

    timeOffsetMinusSmallerButton = ac.addButton(app, "−5min")
    ac.setPosition(timeOffsetMinusSmallerButton, xpos, ypos)
    ac.setSize(timeOffsetMinusSmallerButton, dx*mult, dy-1)
    ac.setFontSize(timeOffsetMinusSmallerButton, fntsize)
    ac.addOnClickedListener(timeOffsetMinusSmallerButton, timeOffsetMinusSmaller)
    xpos+=dx
    timeOffsetPlusSmallerButton = ac.addButton(app, "+5min")
    ac.setPosition(timeOffsetPlusSmallerButton, xpos, ypos)
    ac.setSize(timeOffsetPlusSmallerButton, dx*mult, dy-1)
    ac.setFontSize(timeOffsetPlusSmallerButton, fntsize)
    ac.addOnClickedListener(timeOffsetPlusSmallerButton, timeOffsetPlusSmaller)
    xpos+=dx+5*mult
    timeOffsetMinusHugeButton = ac.addButton(app, "−day")
    ac.setPosition(timeOffsetMinusHugeButton, xpos, ypos)
    ac.setSize(timeOffsetMinusHugeButton, dx*mult, dy-1)
    ac.setFontSize(timeOffsetMinusHugeButton, fntsize)
    ac.addOnClickedListener(timeOffsetMinusHugeButton, timeOffsetMinusHuge)
    xpos+=dx
    timeOffsetPlusHugeButton = ac.addButton(app, "+day")
    ac.setPosition(timeOffsetPlusHugeButton, xpos, ypos)
    ac.setSize(timeOffsetPlusHugeButton, dx*mult, dy-1)
    ac.setFontSize(timeOffsetPlusHugeButton, fntsize)
    ac.addOnClickedListener(timeOffsetPlusHugeButton, timeOffsetPlusHuge)
    xpos+=dx+15*mult
    timeAccelDownButton = ac.addButton(app, "- 1x")
    ac.setPosition(timeAccelDownButton, xpos, ypos)
    ac.setSize(timeAccelDownButton, dx * mult, dy - 1)
    ac.setFontSize(timeAccelDownButton, fntsize)
    ac.addOnClickedListener(timeAccelDownButton, timeAccelDown)
    xpos+=dx
    timeAccelUpButton = ac.addButton(app, "+ 1x")
    ac.setPosition(timeAccelUpButton, xpos, ypos)
    ac.setSize(timeAccelUpButton, dx * mult, dy - 1)
    ac.setFontSize(timeAccelUpButton, fntsize)
    ac.addOnClickedListener(timeAccelUpButton, timeAccelUp)

    xpos=10
    ypos=yposBase+dy
    timeOffsetMinusSmallButton = ac.addButton(app, "−45min")
    ac.setPosition(timeOffsetMinusSmallButton, xpos, ypos)
    ac.setSize(timeOffsetMinusSmallButton, dx*mult, dy-1)
    ac.setFontSize(timeOffsetMinusSmallButton, fntsize)
    ac.addOnClickedListener(timeOffsetMinusSmallButton, timeOffsetMinusSmall)
    xpos+=dx
    timeOffsetPlusSmallButton = ac.addButton(app, "+45min")
    ac.setPosition(timeOffsetPlusSmallButton, xpos, ypos)
    ac.setSize(timeOffsetPlusSmallButton, dx*mult, dy-1)
    ac.setFontSize(timeOffsetPlusSmallButton, fntsize)
    ac.addOnClickedListener(timeOffsetPlusSmallButton, timeOffsetPlusSmall)
    xpos+=dx+5*mult
    timeOffsetMinusMonthButton = ac.addButton(app, "−month")
    ac.setPosition(timeOffsetMinusMonthButton, xpos, ypos)
    ac.setSize(timeOffsetMinusMonthButton, dx*mult, dy-1)
    ac.setFontSize(timeOffsetMinusMonthButton, fntsize)
    ac.addOnClickedListener(timeOffsetMinusMonthButton, timeOffsetMinusMonth)
    xpos+=dx
    timeOffsetPlusMonthButton = ac.addButton(app, "+month")
    ac.setPosition(timeOffsetPlusMonthButton, xpos, ypos)
    ac.setSize(timeOffsetPlusMonthButton, dx*mult, dy-1)
    ac.setFontSize(timeOffsetPlusMonthButton, fntsize)
    ac.addOnClickedListener(timeOffsetPlusMonthButton, timeOffsetPlusMonth)
    xpos+=dx+15*mult
    timeAccelDownFasterButton = ac.addButton(app, "- 20x")
    ac.setPosition(timeAccelDownFasterButton, xpos, ypos)
    ac.setSize(timeAccelDownFasterButton, dx * mult, dy - 1)
    ac.setFontSize(timeAccelDownFasterButton, fntsize)
    ac.addOnClickedListener(timeAccelDownFasterButton, timeAccelDownFaster)
    xpos+=dx
    timeAccelUpFasterButton = ac.addButton(app, "+ 20x")
    ac.setPosition(timeAccelUpFasterButton, xpos, ypos)
    ac.setSize(timeAccelUpFasterButton, dx * mult, dy - 1)
    ac.setFontSize(timeAccelUpFasterButton, fntsize)
    ac.addOnClickedListener(timeAccelUpFasterButton, timeAccelUpFaster)

    xpos=10
    ypos=yposBase+dy*2
    timeOffsetMinusBigButton = ac.addButton(app, "−6hr")
    ac.setPosition(timeOffsetMinusBigButton, xpos, ypos)
    ac.setSize(timeOffsetMinusBigButton, dx*mult, dy-1)
    ac.setFontSize(timeOffsetMinusBigButton, fntsize)
    ac.addOnClickedListener(timeOffsetMinusBigButton, timeOffsetMinusBig)
    xpos+=dx
    timeOffsetPlusBigButton = ac.addButton(app, "+6hr")
    ac.setPosition(timeOffsetPlusBigButton, xpos, ypos)
    ac.setSize(timeOffsetPlusBigButton, dx*mult, dy-1)
    ac.setFontSize(timeOffsetPlusBigButton, fntsize)
    ac.addOnClickedListener(timeOffsetPlusBigButton, timeOffsetPlusBig)
    xpos+=dx+5*mult
    timeOffsetMinusYearButton = ac.addButton(app, "−year")
    ac.setPosition(timeOffsetMinusYearButton, xpos, ypos)
    ac.setSize(timeOffsetMinusYearButton, dx*mult, dy-1)
    ac.setFontSize(timeOffsetMinusYearButton, fntsize)
    ac.addOnClickedListener(timeOffsetMinusYearButton, timeOffsetMinusYear)
    xpos+=dx
    timeOffsetPlusYearButton = ac.addButton(app, "+year")
    ac.setPosition(timeOffsetPlusYearButton, xpos, ypos)
    ac.setSize(timeOffsetPlusYearButton, dx*mult, dy-1)
    ac.setFontSize(timeOffsetPlusYearButton, fntsize)
    ac.addOnClickedListener(timeOffsetPlusYearButton, timeOffsetPlusYear)
    xpos+=dx+15*mult
    timeOffsetMinusPlaySmallButton = ac.addButton(app, "-days/s")
    ac.setPosition(timeOffsetMinusPlaySmallButton, xpos, ypos)
    ac.setSize(timeOffsetMinusPlaySmallButton, dx*mult, dy-1)
    ac.setFontSize(timeOffsetMinusPlaySmallButton, fntsize)
    ac.addOnClickedListener(timeOffsetMinusPlaySmallButton, timeOffsetMinusPlaySmall)
    xpos+=dx
    timeOffsetPlusPlaySmallButton = ac.addButton(app, "+days/s")
    ac.setPosition(timeOffsetPlusPlaySmallButton, xpos, ypos)
    ac.setSize(timeOffsetPlusPlaySmallButton, dx*mult, dy-1)
    ac.setFontSize(timeOffsetPlusPlaySmallButton, fntsize)
    ac.addOnClickedListener(timeOffsetPlusPlaySmallButton, timeOffsetPlusPlaySmall)

    xpos -= dx
    ypos=yposBase+dy*3
    timeOffsetMinusPlayButton = ac.addButton(app, "-weeks/s")
    ac.setPosition(timeOffsetMinusPlayButton, xpos, ypos)
    ac.setSize(timeOffsetMinusPlayButton, dx*mult, dy-1)
    ac.setFontSize(timeOffsetMinusPlayButton, fntsize)
    ac.addOnClickedListener(timeOffsetMinusPlayButton, timeOffsetMinusPlay)
    xpos += dx
    timeOffsetPlusPlayButton = ac.addButton(app, "+weeks/s")
    ac.setPosition(timeOffsetPlusPlayButton, xpos, ypos)
    ac.setSize(timeOffsetPlusPlayButton, dx*mult, dy-1)
    ac.setFontSize(timeOffsetPlusPlayButton, fntsize)
    ac.addOnClickedListener(timeOffsetPlusPlayButton, timeOffsetPlusPlay)

    xpos -= dx*2 + dx / 3 * 2 + 15
    dx = dx / 3 * 2
    ypos=yposBase+dy*3
    timeAccelStopButton = ac.addButton(app, "stop")
    ac.setPosition(timeAccelStopButton, xpos, ypos)
    ac.setSize(timeAccelStopButton, dx * mult, dy - 1)
    ac.setFontSize(timeAccelStopButton, fntsize)
    ac.addOnClickedListener(timeAccelStopButton, timeAccelStop)
    xpos += dx
    timeAccelResetButton = ac.addButton(app, "reset")
    ac.setPosition(timeAccelResetButton, xpos, ypos)
    ac.setSize(timeAccelResetButton, dx * mult, dy - 1)
    ac.setFontSize(timeAccelResetButton, fntsize)
    ac.addOnClickedListener(timeAccelResetButton, timeAccelReset)


def return_accel(temp):
    global accel_offset
    time.sleep(3)
    accel_offset = temp

def set_offset(offset):
    global accel_offset, t
    try:
        temp = accel_offset
        accel_offset = 0
        ac.ext_weatherTimeOffset(offset)
        if not t or not t.is_alive():
            t = threading.Thread(target=return_accel, args=(temp,))
            t.start()
    except:
        ac.log("AccExtWeatherFX: Unexpected error:" + traceback.format_exc())

def timeOffsetMinusSmaller(*args):
    set_offset(-300)

def timeOffsetPlusSmaller(*args):
    set_offset(300)

def timeOffsetMinusSmall(*args):
    set_offset(-2700)

def timeOffsetPlusSmall(*args):
    set_offset(2700)

def timeOffsetMinusBig(*args):
    set_offset(-21600)

def timeOffsetPlusBig(*args):
    set_offset(21600)

def timeOffsetMinusHuge(*args):
    try:
        ac.ext_weatherTimeOffset(-24 * 60 * 60)
    except:
        ac.log("AccExtWeatherFX: Unexpected error:" + traceback.format_exc())

def timeOffsetPlusHuge(*args):
    try:
        ac.ext_weatherTimeOffset(24 * 60 * 60)
    except:
        ac.log("AccExtWeatherFX: Unexpected error:" + traceback.format_exc())

def timeOffsetMinusMonth(*args):
    try:
        ac.ext_weatherTimeOffset(-30 * 24 * 60 * 60)
    except:
        ac.log("AccExtWeatherFX: Unexpected error:" + traceback.format_exc())

def timeOffsetPlusMonth(*args):
    try:
        ac.ext_weatherTimeOffset(30 * 24 * 60 * 60)
    except:
        ac.log("AccExtWeatherFX: Unexpected error:" + traceback.format_exc())

def timeOffsetMinusYear(*args):
    try:
        ac.ext_weatherTimeOffset(-365 * 24 * 60 * 60)
    except:
        ac.log("AccExtWeatherFX: Unexpected error:" + traceback.format_exc())

def timeOffsetPlusYear(*args):
    try:
        ac.ext_weatherTimeOffset(365 * 24 * 60 * 60)
    except:
        ac.log("AccExtWeatherFX: Unexpected error:" + traceback.format_exc())

def timeOffsetMinusPlaySmall(*args):
    global speed
    speed -= 1

def timeOffsetPlusPlaySmall(*args):
    global speed
    speed += 1

def timeOffsetMinusPlay(*args):
    global speed
    speed -= 7

def timeOffsetPlusPlay(*args):
    global speed
    speed += 7

def timeAccelDown(*args):
    global accel, accel_offset
    accel -= 1
    accel_offset = accel / 2

def timeAccelUp(*args):
    global accel, accel_offset
    accel += 1
    accel_offset = accel / 2

def timeAccelDownFaster(*args):
    global accel, accel_offset
    accel -= 20
    accel_offset = accel / 2

def timeAccelUpFaster(*args):
    global accel, accel_offset
    accel += 20
    accel_offset = accel / 2

def timeAccelStop(*args):
    global accel, speed, accel_offset, accel_orig
    accel = -accel_orig
    speed = 0
    accel_offset = accel / 2
    ac.ext_weatherTimeOffset(accel)

def timeAccelReset(*args):
    global accel, speed, accel_offset
    accel = 0
    speed = 0
    accel_offset = 0
    ac.ext_weatherTimeOffset(0)

def getSettingsValue(parser, section, option, value, boolean = False):
    if parser.has_option(str(section), str(option)):
        if boolean:
            return parser.getboolean(str(section), option)
        else:
            return parser.get(str(section), str(option))
    else:
        return str(value)

def appReadSettings():
    global settingsFilePath, documentSectionGeneral
    global gWrapDebugText, gAppsize, gHideBG, gHideWeather, gAppShowOnStart, gHideTitle
    try:
        if not os.path.isfile(settingsFilePath):
            with open(settingsFilePath, "w") as sf:
                ac.log("AccExtWeatherFX: Settings file created")
        settingsParser = configparser.ConfigParser()
        settingsParser.optionxform = str
        settingsParser.read(settingsFilePath)
        gWrapDebugText = getSettingsValue(settingsParser, documentSectionGeneral, "uiWrapDebugText", False, True)
        gHideBG = getSettingsValue(settingsParser, documentSectionGeneral, "uiHideBG", False, True)
        gHideWeather = getSettingsValue(settingsParser, documentSectionGeneral, "uiHideWeather", False, True)
        gAppShowOnStart = getSettingsValue(settingsParser, documentSectionGeneral, "uiShowOnStart", False, True)
        gAppsize = float(getSettingsValue(settingsParser, documentSectionGeneral, "uiSize", "1.0", False))
        gHideTitle = getSettingsValue(settingsParser, documentSectionGeneral, "uiHideTitle", False, True)
    except:
        ac.log("AccExtWeatherFX: Unexpected error:" + traceback.format_exc())

def acUpdate(delta_t):
    global error, timer, speed, day_offset, gWrapDebugText, gAppsize, gHideBG, gHideWeather, accel_offset, accel, accel_orig
    local_gHideWeather = gHideWeather
    timer += delta_t
    day_offset += speed * delta_t
    try:
        if (accel_offset != 0):
            ac.ext_weatherTimeOffset(accel_offset)
        if abs(day_offset) > 1:
            ac.ext_weatherTimeOffset(24 * 60 * 60 * day_offset / abs(day_offset))
            day_offset = 0

        if timer > 0.1:
            timer = 0.0

            s = ac.ext_weatherDebugText()
            s = s.replace('current day:', '> current day:    ')
            s = s.replace('\n\n', '\n')
            ss = s.split('\n')

            # pick 'current day' line
            idx = -1
            for sss in ss:
                idx+=1
                if 'current day' in sss:
                    break
            if idx>=0:
                ss[idx] = ss[idx] + '    time: ' + str(round(accel_orig + accel,3)) + 'x  -  ' + str(round(speed,3)) + ' days/sec'
            s = '\n'.join(s for s in ss)

            if gWrapDebugText==True:
                s = '\n'.join(s.strip() for s in re.findall(r'.{1,80}(?:\s+|$)', s))
                s = s.replace('>>> Sol weather: v', '\n>>> Sol weather: v')

            if 'error' in s: # if error, dont hide anything
                local_gHideWeather = False

            if local_gHideWeather==True:
                # only pick first line and 'current day'
                if idx>=0:
                    s = ss[0] + '\n' + ss[idx]

            ac.setText(label, s)
    except:
        ac.setText(label, "\nShaders Patch not installed! -OR-\n\Weather FX not active!")

    if gHideBG==True:
        ac.setBackgroundOpacity(app,0)
        ac.drawBorder(app,0)

def appReadTimeMultiplier():
    global app, label
    global accel, accel_offset, accel_orig
    INIrace = os.path.expanduser(r"~\Documents\Assetto Corsa\cfg\race.ini")
    config = configparser.ConfigParser()
    config.optionxform = str
    config.read(INIrace)
    try:
        for section in config:
            if section=="LIGHTING":
                for key, value in config.items(section):
                    if key=="TIME_MULT":
                        accel_orig = int(float(value))
    except:
        ac.log("AccExtWeatherFX: Unexpected error:" + traceback.format_exc())
    return

def acMain(ac_version):
    try:
        appReadSettings()
        appCreateMyself()
        appReadTimeMultiplier()
    except:
        ac.log("AccExtWeatherFX: Unexpected error:" + traceback.format_exc())
    return "AccExtWeather"

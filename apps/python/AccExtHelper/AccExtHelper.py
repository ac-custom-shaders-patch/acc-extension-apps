try:
    import ac
    import acsys
    import sys
    import os.path
    import platform
    import time
    import subprocess
    import traceback
except ImportError:
    pass

if platform.architecture()[0] == "64bit":
    sysdir=os.path.dirname(__file__)+'/stdlib64'
else:
    sysdir=os.path.dirname(__file__)+'/stdlib'
sys.path.insert(0, sysdir)
os.environ['PATH'] = os.environ['PATH'] + ";."
import ctypes, ctypes.wintypes

from sim_info import info

app = 0
label = 0
stepBackButton = 0
resetButton = 0
vaoToggleButton = 0
vaoDebugButton = 0
lightsDebugButton = 0
copyCameraCoordsButton = 0
doorToggleButton = 0
driverToggleButton = 0
isVaoActive = True
currentVaoDebugMode = 0
isLightsDebugOn = False
areDoorsOpen = False
isDriverVisible = True
lastFrom = ""
error = 0
timer = 0

# global variables
rstButton = 0
tick_counter = 0
max_tick = 360
# frames/second variables
frame_counter = 0
frame_buffer = 20
time_elapsed = 0
current_fps = 0
# min max counter
MAX_fps = 0
MIN_fps = 5000
MAX_lights = 0
MIN_lights = 100000
odd = True
lx = 0.0
ly = 0.0
lz = 0.0

def acMain(ac_version):
    global app, label, stepBackButton, resetButton, sVer
    global vaoToggleButton, vaoDebugButton, lightsDebugButton, copyCameraCoordsButton
    global doorToggleButton, driverToggleButton

    try:
        app = ac.newApp("Shaders Patch Debug")
        ac.setTitle(app, "  Shaders Patch Debug")
        ac.setSize(app, 180, 358)

        driverToggleButton = ac.addButton(app, "Driver")
        ac.setPosition(driverToggleButton, 20, 25)
        ac.setSize(driverToggleButton, 40, 20)
        ac.setFontSize(driverToggleButton, 12)
        ac.addOnClickedListener(driverToggleButton, driverToggle)

        doorToggleButton = ac.addButton(app, "🚪")
        ac.setPosition(doorToggleButton, 70, 25)
        ac.setCustomFont(doorToggleButton, "Segoe UI Symbol; Weight=UltraLight", 0, 0)
        ac.setSize(doorToggleButton, 40, 20)
        ac.setFontSize(doorToggleButton, 14)
        ac.addOnClickedListener(doorToggleButton, doorToggle)

        copyCameraCoordsButton = ac.addButton(app, "Copy")
        ac.setPosition(copyCameraCoordsButton, 120, 25)
        ac.setSize(copyCameraCoordsButton, 40, 20)
        ac.setFontSize(copyCameraCoordsButton, 12)
        ac.addOnClickedListener(copyCameraCoordsButton, copyCameraCoords)

        vaoToggleButton = ac.addButton(app, "V +/−")
        ac.setPosition(vaoToggleButton, 20, 45)
        ac.setSize(vaoToggleButton, 40, 20)
        ac.setFontSize(vaoToggleButton, 12)
        ac.addOnClickedListener(vaoToggleButton, vaoToggle)

        vaoDebugButton = ac.addButton(app, "V o/N")
        ac.setPosition(vaoDebugButton, 70, 45)
        ac.setSize(vaoDebugButton, 40, 20)
        ac.setFontSize(vaoDebugButton, 12)
        ac.addOnClickedListener(vaoDebugButton, vaoDebug)

        lightsDebugButton = ac.addButton(app, "🔦")
        ac.setPosition(lightsDebugButton, 120, 45)
        ac.setSize(lightsDebugButton, 40, 20)
        ac.setFontSize(lightsDebugButton, 14)
        ac.addOnClickedListener(lightsDebugButton, lightsDebug)

        stepBackButton = ac.addButton(app, "Step back")
        ac.setPosition(stepBackButton, 20, 65)
        ac.setSize(stepBackButton, 140, 20)
        ac.setFontSize(stepBackButton, 12)
        ac.addOnClickedListener(stepBackButton, takeAStepBack)
        ac.setCustomFont(stepBackButton, "Segoe UI; Weight=UltraBlack", 0, 0)

        resetButton = ac.addButton(app, "Reset")
        ac.setPosition(resetButton, 20, 85)
        ac.setSize(resetButton, 140, 20)
        ac.setFontSize(resetButton, 12)
        ac.addOnClickedListener(resetButton, resetCar)
        ac.setCustomFont(resetButton, "Segoe UI; Weight=UltraBlack", 0, 0)

        label = ac.addLabel(app, "")
        ac.setFontSize(label, 12)
        ac.setPosition(label, 5, 103)

        ac.drawBackground(app,0)

        sVer = "CSP v" + str(ac.ext_patchVersion()) + "-code" + str(ac.ext_patchVersionCode())
        # i = 0
        # while i < 1200:
        #     labelTemp = ac.setPosition(ac.addLabel(app, "Label #" + str(i)), 5, 30 + i)
        #     ac.setFontSize(labelTemp, 14 + (i % 10))
        #     i += 1
    except:
        ac.log("Unexpected error:" + traceback.format_exc())
    return "AccExtHelper"

def doorToggle(*args):
    global areDoorsOpen
    try:
        areDoorsOpen = not areDoorsOpen
        ac.ext_setDoorsOpen(areDoorsOpen)
        ac.ext_setTrackConditionInput('CAR_DOORS_OPENED', 1.0 if areDoorsOpen else 0.0)
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

def driverToggle(*args):
    global isDriverVisible
    try:
        isDriverVisible = not isDriverVisible
        ac.ext_setDriverVisible(isDriverVisible)
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

def vaoToggle(*args):
    global isVaoActive, currentVaoDebugMode
    try:
        isVaoActive = not isVaoActive
        currentVaoDebugMode = 0
        ac.ext_setVaoActive(isVaoActive)
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

def vaoDebug(*args):
    global isVaoActive, currentVaoDebugMode
    try:
        isVaoActive = False
        if currentVaoDebugMode == 1:
            ac.ext_vaoNormalDebug()
            currentVaoDebugMode = 2
        else:
            ac.ext_vaoOnly()
            currentVaoDebugMode = 1
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

class LightsDebugMode:
    Off = 0
    Outline = 1
    BoundingBox = 2
    BoundingSphere = 4
    Text = 8

def lightsDebug(*args):
    global isLightsDebugOn
    try:
        isLightsDebugOn = not isLightsDebugOn
        if isLightsDebugOn:
            lightsDebugCount = 20
            lightsDebugDistance = 200.0
            lightsDebugMode = LightsDebugMode.Outline | LightsDebugMode.BoundingBox
            # | LightsDebugMode.Text
            ac.ext_debugLights("?", lightsDebugCount, lightsDebugDistance, lightsDebugMode)
        else:
            ac.ext_debugLights("?", 0, 0, 0)
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

class ApplyTrackConfigFlags:
    Nothing = 0
    RestoreConditionsState = 1

def resetCar(*args):
    try:
        ac.log("resetCar()")
        ac.ext_resetCar()
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

def takeAStepBack(*args):
    try:
        ac.ext_takeAStepBack()
        # ac.ext_debugFn()
        # ac.ext_setCameraFov(30)
#         lightsDebugCount = 10
#         lightsDebugMode = LightsDebugMode.Outline | LightsDebugMode.BoundingBox | LightsDebugMode.Text
#         ac.ext_debugLights("?", lightsDebugCount, lightsDebugMode)

#         ac.ext_applyTrackConfig("[LIGHT_SERIES_0]\n\
# MESHES=Object345\n\
# DESCRIPTION=Pits\n\
# OFFSET=0,1.35,-1.2\n\
# CLUSTER_THRESHOLD=4\n\
# COLOR=" + str(random.randrange(1, 3)) + ", 1.2, 1, 4\n\
# SPOT=110\n\
# RANGE=10\n\
# FADE_AT=150\n\
# FADE_SMOOTH=50\n\
# SPOT_SHARPNESS=0.7\n\
# DIRECTION=0,-1,0\n\
# COLOR_OFF=1.2, 1.2, 0.8, 0\n\
# CONDITION=NIGHT_SHARP\n\
# \n\
# [LIGHT_SERIES_1]\n\
# MATERIALS=light_emissive\n\
# DESCRIPTION=Starting lane spotlghts\n\
# OFFSET=0,0,0\n\
# CLUSTER_THRESHOLD=8\n\
# COLOR=0.8, 0.8, 1, " + str(random.randrange(5, 25)) + "\n\
# SPOT=150\n\
# RANGE=35\n\
# RANGE_GRADIENT_OFFSET=0.6\n\
# FADE_AT=400\n\
# FADE_SMOOTH=10\n\
# SPOT_SHARPNESS=0.7\n\
# DIRECTION=NORMAL\n\
# CONDITION=NIGHT_SMOOTH_HEATING\n\
# SINGLE_FREQUENCY=0", ApplyTrackConfigFlags.RestoreConditionsState)
        ac.log("takeAStepBack() called")
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

def __init__():
    global tick_counter, max_tick, frame_counter, frame_buffer, time_elapsed, current_fps, MAX_fps, MIN_fps, MAX_lights, MIN_lights
    # global variables
    tick_counter = 0
    max_tick = 360
    # frames/second variables
    frame_counter = 0
    frame_buffer = 20
    time_elapsed = 0
    current_fps = 0
    MAX_fps = 0
    MIN_fps = 5000
    MAX_lights = 0
    MIN_lights = 100000

def doReset(*args):
    __init__()

def get_frames_per_second(deltaT):
    global tick_counter, max_tick, frame_counter, frame_buffer, time_elapsed, current_fps, MAX_fps, MIN_fps, MAX_lights, MIN_lights
    frame_counter += 1
    time_elapsed += deltaT
    if frame_counter == frame_buffer:
        # calculating frames per second
        current_fps = frame_buffer / time_elapsed
        if current_fps>MAX_fps:
            MAX_fps=current_fps
        if current_fps<MIN_fps:
            MIN_fps=current_fps
        # calculating max_tick for animations
        # number of fps multiplied by 3 seconds
        max_tick = current_fps * 3 if current_fps * 3 > 30 else 30
        # reseting counters
        frame_counter = 0
        time_elapsed = 0

def acShutdown(*args):
    return

def acUpdate(delta_t):
    global error
    global timer
    global info
    global tick_counter, max_tick, frame_counter, frame_buffer, time_elapsed, current_fps, MAX_fps, MIN_fps, MAX_lights, MIN_lights
    global odd, lx, ly, lz, lastFrom, sVer
    timer += delta_t
    if timer > 0.05:
        timer = 0.0
        get_frames_per_second(delta_t)
        try:
            s = ', '.join(str(round(x, 4)) for x in ac.ext_getCameraPos())
            sf = s.split(',')
            x = sf[0]
            y = sf[1]
            z = sf[2]
            dx = round(lx-float(sf[0]),4)
            dy = round(ly-float(sf[1]),4)
            dz = round(lz-float(sf[2]),4)
            dist = (dx*dx+dy*dy+dz*dz)*0.5
            if dist>15000:
                dist=0
            # ac.log("DIFF = " + str(dx) + ", " + str(dy) + ", "+ str(dz))

            currPoT = ac.getCarState(0, acsys.CS.NormalizedSplinePosition)
            # xw, yw, zw = ac.getCarState(0, acsys.CS.WorldPosition)
            # currentTime = ac.getCarState(0, acsys.CS.LapTime)

            lightsvis = ac.ext_getLightsVisible()
            if lightsvis>MAX_lights:
                MAX_lights=lightsvis
            if lightsvis<MIN_lights:
                MIN_lights=lightsvis
            # ac.ext_setCameraFov(30)
            ac.setText(label, sVer
                + "\nFPS     (" + str(int(MIN_fps)) + "˅˄" + str(int(MAX_fps)) + "):    " + str(round(current_fps,1))
                + "\nLights total (mirror: " + str(ac.ext_getLightsMirrorVisible()) + ") :   "  + str(ac.ext_getTrackLightsNum())
                + "\n  - 🔦 visible (" + str(int(MIN_lights)) + "˅˄" + str(int(MAX_lights)) + "):   -   " + str(int(lightsvis))
                #"Lights: " + str(ac.ext_getLightsNum())
                #+ "\nVisible lights: " + str(ac.ext_getLightsVisible())
                ## + "\nMirror lights: " + str(ac.ext_getLightsMirrorVisible())
                + "\nFOV: " + str(round(ac.ext_getCameraFov(), 3))
                + "\nAmbient darkness: " + str(round(ac.ext_getAmbientMult(), 3))
                # + "\ncamera matr.: " + ', '.join(str(round(x, 2)) for x in ac.ext_getCameraMatrix())
                # + "\ncamera proj.: " + ', '.join(str(round(x, 2)) for x in ac.ext_getCameraProj())
                # + "\ncamera view: " + ', '.join(str(round(x, 2)) for x in ac.ext_getCameraView())
                + "\n⌻ Cam xyz: " + ' | '.join(str(round(x, 2)) for x in ac.ext_getCameraPos())
                + "\n-currPoT  : " + str(round(currPoT,6))
                + "\n-xyz-diff : " + str(round(dx,1)) + " | " + str(round(dy,1)) + " | "+ str(round(dz,1))
                + "\n-dist2last cam: " + str(round(dist,4))
                # + "\n-cam-direction: " + str(ac.lj_getCameraDirection())
                + "\n--dist. traveled in m: " + str(round(info.graphics.distanceTraveled,2))
                # + "\nCentric force:" + str(round(ac.ext_getAngleSpeed(), 3))
                + "\n--baseAltitude in m: " + str(round(ac.ext_getAltitude(0), 3))
                + "\n--Altitude in m: " + str(round(ac.ext_getBaseAltitude(0), 3))
                # + "\ntyres vkm: " + str(round(ac.ext_getTyreVirtualKM(), 3))
                + "\ntyre grain: "     + str(round(ac.ext_getTyreGrain   (0, 3), 4))
                + "\ntyre blister: "   + str(round(ac.ext_getTyreBlister (0, 3), 4))
                + "\ntyre flatspots: " + str(round(ac.ext_getTyreFlatSpot(0, 3), 4))
                )
        except:
            #if error < 10:
            #    ac.log("AccExtHelper:" + traceback.format_exc())
            ac.setText(label,"FPS     (" + str(int(MIN_fps)) + "˅˄" + str(int(MAX_fps)) + "):    " + str(round(current_fps,1)))
            # ac.setText(label, "Unexpected error:" + traceback.format_exc())
        try:
            if (info.graphics.status != 2) & (info.graphics.status != 1):
                __init__()  # reset if not live or replay
        except:
            if error < 10:
                ac.setText(label, "error")
                #ac.console("ExtHelper: could not reset" + traceback.format_exc())

def copyCameraCoords(*args):
    global odd, lx, ly, lz, lastFrom
    try:
        s = ", ".join(str(round(x, 3)) for x in ac.ext_getCameraPos())
        sf = s.split(",")
        x = sf[0]
        y = sf[1]
        z = sf[2]
        dx = round(lx-float(sf[0]),4)
        dy = round(ly-float(sf[1]),4)
        dz = round(lz-float(sf[2]),4)
        dist = (dx*dx+dy*dy+dz*dz)*0.5
        # ac.log("DIFF = " + str(dx) + ", " + str(dy) + ", "+ str(dz))
        #if odd:
        #    s = "LINE_FROM = " + s
        #else:
        #    s = "LINE_TO = " + s
        # if lastFrom=="":
        #     ac.ext_setClipboardData(s)
        # else:
        #     ac.ext_setClipboardData(lastFrom + "\nDIFF = " + str(dx) + ", " + str(dy) + ", "+ str(dz)+ "\n" + s + "\n" + str(dist))
        # ac.setPpColorTemperatureK(2500)
        currPoT = ac.getCarState(0, acsys.CS.NormalizedSplinePosition)
        ac.ext_setClipboardData(
            # lastFrom +
            "\nCamPos   : " + s +
            "\nxyz-diff : " + str(dx) + ", " + str(dy) + ", "+ str(dz)+
            "\ndistance : " + str(dist) +
            "\ncurrPoT  : " + str(round(currPoT,6)) )
        # ac.log(s)
        lastFrom = s
        odd = not odd
        lx = float(sf[0])
        ly = float(sf[1])
        lz = float(sf[2])
    except:
        ac.log("Unexpected error:" + traceback.format_exc())


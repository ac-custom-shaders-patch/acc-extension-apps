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
stepBackButton = 0
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
error = 0
timer = 0

def acMain(ac_version):
    global app, label, stepBackButton
    global vaoToggleButton, vaoDebugButton, lightsDebugButton, copyCameraCoordsButton
    global doorToggleButton, driverToggleButton

    try:
        app = ac.newApp("Shaders Patch Debug")
        ac.setTitle(app, "   Shaders Patch")
        ac.setSize(app, 180, 230)

        label = ac.addLabel(app, "")
        ac.setPosition(label, 5, 30)

        # i = 0
        # while i < 1200:
        #     labelTemp = ac.setPosition(ac.addLabel(app, "Label #" + str(i)), 5, 30 + i)
        #     ac.setFontSize(labelTemp, 14 + (i % 10))
        #     i += 1

        stepBackButton = ac.addButton(app, "Step back")
        ac.setPosition(stepBackButton, 20, 184)
        ac.setSize(stepBackButton, 140, 22)
        ac.setFontSize(stepBackButton, 14)
        ac.addOnClickedListener(stepBackButton, takeAStepBack)
        ac.setCustomFont(stepBackButton, "Segoe UI; Weight=UltraBlack", 0, 0)

        driverToggleButton = ac.addButton(app, "Driver")
        ac.setPosition(driverToggleButton, 20, 132)
        ac.setSize(driverToggleButton, 40, 22)
        ac.setFontSize(driverToggleButton, 14)
        ac.addOnClickedListener(driverToggleButton, driverToggle)

        doorToggleButton = ac.addButton(app, "🚪")
        ac.setPosition(doorToggleButton, 70, 132)
        ac.setCustomFont(doorToggleButton, "Segoe UI Symbol; Weight=UltraLight", 0, 0)
        ac.setSize(doorToggleButton, 40, 22)
        ac.setFontSize(doorToggleButton, 14)
        ac.addOnClickedListener(doorToggleButton, doorToggle)

        copyCameraCoordsButton = ac.addButton(app, "Copy")
        ac.setPosition(copyCameraCoordsButton, 120, 132)
        ac.setSize(copyCameraCoordsButton, 40, 22)
        ac.setFontSize(copyCameraCoordsButton, 14)
        ac.addOnClickedListener(copyCameraCoordsButton, copyCameraCoords)

        vaoToggleButton = ac.addButton(app, "V +/−")
        ac.setPosition(vaoToggleButton, 20, 158)
        ac.setSize(vaoToggleButton, 40, 22)
        ac.setFontSize(vaoToggleButton, 14)
        ac.addOnClickedListener(vaoToggleButton, vaoToggle)

        vaoDebugButton = ac.addButton(app, "V o/N")
        ac.setPosition(vaoDebugButton, 70, 158)
        ac.setSize(vaoDebugButton, 40, 22)
        ac.setFontSize(vaoDebugButton, 14)
        ac.addOnClickedListener(vaoDebugButton, vaoDebug)

        lightsDebugButton = ac.addButton(app, "🔦")
        ac.setPosition(lightsDebugButton, 120, 158)
        ac.setSize(lightsDebugButton, 40, 22)
        ac.setFontSize(lightsDebugButton, 14)
        ac.addOnClickedListener(lightsDebugButton, lightsDebug)
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

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

def copyCameraCoords(*args):
    try:
        ac.ext_setClipboardData(', '.join(str(round(x, 2)) for x in ac.ext_getCameraPos()))
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
            lightsDebugCount = 10
            lightsDebugDistance = 100.0
            lightsDebugMode = LightsDebugMode.Outline | LightsDebugMode.BoundingBox | LightsDebugMode.Text
            ac.ext_debugLights("?", lightsDebugCount, lightsDebugDistance, lightsDebugMode)
        else:
            ac.ext_debugLights("?", 0, 0, 0)
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

class ApplyTrackConfigFlags:
    Nothing = 0
    RestoreConditionsState = 1

def takeAStepBack(*args):
    try:
        ac.log("takeAStepBack()")
        ac.ext_takeAStepBack()
        # ac.ext_debugFn()
        # ac.ext_resetCar()
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

def acUpdate(delta_t):
    global error
    global timer
    timer += delta_t
    if timer > 0.1:
        timer = 0.0
        try:
            # ac.ext_setCameraFov(30)
            ac.setText(label,
                "Lights: " + str(ac.ext_getLightsNum())
                + "\nVisible lights: " + str(ac.ext_getLightsVisible())
                # + "\nMirror lights: " + str(ac.ext_getLightsMirrorVisible())
                # + "\nAmbient darkness: " + str(round(ac.ext_getAmbientMult(), 3))
                + "\nAltitude: " + str(round(ac.ext_getAltitude(0), 5)) + " m"
                + "\nCam.: " + ', '.join(str(round(x, 1)) for x in ac.ext_getCameraPos())
                # + "\nVersion: " + str(ac.ext_patchVersionCode())
                + "\nGr.: " + str(round(ac.ext_getTyreGrain(0, 3), 3)) + ", bl.: " + str(round(ac.ext_getTyreBlister(0, 3), 3)) + ", FS: " + str(round(ac.ext_getTyreFlatSpot(0, 3), 3))
                # + "\nAngle sp. (dbg.): " + str(round(ac.ext_getAngleSpeed(), 3))
                # + "\nCamera matr.: " + ', '.join(str(round(x, 2)) for x in ac.ext_getCameraMatrix())
                # + "\nCamera proj.: " + ', '.join(str(round(x, 2)) for x in ac.ext_getCameraProj())
                # + "\nCamera view: " + ', '.join(str(round(x, 2)) for x in ac.ext_getCameraView())
                # + "\nFOV: " + str(round(ac.ext_getCameraFov(), 3))
                )
        except:
            if error < 10:
                ac.log("Unexpected error:" + traceback.format_exc())
            ac.setText(label, "Unexpected error:" + traceback.format_exc())

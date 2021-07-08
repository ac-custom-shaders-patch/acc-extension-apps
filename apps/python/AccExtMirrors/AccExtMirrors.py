try:
    import ac, acsys, traceback
except ImportError:
    pass

# CSP values are saved in
# Documents\Assetto Corsa\cfg\extension\real_mirrors\carname.ini
#
# [REAL_MIRROR_0] ... [REAL_MIRROR_x] , as many x mirrors there are
# FLIP=0                ; or 1/2/3
# ROTATION = 0.00,0.00  ; x,y
# ASPECT_MULT = 1.2     ; 0.1 ... 2.0
# IS_MONITOR = 0        ; or 1

app = 0
mirror = 0
timer = 0
debug = 0
roles = "NLCR"
isPatch = 1

def acMain(ac_version):
    global app, debug, mirrorrole, mirrorindex, toggleMonButton, fovValue, arUp, arDown, isPatch
    global fovLabel, fovUpButton, fovDownButton, prevButton, nextButton, leftButton, rightButton, upButton, downButton
    try:
        app = ac.newApp("Shaders Patch Mirrors")
        ac.setTitle(app, "Mirrors")
        ac.setSize(app, 144, 213)

        debug = ac.addLabel(app, "")
        ac.setPosition(debug, 6, 35)

        mirrorrole = ac.addLabel(app, "")
        ac.setPosition(mirrorrole, 44, 40)

        mirrorindex = ac.addLabel(app, "")
        ac.setPosition(mirrorindex, 54, 46)
        ac.setFontSize(mirrorindex, 12)

        fovLabel = ac.addLabel(app, "FOV")
        ac.setPosition(fovLabel, 102, 164)

        fovValue = ac.addLabel(app, "")
        ac.setPosition(fovValue, 108, 112)

        fovUpButton = ac.addButton(app, "+")
        ac.setPosition(fovUpButton, 104, 84)
        ac.setSize(fovUpButton, 24, 24)
        ac.setFontSize(fovUpButton, 14)
        ac.addOnClickedListener(fovUpButton, fovUpMirror)

        fovDownButton = ac.addButton(app, "-")
        ac.setPosition(fovDownButton, 104, 132)
        ac.setSize(fovDownButton, 24, 24)
        ac.setFontSize(fovDownButton, 14)
        ac.addOnClickedListener(fovDownButton, fovDownMirror)

        toggleMonButton = ac.addButton(app, "m")
        ac.setPosition(toggleMonButton, 104, 40)
        ac.setSize(toggleMonButton, 24, 24)
        ac.setFontSize(toggleMonButton, 14)
        ac.addOnClickedListener(toggleMonButton, toggleMonMirror)

        prevButton = ac.addButton(app, "-")
        ac.setPosition(prevButton, 16, 40)
        ac.setSize(prevButton, 24, 24)
        ac.setFontSize(prevButton, 14)
        ac.addOnClickedListener(prevButton, prevMirror)

        nextButton = ac.addButton(app, "+")
        ac.setPosition(nextButton, 64, 40)
        ac.setSize(nextButton, 24, 24)
        ac.setFontSize(nextButton, 14)
        ac.addOnClickedListener(nextButton, nextMirror)

        leftButton = ac.addButton(app, "L")
        ac.setPosition(leftButton, 16, 108)
        ac.setSize(leftButton, 24, 24)
        ac.setFontSize(leftButton, 14)
        ac.addOnClickedListener(leftButton, leftMirror)

        rightButton = ac.addButton(app, "R")
        ac.setPosition(rightButton, 64, 108)
        ac.setSize(rightButton, 24, 24)
        ac.setFontSize(rightButton, 14)
        ac.addOnClickedListener(rightButton, rightMirror)

        upButton = ac.addButton(app, "U")
        ac.setPosition(upButton, 40, 84)
        ac.setSize(upButton, 24, 24)
        ac.setFontSize(upButton, 14)
        ac.addOnClickedListener(upButton, upMirror)

        downButton = ac.addButton(app, "D")
        ac.setPosition(downButton, 40, 132)
        ac.setSize(downButton, 24, 24)
        ac.setFontSize(downButton, 14)
        ac.addOnClickedListener(downButton, downMirror)

        arDown = ac.addButton(app, "  -")
        ac.setPosition(arDown, 15, 168)
        ac.setSize(arDown, 24, 24)
        ac.setFontSize(arDown, 14)
        ac.addOnClickedListener(arDown, downAR)
        ac.setFontAlignment(arDown, "left")

        arUp = ac.addButton(app, "+")
        ac.setPosition(arUp, 65, 168)
        ac.setSize(arUp, 24, 24)
        ac.setFontSize(arUp, 14)
        ac.addOnClickedListener(arUp, upAR)

    except:
        isPatch = 0

    return "AccExtMirrors"

def leftMirror(*args):
    try:
        ac.ext_mirrorLeft()
    except:
        acTrace()

def rightMirror(*args):
    try:
        ac.ext_mirrorRight()
    except:
        acTrace()

def upMirror(*args):
    try:
        ac.ext_mirrorUp()
    except:
        acTrace()

def downMirror(*args):
    try:
        ac.ext_mirrorDown()
    except:
        acTrace()

def prevMirror(*args):
    try:
        ac.ext_mirrorPrev()
    except:
        acTrace()

def nextMirror(*args):
    try:
        ac.ext_mirrorNext()
    except:
        acTrace()

def fovUpMirror(*args):
    try:
        ac.ext_mirrorFovUp()
    except:
        acTrace()

def fovDownMirror(*args):
    try:
        ac.ext_mirrorFovDown()
    except:
        acTrace()

def toggleMonMirror(*args):
    try:
        ac.ext_mirrorToggleMon()
    except:
        acTrace()

def downAR(*args):
    try:
        ac.ext_mirrorAspectRatioDown()
    except:
        acTrace()

def upAR(*args):
    try:
        ac.ext_mirrorAspectRatioUp()
    except:
        acTrace()

def acTrace():
    isPatch=0

def HideControls():
    global app, mirrorrole, mirrorindex, toggleMonButton, fovValue, arUp, arDown
    global fovLabel, fovUpButton, fovDownButton, prevButton, nextButton, leftButton, rightButton, upButton, downButton
    ac.setSize(app, 144, 65)
    ac.setVisible(mirrorrole,0)
    ac.setVisible(mirrorindex,0)
    ac.setVisible(fovValue,0)
    ac.setVisible(fovLabel,0)
    ac.setVisible(fovUpButton,0)
    ac.setVisible(fovDownButton,0)
    ac.setVisible(prevButton,0)
    ac.setVisible(nextButton,0)
    ac.setVisible(leftButton,0)
    ac.setVisible(rightButton,0)
    ac.setVisible(upButton,0)
    ac.setVisible(downButton,0)
    ac.setVisible(arUp,0)
    ac.setVisible(arDown,0)

def ShowControls():
    global app, mirrorrole, mirrorindex, toggleMonButton, fovValue, arUp, arDown
    global fovLabel, fovUpButton, fovDownButton, prevButton, nextButton, leftButton, rightButton, upButton, downButton
    ac.setSize(app, 144, 213)
    ac.setVisible(mirrorrole,1)
    ac.setVisible(mirrorindex,1)
    ac.setVisible(fovValue,1)
    ac.setVisible(fovLabel,1)
    ac.setVisible(fovUpButton,1)
    ac.setVisible(fovDownButton,1)
    ac.setVisible(prevButton,1)
    ac.setVisible(nextButton,1)
    ac.setVisible(leftButton,1)
    ac.setVisible(rightButton,1)
    ac.setVisible(upButton,1)
    ac.setVisible(downButton,1)
    ac.setVisible(arUp,1)
    ac.setVisible(arDown,1)


def acUpdate(delta_t):
    global timer, isPatch, app
    global debug, mirrorrole, mirrorindex, toggleMonButton, fovValue, arDown
    timer += delta_t
    if timer > 0.333:
        timer = 0.0
        if isPatch==1:
            try:
                cammode = ac.getCameraMode()
                if cammode == acsys.CM.Cockpit:
                    params = ac.ext_mirrorParams()
                    ac.setText(mirrorrole, roles[int(params[3])])
                    index = int(params[4])
                    if index > 0:
                        ac.setText(mirrorindex, str(index))
                    else:
                        ac.setText(mirrorindex, "")

                    ac.setText(fovValue, str(int(params[1])))
                    if params[0] == True:
                        ac.setText(toggleMonButton, "M")
                        ac.setText(debug, 'set to Monitor')
                        HideControls()
                    else:
                        ac.setText(toggleMonButton, "m")
                        ac.setText(debug, '')
                        ShowControls()
                    ac.setText(arDown, '  -   ' + str(round(float(params[2]),1) ) + '\n       AR')
                    ac.setVisible(toggleMonButton,1)
                else:
                    HideControls()
                    ac.setVisible(toggleMonButton,0)
                    ac.setVisible(mirrorrole,0)
                    ac.setText(debug, 'Not in Cockpit cam.')
                    ac.setSize(app, )
            except:
                acTrace()
        else:
            ac.setText(debug,'Shaders Patch not active.')

def acShutdown(*args):
    return

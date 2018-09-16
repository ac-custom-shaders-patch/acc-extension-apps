try:
    import ac
    import acsys
    import traceback
except ImportError:
    pass

app = 0
label = 0
error = 0

def acMain(ac_version):
    global app, label

    try:
        app = ac.newApp("Shaders Patch Mirrors")
        ac.setTitle(app, "Mirrors")
        ac.setSize(app, 200, 200)

        label = ac.addLabel(app, "")
        ac.setPosition(label, 48, 48)

        fovlabel = ac.addLabel(app, "FOV")
        ac.setPosition(fovlabel, 150, 80)

        fovUpButton = ac.addButton(app, "+")
        ac.setPosition(fovUpButton, 150, 48)
        ac.setSize(fovUpButton, 24, 24)
        ac.setFontSize(fovUpButton, 14)
        ac.addOnClickedListener(fovUpButton, fovUpMirror)

        fovDownButton = ac.addButton(app, "-")
        ac.setPosition(fovDownButton, 150, 112)
        ac.setSize(fovDownButton, 24, 24)
        ac.setFontSize(fovDownButton, 14)
        ac.addOnClickedListener(fovDownButton, fovDownMirror)

        toggleMonButton = ac.addButton(app, "M")
        ac.setPosition(toggleMonButton, 150, 160)
        ac.setSize(toggleMonButton, 24, 24)
        ac.setFontSize(toggleMonButton, 14)
        ac.addOnClickedListener(toggleMonButton, toggleMonMirror)

        prevButton = ac.addButton(app, "-")
        ac.setPosition(prevButton, 16, 48)
        ac.setSize(prevButton, 24, 24)
        ac.setFontSize(prevButton, 14)
        ac.addOnClickedListener(prevButton, prevMirror)

        nextButton = ac.addButton(app, "+")
        ac.setPosition(nextButton, 64, 48)
        ac.setSize(nextButton, 24, 24)
        ac.setFontSize(nextButton, 14)
        ac.addOnClickedListener(nextButton, nextMirror)

        leftButton = ac.addButton(app, "L")
        ac.setPosition(leftButton, 16, 120)
        ac.setSize(leftButton, 28, 28)
        ac.setFontSize(leftButton, 14)
        ac.addOnClickedListener(leftButton, leftMirror)

        rightButton = ac.addButton(app, "R")
        ac.setPosition(rightButton, 76, 120)
        ac.setSize(rightButton, 28, 28)
        ac.setFontSize(rightButton, 14)
        ac.addOnClickedListener(rightButton, rightMirror)

        upButton = ac.addButton(app, "U")
        ac.setPosition(upButton, 46, 90)
        ac.setSize(upButton, 28, 28)
        ac.setFontSize(upButton, 14)
        ac.addOnClickedListener(upButton, upMirror)

        downButton = ac.addButton(app, "D")
        ac.setPosition(downButton, 46, 150)
        ac.setSize(downButton, 28, 28)
        ac.setFontSize(downButton, 14)
        ac.addOnClickedListener(downButton, downMirror)
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

def leftMirror(*args):
    try:
        ac.ext_mirrorLeft()
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

def rightMirror(*args):
    try:
        ac.ext_mirrorRight()
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

def upMirror(*args):
    try:
        ac.ext_mirrorUp()
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

def downMirror(*args):
    try:
        ac.ext_mirrorDown()
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

def prevMirror(*args):
    try:
        ac.ext_mirrorPrev()
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

def nextMirror(*args):
    try:
        ac.ext_mirrorNext()
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

def fovUpMirror(*args):
    try:
        ac.ext_mirrorFovUp()
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

def fovDownMirror(*args):
    try:
        ac.ext_mirrorFovDown()
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

def toggleMonMirror(*args):
    try:
        ac.ext_mirrorToggleMon()
    except:
        ac.log("Unexpected error:" + traceback.format_exc())

def acUpdate(delta_t):
    global error

    try:
        ac.setText(label, str(ac.ext_mirrorCurrent()))
    except:
        if error < 10:
            ac.log("Unexpected error:" + traceback.format_exc())
        ac.setText(label, "Unexpected error:" + traceback.format_exc())

import ac, acsys, os, sys, traceback, configparser, codecs
cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(cwd))
os.environ['PATH'] = os.environ['PATH'] + ";."
import ctypes # we only provide 64bit _ctype version, CSP is only that
from ctypes import wintypes
CSIDL_PERSONAL = 5 # My Documents
SHGFP_TYPE_CURRENT = 0 # Get current, not default value
buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)
userDir = buf.value # bingo, userdir/documents!
smart_mirrorini = userDir + "\\Assetto Corsa\\cfg\\extension\\smart_mirror.ini"
ac.log('AccExtMirror ini: ' + smart_mirrorini)

# \\Assetto Corsa\\extension\\config\\smart_mirror.ini
# looks like this:
# [PIECE_0]
# ; hidden
# WIDTH=0.1185 * screen.height * 4
# HEIGHT=0.1185 * screen.height
# CENTER_X=0.5 * screen.width
# CENTER_Y=85 + 0.1185 * screen.height / 2
# OPACITY=1


xoffset = 0
yoffset = 5
app = 0
mirror = 0
timer = 0.0
debug = 0
isPatch = True
mirrorrole = 0
mirrorindex = 0
toggleMonButton = 0
fovValue = 0
arUp = 0
arDown = 0
fovLabel = 0
fovUpButton = 0
fovDownButton = 0
leftButton = 0
rightButton = 0
upButton = 0
downButton = 0
prevButton = 0
nextButton = 0
virt=False
roles = "NLCR"
rolesLONG = ["None","Left","Center","Right"]

def VirtChange(dsize, dx, dy):
    global smart_mirrorini, xoffset, yoffset, smart_mirrorini
    try:
        configDocs = configparser.ConfigParser(empty_lines_in_values=False, inline_comment_prefixes=(";","/","#","\\"), strict=False)
        configDocs.optionxform = str # keep case
        if not os.path.isfile(smart_mirrorini):
            with codecs.open(smart_mirrorini, 'w', 'utf_8', errors='ignore') as f:
                f.write('')
        else:
            configDocs.read(smart_mirrorini)

        # defaults
        swO='0.1185'
        shO='0.1185'
        sxoffset=str(xoffset)
        syoffset=str(yoffset)
        if not configDocs.has_section('PIECE_0'):
            configDocs.add_section('PIECE_0')
            syoffset =      '85 + ' +   str(round(float(shO) + dsize,4)) + ' * screen.height / 2'
        else:
            if configDocs.has_option('PIECE_0', 'WIDTH'):
                swO = configDocs['PIECE_0']['WIDTH'].split('*')[0].strip()
            if configDocs.has_option('PIECE_0', 'HEIGHT'):
                shO = configDocs['PIECE_0']['HEIGHT'].split('*')[0].strip()
            if configDocs.has_option('PIECE_0', 'APP_VIRTYOFFSET'):
                yoffset = configDocs['PIECE_0']['APP_VIRTYOFFSET']
            if configDocs.has_option('PIECE_0', 'APP_VIRTXOFFSET'):
                xoffset = configDocs['PIECE_0']['APP_VIRTXOFFSET']
            sxoffset = '0.5 * screen.width + ' + str(round(float(xoffset) + float(dx), 4))
            syoffset = str(float(yoffset) + float(dy)) + ' + '+ str(round(float(shO) + dsize,4)) + ' * screen.height / 2'

        configDocs.set('PIECE_0', 'WIDTH',    str(round(float(swO) + dsize,4)) + ' * screen.height * 4')
        configDocs.set('PIECE_0', 'HEIGHT',   str(round(float(shO) + dsize,4)) + ' * screen.height')
        configDocs.set('PIECE_0', 'CENTER_X', sxoffset)
        configDocs.set('PIECE_0', 'CENTER_Y', syoffset)
        configDocs.set('PIECE_0', 'OPACITY', '1')
        configDocs.set('PIECE_0', 'APP_VIRTXOFFSET', str(float(xoffset) + float(dx)) )
        configDocs.set('PIECE_0', 'APP_VIRTYOFFSET', str(float(yoffset) + float(dy)) )

        with open(smart_mirrorini, 'w') as configfile:
            configDocs.write(configfile, space_around_delimiters=False)
    except:
        ac.log('AccExtMirrors main: \n' + traceback.format_exc())

def prevMirror(*args):
    ac.ext_mirrorPrev()

def nextMirror(*args):
    ac.ext_mirrorNext()

def leftMirror(*args):
    global virt
    if virt:
        VirtChange(0,-5,0)
    else:
        ac.ext_mirrorLeft()

def rightMirror(*args):
    global virt
    if virt:
        VirtChange(0,5,0)
    else:
        ac.ext_mirrorRight()

def upMirror(*args):
    global virt
    if virt:
        VirtChange(0,0,-5)
    else:
        ac.ext_mirrorUp()

def downMirror(*args):
    global virt
    if virt:
        VirtChange(0,0,5)
    else:
        ac.ext_mirrorDown()

def fovUpMirror(*args):
    global virt
    if virt:
        VirtChange(0.01,0,0)
    else:
        ac.ext_mirrorFovUp()

def fovDownMirror(*args):
    global virt
    if virt:
        VirtChange(-0.01,0,0)
    else:
        ac.ext_mirrorFovDown()

def toggleMonMirror(*args):
    ac.ext_mirrorToggleMon()

def downAR(*args):
    ac.ext_mirrorAspectRatioDown()

def upAR(*args):
    ac.ext_mirrorAspectRatioUp()

def ShowVirtControls():
    global virt
    virt=True
    ac.setText(fovLabel, "Size")
    ac.setVisible(fovValue,1)
    ac.setVisible(fovLabel,1)
    ac.setVisible(fovUpButton,1)
    ac.setVisible(fovDownButton,1)
    ac.setVisible(leftButton,1)
    ac.setVisible(rightButton,1)
    ac.setVisible(upButton,1)
    ac.setVisible(downButton,1)

def HideVirtControls():
    global virt
    virt=False
    ac.setText(fovLabel, "FOV")
    ac.setVisible(fovValue,0)
    ac.setVisible(fovLabel,0)
    ac.setVisible(fovUpButton,0)
    ac.setVisible(fovDownButton,0)
    ac.setVisible(leftButton,0)
    ac.setVisible(rightButton,0)
    ac.setVisible(upButton,0)
    ac.setVisible(downButton,0)

def HideControls():
    global app, mirrorrole, mirrorindex, toggleMonButton, fovValue, arUp, arDown
    global fovLabel, fovUpButton, fovDownButton, leftButton, rightButton, upButton, downButton, prevButton, nextButton
    ac.setSize(app, 144, 85)
    ac.setVisible(mirrorindex,0)
    ac.setVisible(fovValue,0)
    ac.setVisible(fovLabel,0)
    ac.setVisible(fovUpButton,0)
    ac.setVisible(fovDownButton,0)
    ac.setVisible(leftButton,0)
    ac.setVisible(rightButton,0)
    ac.setVisible(upButton,0)
    ac.setVisible(downButton,0)
    ac.setVisible(arUp,0)
    ac.setVisible(arDown,0)
    ac.setVisible(prevButton,0)
    ac.setVisible(nextButton,0)
    ac.setVisible(toggleMonButton,0)

def ShowControls():
    global app, mirrorrole, mirrorindex, toggleMonButton, fovValue, arUp, arDown
    global fovLabel, fovUpButton, fovDownButton, leftButton, rightButton, upButton, downButton, prevButton, nextButton
    ac.setSize(app, 144, 213)
    ac.setVisible(mirrorindex,1)
    ac.setVisible(fovValue,1)
    ac.setVisible(fovLabel,1)
    ac.setVisible(fovUpButton,1)
    ac.setVisible(fovDownButton,1)
    ac.setVisible(leftButton,1)
    ac.setVisible(rightButton,1)
    ac.setVisible(upButton,1)
    ac.setVisible(downButton,1)
    ac.setVisible(arUp,1)
    ac.setVisible(arDown,1)
    ac.setVisible(prevButton,1)
    ac.setVisible(nextButton,1)
    ac.setVisible(toggleMonButton,1)

def acMain(ac_version):
    try:
        global app, debug, mirrorrole, mirrorindex, toggleMonButton, fovValue, arUp, arDown, isPatch
        global fovLabel, fovUpButton, fovDownButton, prevButton, nextButton, leftButton, rightButton, upButton, downButton
        app = ac.newApp("AccExtMirrors")

        ac.setTitle(app, "Mirrors")
        ac.setSize(app, 144, 213)

        debug = ac.addLabel(app, "")
        ac.setPosition(debug, 6, 65)

        mirrorrole = ac.addLabel(app, "")
        # ac.setPosition(mirrorrole, 44, 40)
        ac.setPosition(mirrorrole, 35, 25)

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

        isPatch = int(ac.ext_patchVersionCode())>0
        # ac.log('AccExtMirrors: isPatch: \n' + str(isPatch) )
    except:
        isPatch = 0
        ac.log('AccExtMirrors main: \n' + traceback.format_exc())

    return "AccExtMirrors"

def acUpdate(delta_t):
    global timer, isPatch, app, rolesLONG
    global debug, mirrorrole, mirrorindex, toggleMonButton, fovValue, arDown, arUp, prevButton, nextButton
    global btnVirtSizePlus, btnVirtSizeMinus
    timer += delta_t
    if timer > 0.1 and ac.isConnected(0):
        timer = 0.0
        if not isPatch:
            ac.setText(debug,'Shaders Patch not active.')
        else:
            try:
                cammode = ac.getCameraMode()
                if cammode == acsys.CM.Cockpit:
                    params = ac.ext_mirrorParams()
                    if params[3]==0:
                        ac.setText(debug, '') #  + str(ac.ext_mirrorDebug()) )
                        HideControls()
                        ShowVirtControls()
                        ac.setText(mirrorrole, 'F11 VirtMirror')
                        ac.setText(fovValue, '')
                        ac.setSize(app, 144, 213)
                    else:
                        index = int(params[4])
                        HideVirtControls()
                        if bool(int(params[0])) == True:
                            HideControls()
                            ac.setText(debug, 'set to Monitor\n') #  + str(ac.ext_mirrorDebug()) )
                            ac.setText(toggleMonButton, "M")
                        else:
                            ShowControls()
                            ac.setText(debug, '\n') #  + str(ac.ext_mirrorDebug()) )
                            ac.setText(toggleMonButton, "m")
                        if index > 0:
                            ac.setText(mirrorindex, str(index))
                        else:
                            ac.setText(mirrorindex, "")
                        if virt:
                            ac.setText(fovValue, '')
                        else:
                            ac.setText(fovValue, str(int(params[1])))
                        # ac.setText(mirrorrole, roles[int(params[3])])
                        ac.setText(arDown, '  -   ' + str(round(float(params[2]),1) ) + '\n       AR')
                        ac.setText(mirrorrole, rolesLONG[int(params[3])])
                        ac.setVisible(toggleMonButton,1)
                        ac.setVisible(mirrorrole,1)
                        ac.setVisible(prevButton,1)
                        ac.setVisible(nextButton,1)
                        ac.setSize(app, 144, 213)
                else:
                    ac.setText(mirrorrole, 'Not in Cockpit\n') #  + str(ac.ext_mirrorDebug()) )
                    ac.setText(debug, '')
                    HideVirtControls()
                    HideControls()
                    ac.setSize(app, 144, 85)
            except:
                isPatch = False
                ac.log("AccExtMirror error: " + traceback.format_exc())

def acShutdown(*args):
    pass

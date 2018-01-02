'''
Nicole Lynn Krason
nicoleGUI.p
How to Run:
import nicoleGUI
reload(nicoleGUI)
nicoleGUI.nicoleGUI()
'''

print "Nicole Lynn Krason's Rigging GUI"


import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel
import functools as fun

global panelList
panelList = ["modelPanel1", "modelPanel2", "modelPanel3", "modelPanel4"]

global red, blue, yellow
red = 13
blue = 6
yellow = 17

def nicoleGUI():

	global windowWidth, windowHeight, mainColumnLayout, riggingLayout
	windowWidth = 325
	windowHeight = 600

	windowName = "Rigging Toolset"

	if pm.dockControl("Toolset", ex = True):
	   pm.deleteUI("Toolset", uit = True)


	window_object = pm.window(windowName, w = windowWidth, h = windowHeight, t = "toolSet")
	allowedAreas = ["right", "left"]

	scrollFieldColumnLayout = rcl(nc = 1)
	scrollField = pm.scrollLayout(w = (windowWidth)+30, h = windowHeight)
	mainColumnLayout = rcl(nc = 1)

	riggingLayout()

	pm.dockControl(l = "Nicole Krason's GUI", a = "right", con = window_object, aa = allowedAreas)

def riggingLayout():
	pm.setParent(mainColumnLayout)
	frameLayout(label = 'Rigging')
	global rigging
	rigging = pm.columnLayout()

	theBasicsLayout()
	jointsLayout()
	controlLayout()

def theBasicsLayout():
	pm.setParent(rigging)
	frameLayout(label = 'Basics')
	global theBasics
	theBasics = pm.columnLayout()

	FT()
	hideAndShowLayout()

	pm.setParent(rigging)

def FT():
	pm.setParent(theBasics)
	frameLayout(label = 'FT, DH, CP & NUKE')
	pm.columnLayout()
	rcl(nc = 4)
	button(freezeTransforms, True, label = 'FT', width = 4)
	button(deleteHistory, True, label = 'DH', width = 4)
	button(centerPivot, True, label = 'CP', width = 4)
	button(nukeIt, True, label = 'NUKE', width = 4)
	pm.setParent(theBasics)

def hideAndShowLayout():
	frameLayout(label = 'Show and Hide')
	hideAndShow = pm.columnLayout()
	rcl(nc = 7)
	pm.text("Geo", al = "right", w = windowWidth/7)
	pm.separator(hr = False, w = windowWidth/7)
	pm.text("Jnts", al = "center", w = windowWidth/7)
	pm.separator(hr = False, w = windowWidth/7)
	pm.text("IK", al = "center", w = windowWidth/7)
	pm.separator(hr = False, w = windowWidth/7)
	pm.text("Ctrls", al = "left", w = windowWidth/7)
	pm.setParent(hideAndShow)
	rcl(nc = 8)
	button(showAllGeo, True, label = 'Show', width = 8)
	button(hideAllGeo, True, label = 'Hide', width = 8)
	button(showAllJoints, True, label = 'Show', width = 8)
	button(hideAllJoints, True, label = 'Hide', width = 8)
	button(showAllIKHandles, True, label = 'Show', width = 8)
	button(hideAllIKHandles, True, label = 'Hide', width = 8)
	button(showAllCtrls, True, label = 'Show', width = 8)
	button(hideAllCtrls, True, label = 'Hide', width = 8)
	pm.setParent(hideAndShow)
	rcl(nc = 2)
	pm.text("Highlight Color (Binding):", al = "center", w = windowWidth/2)
	pm.text("Everything:", al = "center", w = windowWidth/2)
	pm.setParent(hideAndShow)
	rcl(nc = 4)
	button(showHighlightColor, True, label = 'Show', width = 4)
	button(hideHighlightColor, True, label = 'Hide', width = 4)
	button(showAllObjects, True, label = 'Show', width = 4)
	button(hideAllObjects, True, label = 'Hide', width = 4)
	pm.setParent(hideAndShow)

	drawingOverrides = pm.columnLayout()
	rcl(nc = 1)
	pm.text("Drawing Overrides:", al = "center", width = windowWidth)
	rcl(nc = 3)
	button(normalDrawingOverrides, True, label = "Normal", width = 3)
	button(templateDrawingOverrides, True, label = "Template", width = 3)
	button(referenceDrawingOverrides, True, label = "Reference", width = 3)
	pm.setParent(hideAndShow)

	frameLayout(label = 'Control Attributes')
	controlHideAndShow = pm.columnLayout()
	rcl(nc = 7)
	pm.text("Trans", al = "right", w = windowWidth/7)
	pm.separator(hr = False, w = windowWidth/7)
	pm.text("Rotate", al = "center", w = windowWidth/7)
	pm.separator(hr = False, w = windowWidth/7)
	pm.text("Scale", al = "center", w = windowWidth/7)
	pm.separator(hr = False, w = windowWidth/7)
	pm.text("Vis", al = "left", w = windowWidth/7)
	pm.setParent(controlHideAndShow)
	rcl(nc = 4)
	button(showAllTranslate, True, label = 'S All', width = 4)
	button(showAllRotate, True, label = 'S All', width = 4)
	button(showAllScale, True, label = 'S All', width = 4)
	button(showAllVisibility, True, label = 'Show', width = 4)
	pm.setParent(controlHideAndShow)
	rcl(nc = 4)
	button(hideAllTranslate, True, label = 'Hide', width = 4)
	button(hideAllRotate, True, label = 'Hide', width = 4)
	button(hideAllScale, True, label = 'Hide', width = 4)
	button(hideAllVisibility, True, label = 'Hide', width = 4)
	pm.setParent(controlHideAndShow)
	rcl(nc = 3)
	button(hideTranslateX, True, label = 'Hide', width = 3)
	button(hideTranslateY, True, label = 'Hide', width = 3)
	button(hideTranslateZ, True, label = 'Hide', width = 3)
	pm.setParent(controlHideAndShow)
	rcl(nc = 3)
	button(hideRotateX, True, label = 'Hide', width = 3)
	button(hideRotateY, True, label = 'Hide', width = 3)
	button(hideRotateZ, True, label = 'Hide', width = 3)
	pm.setParent(controlHideAndShow)
	rcl(nc = 3)
	button(hideScaleX, True, label = 'Hide', width = 3)
	button(hideScaleY, True, label = 'Hide', width = 3)
	button(hideScaleZ, True, label = 'Hide', width = 3)
	pm.setParent(controlHideAndShow)

	pm.setParent(theBasics)

def jointsLayout():
	global nameField, suffixField, jointNameField, jointSuffixField
	pm.setParent(rigging)
	frameLayout(label = 'Joints')
	joints = pm.columnLayout()
	rcl(nc = 4)
	button(jointTool, True, label = 'Joint Tool', width = 4)
	button(insertJointTool, True, label = 'Insert Joint', width = 4)
	button(mirrorJointsYZ, True, label = 'Mirror Jnts', width = 4)
	button(padding, True, label = 'Padding', width = 4)
	pm.setParent(joints)
	pm.text("Joint Renamer:", w = windowWidth)
	rcl(nc = 4)
	pm.text(l = "Name:", w = windowWidth/4)
	jointNameField = pm.textField(w = windowWidth/4)
	pm.text("Suffix:", w = windowWidth/4)
	jointSuffixField = pm.textField(w = windowWidth/4)
	pm.setParent(joints)
	rcl(nc = 1)
	renameButton = pm.button(l = "Rename Joints", w = windowWidth, c = pm.Callback(jointRenamer))
	pm.setParent(joints)
	rcl(nc = 1)
	pm.columnLayout(adj = True, cal = "left", co = ["left", -50])
	pm.floatSliderGrp(w = windowWidth, min = 0.01, max = 10.00, l = "Joint Size", pre = 2, f = True, v = .50, cc = jointSize, dc = jointSize, adj = True)
	rcl(nc = 1)
	pm.text(l = "Constraints:", w = windowWidth)
	pm.setParent(joints)
	rcl(nc = 5)
	global parentCheckbox, aimCheckbox, orientCheckbox, pointCheckbox, scaleCheckbox
	button(parentConstraintOn, True, label = 'Parent', width = 5)
	button(aimConstraintOn, True, label = 'Aim', width = 5)
	button(orientConstraintOn, True, label = 'Orient', width = 5)
	button(pointConstraintOn, True, label = 'Point', width = 5)
	button(scaleConstraintOn, True, label = 'Scale', width = 5)
	pm.setParent(joints)
	rcl(nc = 5)
	parentCheckbox = pm.checkBox(l = "Offset", w = windowWidth/5, v = True)
	aimCheckbox = pm.checkBox(l = "Offset", w = windowWidth/5, v = False)
	orientCheckbox = pm.checkBox(l = "Offset", w = windowWidth/5, v = False)
	pointCheckbox = pm.checkBox(l = "Offset", w = windowWidth/5, v = False)
	scaleCheckbox = pm.checkBox(l = "Offset", w = windowWidth/5, v = False)
	pm.setParent(joints)
	rcl(nc = 1)
	button(poleVectorConstraint, True, label = 'Pole Vector', width = 1)
	pm.setParent(joints)
	rcl(nc = 1)
	pm.setParent(joints)
	pm.columnLayout(adj = True, cal = "left", co = ["left", -50])
	pm.floatSliderGrp(w = windowWidth, min = 0.01, max = 10.00, l = "IK Size", pre = 2, f = True, v = .50, cc = ikSize, dc = ikSize, adj = True)
	pm.setParent("..")
	rcl(nc = 2)
	button(rpIkHandleTool, True, label = "IK (RP)", width = 2)
	button(scIkHandleTool, True, label = "IK (SC)", width = 2)
	pm.setParent(joints)

	pm.setParent(rigging)

def controlLayout():
	frameLayout(label = 'Controls')
	controls = pm.columnLayout()
	rcl(nc = 4)
	button(circleIcon, True, label = 'Circle', width = 4)
	button(arrowIcon, True, label = 'Arrow', width = 4)
	button(twoWayArrowIcon, True, label = '2/Arrow', width = 4)
	button(fourWayArrowIcon, True, label = '4/Arrow', width = 4)
	button(cubeIcon, True, label = 'Cube', width = 4)
	button(cogIcon, True, label = 'COG', width = 4)
	button(fiveFingerHandIcon, True, label = 'Hand', width = 4)
	button(poleVectorIcon, True, label = 'PV', width = 4)
	button(squareIcon, True, label = 'Sqr', width = 4)
	pm.setParent(controls)
	rcl(nc = 3)
	button(priming, True, label = 'Priming', width = 3)
	button(handAttributes, True, label = 'Hand Att', width = 3)
	button(rflAttributes, True, label = 'RFL', width = 3)
	pm.setParent(controls)
	rcl(nc = 3)
	button(controlAttributes, True, label = 'Contols', width = 3)
	button(ikfkAttributes, True, label = 'IKFK', width = 3)
	button(clusterObject, True, label = 'Cluster', width = 3)
	pm.setParent(controls)
	rcl(nc = 3)
	colorButton(cmd = fun.partial(colorOverride, red), width = 3, color = [1, .4, .4])
	colorButton(cmd = fun.partial(colorOverride, yellow), width = 3, color = [1, 1, .4])
	colorButton(cmd = fun.partial(colorOverride, blue), width = 3, color = [.4, .4, 1])
	pm.setParent(controls)

	pm.setParent(rigging)

######################################################################
def freezeTransforms(*args):
	pm.makeIdentity(a = True, t = 1, r = 1, s = 1)

def deleteHistory(*args):
	pm.delete(all = True, ch = True)

def centerPivot(*args):
	pm.xform(cp = True)

def nukeIt(*args):
	pm.makeIdentity(a = True, t = 1, r = 1, s = 1)
	pm.delete(all = True, ch = True)
	pm.xform(cp = True)

def showAllGeo(*args):
	for panel in panelList:
		pm.modelEditor(panel, e = True, pm = True)

def hideAllGeo(*args):
	for panel in panelList:
		pm.modelEditor(panel, e = True, pm = False)

def showAllJoints(*args):
	for panel in panelList:
		pm.modelEditor(panel, e = True, j = True)

def hideAllJoints(*args):
	for panel in panelList:
		pm.modelEditor(panel, e = True, j = False)

def showAllIKHandles(*args):
	for panel in panelList:
		pm.modelEditor(panel, e = True, ikh = True)

def hideAllIKHandles(*args):
	for panel in panelList:
		pm.modelEditor(panel, e = True, ikh = False)

def showAllCtrls(*args):
	for panel in panelList:
		pm.modelEditor(panel, e = True, nc = True, cv = True)

def hideAllCtrls(*args):
	for panel in panelList:
		pm.modelEditor(panel, e = True, nc = False, cv = False)

def showAllObjects(*args):
	for panel in panelList:
		pm.modelEditor(panel, e = True, alo = True, ca=False)

def hideAllObjects(*args):
	for panel in panelList:
		pm.modelEditor(panel, e = True, alo = True, ca=False)

def showHighlightColor(*args):
	pm.displayPref(da = True)

def hideHighlightColor(*args):
	pm.displayPref(da = False)

def normalDrawingOverrides(index, *args):
	selected = pm.ls(sl = True)
	for selection in selected:
		pm.setAttr(selection + ".overrideDisplayType", 0)

def templateDrawingOverrides(index, *args):
	selected = pm.ls(sl = True)
	for selection in selected:
		pm.setAttr(selection + ".overrideDisplayType", 1)

def referenceDrawingOverrides(index, *args):
	selected = pm.ls(sl = True)
	for selection in selected:
		pm.setAttr(selection + ".overrideDisplayType", 2)


######################################################################################################

def jointTool(*args):
	pm.mel.eval("JointTool")

def insertJointTool(*args):
	pm.mel.eval("InsertJointTool")

def jointRenamer(*args):
	
	jointChain = pm.ls(sl = True, dag = True, type = "joint")

	prefix = jointNameField.getText()
	suffix = jointSuffixField.getText()

	for index, jnt in enumerate(jointChain):
		
		new_name = '{0}_{1:02d}_{2}'.format(prefix, index + 1, suffix)

		jnt.rename(new_name)

		first_name = jointChain[0].replace("bind", "bind")
		jointChain[0].rename(first_name)

		end_name = jointChain[-1].replace("bind", "waste")
		jointChain[-1].rename(end_name)


def mirrorJointsYZ(*args):
	pm.mirrorJoint(myz = True, mb = True, sr = ("lt_", "rt_"))

def padding(*args):
	rootJoint = pm.ls(sl = True)[0]

	ori = raw_input()
	systemName = raw_input()
	suffix = "pad"

	pad_1_name = "{0}_{1}_00_{2}1".format(ori, systemName, suffix)
	pad_2_name = "{0}_{1}_00_{2}2".format(ori, systemName, suffix)

	pm.select(cl = True)

	pad_2 = pm.group(n = pad_2_name)
	pad_1 = pm.group(n = pad_1_name)

	tempConstraint = pm.pointConstraint(rootJoint, pad_1)

	pm.delete(tempConstraint)

	pm.parent(rootJoint, pad_2)

	pm.makeIdentity(rootJoint, a = True, t = 1, r = 1, s = 1)

def parentConstraintOn(*args):
	offsetParent = parentCheckbox.getValue()
	pm.parentConstraint(mo = offsetParent)

def aimConstraintOn(*args):
	offsetAim = aimCheckbox.getValue()
	pm.aimConstraint(mo = offsetAim)

def pointConstraintOn(*args):
	offsetPoint = pointCheckbox.getValue()
	pm.pointConstraint(mo = offsetPoint)	

def orientConstraintOn(*args):
	offsetOrient = orientCheckbox.getValue()
	pm.orientConstraint(mo = offsetOrient)

def scaleConstraintOn(*args):
	offsetScale = scaleCheckbox.getValue()
	pm.scaleConstraint(mo = offsetScale)

def poleVectorConstraint(*args):
	pm.poleVectorConstraint()

def jointSize(sizer):
	pm.jointDisplayScale(sizer)

def ikSize(ikSizer):
	pm.ikHandleDisplayScale(ikSizer)

def rpIkHandleTool(*args):
	pm.ikHandle(sol = "ikRPsolver")

def scIkHandleTool(*args):
	pm.ikHandle(sol = "ikSCsolver")

def circleIcon(*args):
	pm.circle(nr = [0, 1, 0])

def arrowIcon(*args):
	arrow = pm.curve(d = 1, p = [(2.5, 0, 2.5,), (5, 0, 2.5), (5, 0, 5), (6.25, 0, 5), (3.75, 0, 7.5), (1.25, 0, 5), (2.5, 0, 5), (2.5, 0, 2.5)], k = [0,1,2,3,4,5,6,7] )
	pm.xform(arrow, cp = True)
	pm.move(arrow, rpr = True)
	pm.makeIdentity(arrow, a = True, t = 1, r = 1, s = 1, n = 0, pn = 1)

def twoWayArrowIcon(*args):
	twoWayArrow = pm.mel.eval("curve -d 1 -p 9.984186 0 6.079122 -p 12.033601 0 6.056861 -p 12.011836 0 3.017724 -p 9.976887 0 3.017724 -p 12.977521 0 0.0230467 -p 16.036775 0 3.062585 -p 14.024301 0 3.062585 -p 14.016239 0 6.056861 -p 16.065942 0 6.012336 -p 12.987368 0 9.006634 -p 10.006515 0 6.101382 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10")
	pm.xform(twoWayArrow, cp = True)
	pm.move(twoWayArrow, rpr = True)
	pm.makeIdentity(twoWayArrow, a = True, t = 1, r = 1, s = 1, n = 0, pn = 1)

def fourWayArrowIcon(*args):
	pm.mel.eval("curve -d 1 -p 0 0 -6.25 -p 2.5 0 -3.75 -p 1.25 0 -3.75 -p 1.25 0 -1.25 -p 3.75 0 -1.25 -p 3.75 0 -2.5 -p 6.25 0 0 -p 3.75 0 2.5 -p 3.75 0 1.25 -p 1.25 0 1.25 -p 1.25 0 3.75 -p 2.5 0 3.75 -p 0 0 6.25 -p -2.5 0 3.75 -p -1.25 0 3.75 -p -1.25 0 1.25 -p -3.75 0 1.25 -p -3.75 0 2.5 -p -6.25 0 0 -p -3.75 0 -2.5 -p -3.75 0 -1.25 -p -1.25 0 -1.25 -p -1.25 0 -3.75 -p -2.5 0 -3.75 -p 0 0 -6.25 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24")

def cubeIcon(*args):
	pm.mel.eval("curve -d 1 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28")

def cogIcon(*args):
	cog = pm.circle(s = 16)[0]
	pm.xform(cog.cv[::2], r = True, s = [0.476707, 0.476707, 0.476707])
	pm.xform(cog, r = True, ro = [90, 0, 0])
	pm.makeIdentity(cog, a = True, t = 1, r = 1, s = 1, n = 0, pn = 1)

def fiveFingerHandIcon(*args):
	handIcon = pm.mel.eval("curve -d 2 -p 0.341474 0 -4.10043 -p 0.349418 0 -4.227543 -p 0.341474 0 -4.346711 -p 0.460642 0 -4.442045 -p 0.6672 0 -4.569158 -p 0.849925 0 -4.688327 -p 1.024705 0 -4.847218 -p 1.263042 0 -4.958441 -p 1.429877 0 -5.045831 -p 1.620546 0 -5.109388 -p 1.755604 0 -5.188833 -p 1.787382 0 -5.33978 -p 1.668214 0 -5.451004 -p 1.350432 0 -5.474837 -p 1.12004 0 -5.395392 -p 0.905537 0 -5.292113 -p 0.691034 0 -5.308002 -p 0.532143 0 -5.51456 -p 0.444753 0 -5.808508 -p 0.412975 0 -6.046845 -p 0.412975 0 -6.221625 -p 0.500365 0 -6.467906 -p 0.611588 0 -6.722132 -p 0.659256 0 -7.047858 -p 0.706923 0 -7.302084 -p 0.730757 0 -7.516587 -p 0.675145 0 -7.691367 -p 0.563921 0 -7.723145 -p 0.444753 0 -7.627811 -p 0.381196 0 -7.357696 -p 0.301751 0 -7.079637 -p 0.246139 0 -6.777744 -p 0.166693 0 -6.602964 -p 0.103137 0 -6.467906 -p 0.0385937 0 -6.394065 -p -0.0244248 0 -6.462335 -p -0.0349279 0 -6.619881 -p -0.0139217 0 -6.861452 -p -0.00341864 0 -7.055759 -p -0.0244248 0 -7.244814 -p -0.0401794 0 -7.407612 -p -0.055934 0 -7.617674 -p -0.0769402 0 -7.785723 -p -0.0874432 0 -8.006287 -p -0.166216 0 -8.100815 -p -0.339517 0 -8.090312 -p -0.41829 0 -7.964275 -p -0.41829 0 -7.580913 -p -0.402535 0 -7.360348 -p -0.392032 0 -7.103023 -p -0.371026 0 -6.950728 -p -0.381529 0 -6.75117 -p -0.365775 0 -6.567366 -p -0.376278 0 -6.446581 -p -0.449799 0 -6.415072 -p -0.544327 0 -6.483342 -p -0.591591 0 -6.724912 -p -0.638855 0 -6.961231 -p -0.722879 0 -7.171293 -p -0.780646 0 -7.418115 -p -0.848916 0 -7.628177 -p -0.959198 0 -7.785723 -p -1.106241 0 -7.712201 -p -1.111493 0 -7.470631 -p -1.037972 0 -7.197551 -p -1.006462 0 -6.971734 -p -0.953947 0 -6.714409 -p -0.89618 0 -6.509599 -p -0.848916 0 -6.325795 -p -0.890928 0 -6.194507 -p -1.022217 0 -6.194507 -p -1.179763 0 -6.404568 -p -1.379321 0 -6.646139 -p -1.500107 0 -6.861452 -p -1.626144 0 -6.971734 -p -1.767935 0 -6.924471 -p -1.752181 0 -6.730164 -p -1.631395 0 -6.493845 -p -1.452843 0 -6.194507 -p -1.295297 0 -5.994949 -p -1.174511 0 -5.784887 -p -1.121996 0 -5.52231 -p -1.069481 0 -5.201966 -p -1.022217 0 -4.93939 -p -0.906683 0 -4.682064 -p -0.785898 0 -4.524518 -p -0.696622 0 -4.32496 -p -0.680867 0 -4.109647 -p 0.348434 0 -4.093892 -k 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 -k 59 -k 60 -k 61 -k 62 -k 63 -k 64 -k 65 -k 66 -k 67 -k 68 -k 69 -k 70 -k 71 -k 72 -k 73 -k 74 -k 75 -k 76 -k 77 -k 78 -k 79 -k 80 -k 81 -k 82 -k 83 -k 84 -k 85 -k 86 -k 87 -k 87")
	pm.xform(cp = True)
	pm.move(rpr = True, a = True)
	pm.makeIdentity(handIcon, a = True, t = 1, r = 1, s = 1, n = 0, pn = 1)

def poleVectorIcon(*args):
	pm.mel.eval("curve -d 1 -p 0.707107 -0.353553 0 -p 9.27258e-08 -0.353553 -0.707107 -p -0.707107 -0.353553 -6.18172e-08 -p -3.09086e-08 -0.353553 0.707107 -p 0.707107 -0.353553 0 -p 0 0.353553 0 -p 9.27258e-08 -0.353553 -0.707107 -p -0.707107 -0.353553 -6.18172e-08 -p 0 0.353553 0 -p -3.09086e-08 -0.353553 0.707107 -p 0.707107 -0.353553 0 -p 0 0.353553 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11")

def squareIcon(*args):
	pm.mel.eval("curve -d 1 -p -1 0 -1 -p 0 0 -1 -p 1 0 -1 -p 1 0 0 -p 1 0 1 -p 0 0 1 -p -1 0 1 -p -1 0 0 -p -1 0 -1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 ;")

def priming(*args):
	jointChain = pm.ls(sl = True, dag = True)[:-1]

	iconList = []
	topGroup = []

	i = 0

	for jointName in jointChain:
	    iconName = jointName.replace("bind", "ctrl")
	    primeIcon = pm.circle(nr = [1, 0, 0], n = iconName)

	    groupOneName = jointName.replace('bind', 'prime3')
	    groupOne = pm.group(primeIcon, n = groupOneName)

	    groupTwoName = jointName.replace('bind', 'prime2')
	    groupTwo = pm.group(groupOne, n = groupTwoName)

	    groupThreeName = jointName.replace('bind', 'prime1')
	    groupThree = pm.group(groupTwo, n = groupThreeName)

	    tempConstraint = pm.parentConstraint(jointName, groupThree, mo = False)
	    pm.delete(tempConstraint)

	    pm.makeIdentity(primeIcon, a = True, t = True, r = True, s = True)
	    pm.parentConstraint(primeIcon, jointName, mo = True)

	    iconList.append(primeIcon)
	    topGroup.append(groupThree)
		
	    if (i > 0):
	        pm.parent(topGroup[i], iconList[i-1])
	        
	    i = i + 1
#####################################################################################

def button(cmd, TF, label, width):
	pm.button(l = label, w = windowWidth/width, c = cmd)

def colorButton(cmd, width, color):
	pm.button(l = '', w = windowWidth/width, c = cmd, bgc = color)

def frameLayout(label):
	pm.frameLayout(l = label, w = windowWidth, cl = True, cll = True)

def rcl(nc):
	pm.rowColumnLayout(nc = nc)

def colorOverride(index, *args):
	selected = pm.ls(sl = True)
	for selection in selected:
		pm.setAttr(selection + ".overrideEnabled", 1)
		pm.setAttr(selection + ".overrideColor", index)

def handAttributes(*args):
	pm.addAttr(ln = "HANDS", at = "enum", en = "----------------:", k = False)
	pm.setAttr('.HANDS', k = False, cb = True, l = True)

	pm.addAttr(ln = "INDEX", at = "enum", en = "----------------:", k = False)
	pm.setAttr('.INDEX', k = False, cb = True, l = True)

	pm.addAttr(ln = "All_Index", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Index_Root", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Index_1", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Index_2", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Index_Twist", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Index_Spread", at = "float", dv = 0, k = True)

	pm.addAttr(ln = "MIDDLE", at = "enum", en = "----------------:", k = False)
	pm.setAttr('.MIDDLE', k = False, cb = True, l = True)

	pm.addAttr(ln = "All_Middle", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Middle_Root", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Middle_1", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Middle_2", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Middle_Twist", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Middle_Spread", at = "float", dv = 0, k = True)

	pm.addAttr(ln = "RING", at = "enum", en = "----------------:", k = False)
	pm.setAttr('.RING', k = False, cb = True, l = True)

	pm.addAttr(ln = "All_Ring", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Ring_Root", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Ring_1", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Ring_2", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Ring_Twist", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Ring_Spread", at = "float", dv = 0, k = True)

	pm.addAttr(ln = "PINKY", at = "enum", en = "----------------:", k = False)
	pm.setAttr('.PINKY', k = False, cb = True, l = True)

	pm.addAttr(ln = "All_Pinky", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Pinky_Root", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Pinky_1", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Pinky_2", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Pinky_Twist", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Pinky_Spread", at = "float", dv = 0, k = True)

	pm.addAttr(ln = "THUMB", at = "enum", en = "----------------:", k = False)
	pm.setAttr('.THUMB', k = False, cb = True, l = True)

	pm.addAttr(ln = "All_Thumb", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Thumb_Root", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Thumb_1", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Thumb_2", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Thumb_Twist", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Thumb_Spread", at = "float", dv = 0, k = True)

def rflAttributes(*args):
	pm.addAttr(ln = "RFL", at = "enum", en = "----------------:", k = False)
	pm.setAttr('.RFL', k = False, cb = True, l = True)

	pm.addAttr(ln = "Lift_Heel", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Rotate_Heel", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Inner", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Outer", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Lift_Toe", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Rotate_Toe", at = "float", dv = 0, k = True)
	pm.addAttr(ln = "Ball", at = "float", dv = 0, k = True)

def controlAttributes(*args):
	pm.addAttr(ln = "CONTROLS", at = "enum", en = "----------:", k = False)
	pm.setAttr('.CONTROLS', k = False, cb = True, l = True)

	pm.addAttr(ln = "Controls", at = "float", dv = 0, min = 0, max = 1, k = True)

def ikfkAttributes(*args):
	pm.addAttr(ln = "IKFK", at = "enum", en = "----------:", k = False)
	pm.setAttr('.IKFK', k = False, cb = True, l = True)

	pm.addAttr(ln = "Ikfk", at = "float", dv = 0, min = 0, max = 10, k = True)

def showAllTranslate(*args):
	selected = pm.ls(sl = True)
	firstSelected = selected[0]
	firstSelected.tx.set(l = False, k = True)
	firstSelected.ty.set(l = False, k = True)
	firstSelected.tz.set(l = False, k = True)

def hideAllTranslate(*args):
	pm.setAttr(".tx", l = True, k = False, cb = False)
	pm.setAttr(".ty", l = True, k = False, cb = False)
	pm.setAttr(".tz", l = True, k = False, cb = False)

def hideTranslateX(*args):
	pm.setAttr(".tx", l = True, k = False, cb = False)

def hideTranslateY(*args):
	pm.setAttr(".ty", l = True, k = False, cb = False)

def hideTranslateZ(*args):
	pm.setAttr(".tz", l = True, k = False, cb = False)


def showAllRotate(*args):
	selected = pm.ls(sl = True)
	firstSelected = selected[0]
	firstSelected.rx.set(l = False, k = True)
	firstSelected.ry.set(l = False, k = True)
	firstSelected.rz.set(l = False, k = True)

def hideAllRotate(*args):
	pm.setAttr(".rx", l = True, k = False, cb = False)
	pm.setAttr(".ry", l = True, k = False, cb = False)
	pm.setAttr(".rz", l = True, k = False, cb = False)

def hideRotateX(*args):
	pm.setAttr(".rx", l = True, k = False, cb = False)

def hideRotateY(*args):
	pm.setAttr(".ry", l = True, k = False, cb = False)

def hideRotateZ(*args):
	pm.setAttr(".rz", l = True, k = False, cb = False)

def showAllScale(*args):
	selected = pm.ls(sl = True)
	firstSelected = selected[0]
	firstSelected.sx.set(l = False, k = True)
	firstSelected.sy.set(l = False, k = True)
	firstSelected.sz.set(l = False, k = True)

def hideAllScale(*args):
	pm.setAttr(".sx", l = True, k = False, cb = False)
	pm.setAttr(".sy", l = True, k = False, cb = False)
	pm.setAttr(".sz", l = True, k = False, cb = False)

def hideScaleX(*args):
	pm.setAttr(".sx", l = True, k = False, cb = False)

def hideScaleY(*args):
	pm.setAttr(".sy", l = True, k = False, cb = False)

def hideScaleZ(*args):
	pm.setAttr(".sz", l = True, k = False, cb = False)


def showAllVisibility(*args):
	selected = pm.ls(sl = True)
	firstSelected = selected[0]
	firstSelected.v.set(l = False, k = True)

def hideAllVisibility(*args):
	pm.setAttr(".v", l = True, k = False, cb = False)

def clusterObject(*args):
	pm.cluster()
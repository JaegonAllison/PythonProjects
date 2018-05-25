# Script to group and spin all objects in scene
import maya.cmds as cmds      
def startSpinAll():
    cmds.select(all=True)
    cmds.group(n=‘SpinningGroup’)
    cmds.currentTime(1)
    cmds.playbackOptions(l=‘continuous’,ps=1)
    cmds.setKeyframe(‘SpinningGroup’, at=‘rotateY’, v=0, t=1)
    cmds.setKeyframe(‘SpinningGroup’, at=‘rotateY’, v=360, t=100)
    cmds.play(f=True)

startSpinAll()
  
 
 
 
 
# Script to group and spin only selected objects  
import maya.cmds as cmds      
def startSpinSelected():
    cmds.group(n=‘SpinningGroup’)
    cmds.currentTime(1)
    cmds.playbackOptions(l=‘continuous’,ps=1)
    cmds.setKeyframe(‘SpinningGroup’, at=‘rotateY’, v=0, t=1)
    cmds.setKeyframe(‘SpinningGroup’, at=‘rotateY’, v=360, t=100)
    cmds.play(f=True)
    
startSpinSelected()








   
# Script to stop spinnning  
import maya.cmds as cmds  
def endSpin():
    cmds.cutKey(‘SpinningGroup’)
    cmds.play(st=False)
    cmds.rotate(0,0,0,‘SpinningGroup’)
    cmds.ungroup(‘SpinningGroup’)
    cmds.currentTime(1)

endSpin()
#ms.cutKey(cl=True)
                        YOU SHOULDN'T LEAVE YOUR FILES OPEN ON THE COMPUTER AT THE SCHOOL. FYI.

import maya.cmds as ms
def backflipAction(height):
    """quick and easy backflip to see your character in action."""
    
    # inatalize group and play options
    ms.group(n='flipper')
    ms.currentTime(1)
    ms.playbackOptions(l='continuous', ps=1, animationEndTime=25, max=25)
    
    # start / initalize flip action
    ms.setKeyframe('flipper', at='translateY', v=0, t=1)
    ms.setKeyframe('flipper', at='rotateX', v=0, t=1)
    ms.setKeyframe('flipper', at='scaleY', v=1, t=1)
    
    # mid / flip action
    ms.setKeyframe('flipper', at='translateY', v=-7, t=6)
    ms.setKeyframe('flipper', at='scaleY', v=0.8, t=6)
    ms.setKeyframe('flipper', at='rotateX', v=0, t=6)
    
    ms.setKeyframe('flipper', at='scaleY', v=1.3, t=10)
    ms.setKeyframe('flipper', at='translateY', v=height, t=16)
    ms.setKeyframe('flipper', at='scaleY', v=1, t=16)
    ms.setKeyframe('flipper', at='scaleY', v=1.3, t=20)
    
    # end / reset values
    ms.setKeyframe('flipper', at='translateY', v=0, t=24)
    ms.setKeyframe('flipper', at='rotateX', v=-360, t=24)
    ms.setKeyframe('flipper', at='scaleY', v=1, t=24)
    ms.setKeyframe('flipper', at='rotateX', v=0, t=25)
    
    ms.play(f=True, st=True)
    
backflipAction(165)


import maya.cmds as ms
def stopBackflip():
    """stop backflip action and clean up group / keys """
    
    ms.cutKey('flipper')
    ms.play(st=False)
    ms.scale(1,1,1,'flipper')
    ms.rotate(0,0,0, 'flipper')
    ms.move(0,0,0, 'flipper')
    ms.ungroup('flipper')
    ms.currentTime(1)
    
stopBackflip()

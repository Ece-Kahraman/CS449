from robotic import ry
import time
C = ry.Config()
C.addFile(ry.raiPath('../rai-robotModels/objects/kitchen.g'))
C.addFrame('part1.g')

#Part d - State2
C.addFrame(name="tray", parent="table1") \
.setShape(ry.ST.ssBox, size=[.4, .4, .05, .02]) \
.setColor([0,1,0]) \
.setRelativePose('t(0 0 .42) d(135 0 0 1)')

C.addFrame(name="item1", parent="tray") \
.setShape(ry.ST.ssBox, size=[.1, .1, .25, .02]) \
.setRelativePosition([-.1, -.1, .15]) \
.setColor([1,0,0])

C.addFrame(name="item2", parent="tray") \
.setShape(ry.ST.ssBox, size=[.1, .1, .25, .02]) \
.setRelativePosition([.1, .1, .15]) \
.setColor([1,1,0])

C.view()
time.sleep(35)



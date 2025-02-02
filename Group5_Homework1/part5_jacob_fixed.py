from robotic import ry
import numpy as np
import time
C = ry.Config()
C.addFile(ry.raiPath('../rai-robotModels/objects/kitchen.g'))
#C.addFrame('part1.g')

C.addFrame(name="tray", parent="stove1") \
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

C.addFile('kopke.g')
C.view()
time.sleep(2)
n = C.getJointDimension()
q = C.getJointState()
w = 2
W = w * np.identity(n)
for i in range(100):
    F = C.feature(ry.FS.position, ["handR"])
    F2 = C.feature(ry.FS.position,["item2"])
    y_target,_ = F2.eval(C)
    y,J = F.eval(C)
    print(y,y_target)
    q += np.linalg.inv(J.T @ J + W) @ J.T @ (y_target - y)
    C.setJointState(q)
    C.view()
    time.sleep(0.05)

for i in range(100):
    F = C.feature(ry.FS.position, ["handR"])
    F2 = C.feature(ry.FS.position,["tray"])
    y_target,_ = F2.eval(C)
    y,J = F.eval(C)
    print(y,y_target)
    q += np.linalg.inv(J.T @ J + W) @ J.T @ (y_target - y)
    C.setJointState(q)
    C.view()
    time.sleep(0.05)

for i in range(100):
    F = C.feature(ry.FS.position, ["handR"])
    F2 = C.feature(ry.FS.position,["item1"])
    y_target,_ = F2.eval(C)
    y,J = F.eval(C)
    print(y,y_target)
    q += np.linalg.inv(J.T @ J + W) @ J.T @ (y_target - y)
    C.setJointState(q)
    C.view()
    time.sleep(0.05)
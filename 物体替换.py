import maya.cmds as mc

#选中需要被替换的物体后执行以下操作
objA = mc.ls(sl = 1)
objN = list()
for inf in objA:
    obj_T = mc.getAttr('{}.translate'.format(inf))
    objN.append(obj_T)


#---------------------------------------------------#####
#选中替换的物体后执行以下操作
objB = mc.ls(sl = 1)
for i in range(0, len(objA)):
    d_objB = mc.duplicate(objB)
    mc.setAttr('{}.translate'.format(d_objB[0]), objN[i][0][0], objN[i][0][1], objN[i][0][2])
    mc.delete(objA[i])
    
#执行后被选中的替换物体会删除
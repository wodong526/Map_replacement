import maya.cmds as mc

#ѡ����Ҫ���滻�������ִ�����²���
objA = mc.ls(sl = 1)
objN = list()
for inf in objA:
    obj_T = mc.getAttr('{}.translate'.format(inf))
    objN.append(obj_T)


#---------------------------------------------------#####
#ѡ���滻�������ִ�����²���
objB = mc.ls(sl = 1)
for i in range(0, len(objA)):
    d_objB = mc.duplicate(objB)
    mc.setAttr('{}.translate'.format(d_objB[0]), objN[i][0][0], objN[i][0][1], objN[i][0][2])
    mc.delete(objA[i])
    
#ִ�к�ѡ�е��滻�����ɾ��
def tabdil(seccond):
    if ((seccond // 60) == 0) and ((seccond // 3600) == 0):
        print(seccond , " Seccond")
    elif ((seccond // 60) > 0) and ((seccond // 3600) == 0):
        print((seccond // 60) , " Minute " , (seccond % 60) , " seccond")
    elif ((seccond // 60) == 0) and ((seccond // 3600) > 0):
        print((seccond // 3600) , " Hour " , (seccond % 60) , " seccond")
    elif ((seccond // 60) > 0) and ((seccond // 3600) > 0):
        print((seccond // 3600) , " Hour " ,((seccond // 60)-60) , " Minute " ,(seccond % 60) , " seccond")
    else:
        pass
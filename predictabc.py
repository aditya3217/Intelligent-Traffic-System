def predict_side(road_images):
	

    
    dct = road_images
    
    r1 = int(road_images["up"].split(' ')[0])
    y1 = int(road_images["up"].split(' ')[1])
    g1 = int(road_images["up"].split(' ')[2])
    r2 = int(road_images["down"].split(' ')[0])
    y2 = int(road_images["down"].split(' ')[1])
    g2 = int(road_images["down"].split(' ')[2])
    r3 = int(road_images["left"].split(' ')[0])
    y3 = int(road_images["left"].split(' ')[1])
    g3 = int(road_images["left"].split(' ')[2])
    r4 = int(road_images["right"].split(' ')[0])
    y4 = int(road_images["right"].split(' ')[1])
    g4 = int(road_images["right"].split(' ')[2])
   

    out = ""
    r_list = [r1, r2, r3, r4]
    r_list.sort()
    gy_list = [g1+y1, g2+y2, g3+y3, g4+y4]

    k1 = max(r1, r2, r3, r4)
    out1 = -1
    drn = ""
    if(k1 == r1):
        out1 = 0
        drn = 'N'
    elif(k1 == r2):
        out1 = 1
        drn = 'S'
    elif(k1 == r3):
        out1 = 2
        drn = 'E'
    else:
        drn = 'W'
    k = max((g1+y1), (g2+y2), (g3+y3), (g4+y4))
    if(r1 == 0 and r2 == 0 and r3 == 0 and r4 == 0):
        if((g1+y1) == (g2+y2)):
            if((g2+y2) == (g3+y3)):
                if((g3+y3) == (g4+y4)):
                    k1 = max(y1, y2, y3, y4)
                    if(k1 == y1):
                        out = 'N'
                    elif(k1 == y2):
                        out = 'S'
                    elif(k1 == y3):
                        out = 'E'
                    else:
                        out = 'W'


        
        if(k == (g1+y1)):
            out = 'N'
        elif(k == (g2+y2)):
             out = 'S'
        elif(k == (g3+y3)):
             out = 'E'
        else:
             out = 'W'

    elif((r1 > 0 and r2 == 0 and r3 == 0 and r4 == 0) or (r1 == 0 and r2 > 0 and r3 == 0 and r4 == 0) or (r1 == 0 and r2 == 0 and r3 > 0 and r4 == 0) or (r1 == 0 and r2 == 0 and r3 == 0 and r4 > 0)):
        k1 = max(r1, r2, r3, r4)
        out1 = -1
        drn = ""
        if(k1 == r1):
            out1 = 0
            drn = 'N'
        elif(k1 == r2):
            out1 = 1
            drn = 'S'
        elif(k1 == r3):
            out1 = 2
            drn = 'E'
        else:
            drn = 'W'
        min1 = 1000
        for i in range(len(gy_list)):
            if(i != out1):
                min1 = min(min1, gy_list[i])
        if((3*k) > min1):
            out = drn
        else:
            k = max((g1+y1), (g2+y2), (g3+y3), (g4+y4))
        if(k == (g1+y1)):
            out = 'N'
        elif(k == (g2+y2)):
            out = 'S'
        elif(k == (g3+y3)):
            out = 'E'
        else:
            out = 'W'
    elif((r1 > 0 and r2 > 0 and r3 == 0 and r4 == 0) or (r1 > 0 and r2 == 0 and r3 > 0 and r4 == 0) or (r1 > 0 and r2 == 0 and r3 == 0 and r4 > 0) or (r1 == 0 and r2 > 0 and r3 > 0 and r4 == 0) or (r1 == 0 and r2 > 0 and r3 == 0 and r4 > 0) or (r1 == 0 and r2 == 0 and r3 > 0 and r4 > 0)):
        k1 = r_list[2]
        k2 = -1
        k3 = -1
        out2 = -1
        drn1 = ""
        if(k1 == r1):
            out2 = 0
            drn1 = 'N' 
            k2 = y1
            k3 = g1 
        elif(k1 == r2):
            out2 = 1
            drn1 = 'S'
            k2 = y2
            k3 = g2
        elif(k1 == r3):
            out2 = 2
            drn1 = 'E'
            k2 = y3
            k3 = g3
        else:
            out2 = 3
            drn1 = 'W'
            k2 = y4
            k3 = g4
        k1 = max(r1, r2, r3, r4)
        out1 = -1
        k4 = -1
        k5 = -1
        drn = ""
        max_gy = -1000
        c = 0
        if(k1 == r1):
            c += 1
            out1 = 0
            prev_max_gy = max_gy
            max_gy = max(max_gy, gy_list[out1])
            if(max_gy > prev_max_gy):
                drn = 'N'
        if(k1 == r2):
            c += 1
            out1 = 1
            prev_max_gy = max_gy
            max_gy = max(max_gy, gy_list[out1])
            if(max_gy > prev_max_gy):
                drn = 'S'
        if(k1 == r3):
            c += 1
            out1 = 2
            prev_max_gy = max_gy
            max_gy = max(max_gy, gy_list[out1])
            if(max_gy > prev_max_gy):
                drn = 'E'
        if(k1 == r4):
            c += 1
            out1 = 3
            prev_max_gy = max_gy
            max_gy = max(max_gy, gy_list[out1])
            if(max_gy > prev_max_gy):
                drn = 'W'
        min1 = 1000
        max1 = -1
        for i in range(len(gy_list)):
            if(i != out1 and i != out2):
                min1 = min(min1, gy_list[i])
                max1 = max(max1, gy_list[i])
                drn2 = ""
        if(c > 1):
            out = drn
        else:    
            if(max1 == r1):
                drn2 = 'N'
            elif(max1 == r2):
                drn2 = 'S'
            elif(max1 == r3):
                drn2 = 'E'
            else:
                drn2 = 'W'
            if(3*k1 > min(r_list[2]+k2+k3, min1)):
                out = drn
            elif(3*r_list[2] > min1):
                out = drn1
            else:
                out = drn2  
    elif((r1 > 0 and r2 > 0 and r3 > 0 and r4 == 0) or (r1 > 0 and r2 > 0 and r3 == 0 and r4 > 0) or (r1 > 0 and r2 == 0 and r3 > 0 and r4 > 0) or (r1 == 0 and r2 > 0 and r3 > 0 and r4 > 0)):
        k1 = r_list[2]
        k2 = -1
        k3 = -1
        out2 = -1
        drn1 = ""
        if(k1 == r1):
            out2 = 0
            drn1 = 'N' 
            k2 = y1
            k3 = g1 
        elif(k1 == r2):
            out2 = 1
            drn1 = 'S'
            k2 = y2
            k3 = g2
        elif(k1 == r3):
            out2 = 2
            drn1 = 'E'
            k2 = y3
            k3 = g3
        else:
            out2 = 3
            drn1 = 'W'
            k2 = y4
            k3 = g4
        k1 = max(r1, r2, r3, r4)
        out1 = -1
        k4 = -1
        k5 = -1
        drn = ""
        max_gy = -1000
        c = 0
        if(k1 == r1):
            c += 1
            out1 = 0
            prev_max_gy = max_gy
            max_gy = max(max_gy, gy_list[out1])
            if(max_gy > prev_max_gy):
                drn = 'N'
        if(k1 == r2):
            c += 1
            out1 = 1
            prev_max_gy = max_gy
            max_gy = max(max_gy, gy_list[out1])
            if(max_gy > prev_max_gy):
                drn = 'S'
        if(k1 == r3):
            c += 1
            out1 = 2
            prev_max_gy = max_gy
            max_gy = max(max_gy, gy_list[out1])
            if(max_gy > prev_max_gy):
                drn = 'E'
        if(k1 == r4):
            c += 1
            out1 = 3
            prev_max_gy = max_gy
            max_gy = max(max_gy, gy_list[out1])
            if(max_gy > prev_max_gy):
                drn = 'W'
        min1 = 1000
        max1 = -1
        for i in range(len(gy_list)):
            if(i != out1 and i != out2):
                min1 = min(min1, gy_list[i])
                max1 = max(max1, gy_list[i])
                drn2 = ""
        if(c > 1):
            out = drn
        else:    
            if(max1 == r1):
                drn2 = 'N'
            elif(max1 == r2):
                drn2 = 'S'
            elif(max1 == r3):
                drn2 = 'E'
            else:
                drn2 = 'W'
            if(3*k1 > min(r_list[2]+k2+k3, min1)):
                out = drn
            elif(3*r_list[2] > min1):
                out = drn1
            else:
                out = drn2    
    elif(r1 > 0 and r2 > 0 and r3 > 0 and r4 > 0):
        out = drn      
    return out
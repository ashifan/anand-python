def checkio(l):
    a=l[0]
    b=l[1]
    c=l[2]
    poss_list = [a,b,c]
    str1 = a[0]+b[0]+c[0]
    str2 = a[1]+b[1]+c[1]
    str3 = a[2]+b[2]+c[2]
    poss_list.extend([str1, str2, str3])
    str4 = a[0]+b[1]+c[2]
    str5 = a[2]+b[1]+c[0]
    poss_list.extend([str4,str5])
    if "xxx" in poss_list:
        return "x"
    elif "ooo" in poss_list:
        return "o"
    else:
        return "D"
print checkio(["oo.","xox","xox"])
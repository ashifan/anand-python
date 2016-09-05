def nonUniqe(params):
    
    x=[]
    for i in params:
        if params.count(i) != 1:
            x.append(i)
    print x      
nonUniqe([1, 2, 3,4,5,5,6,6,6,6])

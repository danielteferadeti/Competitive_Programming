def countingValleys(steps, path):
    print(path)
    # Write your code here
    num_valley = 0
    cur_pst = 0
    vly_started = False
    
    for char in path: 
        if char == 'D' and not vly_started:
            if cur_pst == 0:
                cur_pst -=1
                vly_started = True
            else:
                cur_pst -=1
        elif char == 'D' and vly_started and cur_pst !=0:
            cur_pst -=1
        elif char == 'U':
            cur_pst +=1
        if cur_pst == 0 and vly_started:
            num_valley +=1
            vly_started = False
    return num_valley
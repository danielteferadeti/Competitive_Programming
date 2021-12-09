import sys

def insertion_sorting(given_list):
    cur_min = sys.maxsize
    min_ind = 0
    for j in range(len(given_list)):
        i = j
        while i < len(given_list):
            if cur_min > given_list[i]:
                cur_min = given_list[i]
                min_ind = i
            i+=1
        temp = given_list[j]
        given_list[j] = given_list[min_ind]
        given_list[min_ind] = temp
        cur_min = sys.maxsize
        min_ind = 0
    return given_list
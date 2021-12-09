import sys
def selection_sort(given_list):
    result = []
    cur_min = given_list[0]
    cur_ind = 0
    for j in range(len(given_list)):
        for i in range(len(given_list)):
            if cur_min > given_list[i]:
                cur_min = given_list[i]
                cur_ind = i
        result.append(cur_min)
        given_list[cur_ind] = sys.maxsize
        cur_min = given_list[0]
        cur_ind = 0
    return result
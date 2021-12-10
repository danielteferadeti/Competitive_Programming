def counting_sort(given_list):
    count_list = []
    result = []
    max_num = given_list[0]
    for element in given_list:
        if max_num < element:
            max_num = element

    for j in range(max_num + 1):
        count_list.append(0)

    for elt in given_list:
        count_list[elt] +=1

    for i in range(len(count_list)):
        if count_list[i] !=0:
            for k in range(count_list[i]):
                result.append(i)
    return result


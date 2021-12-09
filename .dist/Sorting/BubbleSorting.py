def bubbleSort(g_list):
    for k in range(len(g_list)):
        print(k)
        for i in range(len(g_list)-1):
            if g_list[i] > g_list[i+1]:
                temp = g_list[i]
                g_list[i] = g_list[i+1]
                g_list[i+1] = temp
    return g_list
def find_second_smallest(my_list):
    if len(my_list)>1:
        m=my_list[0]
        for t in my_list:
            if t < m :
                sec=m
                m=t
        return sec
    return None  

print(find_second_smallest([5, 8, 3, 2, 6]))

def is_rotation(str_1: str, str_2: str) -> bool:
    if len(str_1) != len(str_2):
        return False
    
    if len(str_1) == 0:
        return False

    first_index_of_similar_part = None
    i_2 = 0
    for i_1 in range(0, len(str_1)):
        if str_1[i_1] == str_2[i_2]:
            if first_index_of_similar_part is None:
                first_index_of_similar_part = i_1
            i_2 += 1
        else:
            first_index_of_similar_part = None
            i_2 = 0

    if first_index_of_similar_part is None:
        return False
    
    for i_1 in range(0, first_index_of_similar_part):
        if str_1[i_1] != str_2[i_2]:
            return False
        
        i_2 += 1

    return True
    



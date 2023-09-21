def is_every_character_unique(string: str) -> bool:
    sorted_string = sorted(string)

    for i in range(1, len(sorted_string)):        
        if sorted_string[i] == sorted_string[i -1]:
            return False
        
    return True


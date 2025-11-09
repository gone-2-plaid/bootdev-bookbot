def get_num_words(input_list) :
    return len(input_list)

def character_count(input_string) :
    lower_string = input_string.lower()
    letters = list(lower_string)
    return_dict = {}
    for letter in letters :
        if letter not in return_dict :
            return_dict[letter] = 1
        else :
            return_dict[letter] += 1
    return return_dict

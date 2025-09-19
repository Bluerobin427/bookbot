def number_of_words_in_string(string_to_split):
    list_of_split_words = string_to_split.split()
    num_words = len(list_of_split_words)
    return num_words

def number_of_times_char_used(string_to_test):
    alphabet = "abcdefghijklmnopqrstuvwxyzæâêëô"
    result_dictionary = {}
    lowercase_str_to_test = string_to_test.lower()
    for letter in alphabet:
        result_dictionary[letter] = lowercase_str_to_test.count(letter)
    
    return result_dictionary

def sort_by(input):
    return input["num"]

def sorted_list_of_num_of_times_char_used(num_of_times_char_used):
    sorted_list = []
    #turn the input dictionary into a list of dictionaries, one dictionary for each character
    for key in num_of_times_char_used:
        sorted_list.append({"char": key, "num": num_of_times_char_used[key]})
    
    #sort the list based on the dictionary's "num" value, the number of times that character
    #was found in the book
    sorted_list.sort(reverse=True, key=sort_by)
    
    return sorted_list

def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def get_character_frequency(book_text):
    words = book_text.split()
    char_freq = {}

    for word in words:
        for ch in word:
            ch = ch.lower()
            if ch in char_freq:
                char_freq[ch] += 1
            else:
                char_freq[ch] = 1
    
    return char_freq

def sort_on(dict):
    return dict["frequency"]

def sort_char_freq(char_freq_dict):
    char_freq_list = []

    for char in char_freq_dict:
        freq = char_freq_dict[char]
        char_freq_list.append({"character": char, "frequency": freq})
    
    char_freq_list.sort(reverse=True, key=sort_on)
    return char_freq_list
    
    




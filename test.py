from collections import Counter

def unique_character(text):
    words = text.split()
    unique_letters = []
    
    for word in words:
        counter = Counter(word)
        for char in word:
            if counter[char] == 1:
                unique_letters.append(char)
                break
    
    counter = Counter(unique_letters)
    for char in unique_letters:
        if counter[char] == 1:
            return char
    
    return None  

input_text = "C makes it easy for you to shoot yourself in the foot. C++ makes that harder, but when you do, it blows away your whole leg. (с) Bjarne Stroustrup"
result = unique_character(input_text)
print(result)
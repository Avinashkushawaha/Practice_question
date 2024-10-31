def vowel_or_consonant(char):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', "u"]
    if char in vowels:
        vowel_list = []
        vowel_list.append(char)
        print(f"Vowels stored: {vowel_list}")
    else:
        print(f"Consonent ASCII: {ord(char)}")

vowel_or_consonant('b')        


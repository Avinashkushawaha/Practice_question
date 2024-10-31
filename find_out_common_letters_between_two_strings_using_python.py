def common_letter():
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")


    s1 = set(word1)
    s2 = set(word2)
    
    lst =s1 & s2
    print(lst)
common_letter()    
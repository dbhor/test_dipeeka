def FindVowel(str):
    print(str)
    vowels="AaEeIiOoUu"
    V = list(vowels)
    print(V)
    for i in str:
        if i in V:
            print(f"{i} is a vowel")
        else:
            print(f"{i} is consonant")






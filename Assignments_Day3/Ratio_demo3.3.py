def countofVowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count

def countofConsonants(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch.isalpha() and ch not in vowels:
            count += 1
    return count

def VoweltoConsonant_ratio(s):
    v = countofVowels(s)
    c = countofConsonants(s)
    
    if c == 0:
         print("Consonants count is zero, ratio not possible")
    else:
         return v / c

string = input("Enter a string: ")

ratio = VoweltoConsonant_ratio(string)
print("Ratio of vowels to consonants:", ratio)
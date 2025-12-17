def reverseString(s):
    return s[::-1]

def countVowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
            return count


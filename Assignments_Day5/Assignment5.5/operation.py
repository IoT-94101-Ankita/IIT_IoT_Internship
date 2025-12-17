from operations import __arithmetic__ , __string_ops

print("addition:", __arithmetic__.add(10, 5))
print("multiplication:", __arithmetic__.multiply(4, 3))

text = "today is a good day"
print("reversed String:", __string_ops.reverseString(text))
print("vowel Count:", __string_ops.countVowels(text))
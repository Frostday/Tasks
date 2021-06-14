from s2w_english.convert import convert_s2w

text = input("Enter spoken text: ")
out = convert_s2w(text)
print("Output: " + out)

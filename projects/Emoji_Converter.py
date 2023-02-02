message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😀",
    ":(": "😞",
    ":o": "😯"
}
output = ""
for i in words:
    output += emojis.get(i, i) + " "    # (i, i) is setting the key to the value
print(output)
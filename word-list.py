import re
file = open('file.txt', 'r')
# .lower() returns a version with all upper case characters replaced with lower case characters.
text = file.read().lower()
file.close()
# replaces anything that is not a lowercase letter, a space, or an apostrophe with a space:
text = re.sub('[^a-z\ \']+', " ", text)
words = list(text.split())
for word in words:
    if len(word) > 4:
        print(word)
    

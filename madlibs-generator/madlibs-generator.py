with open("story.txt", 'r') as f:
    story = f.read()

print(story)


words = set()
target_start = "<"
target_end = ">"

start_index = -1 

for i, char in enumerate(story):
    if char == "<":
        start_index = i
    if char == ">" and start_index != -1:
        words.add(story[start_index: i+1])

print(words)

answers = {}

for word in words:
    answer = input("Enter the word for "+word+": ")
    answers[word] = answer

print(answers)

for word in words:
    story = story.replace(word, answers[word])

print(story)





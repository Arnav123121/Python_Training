# WAP to count the word
# input = Arnav is good programmer

sentence = "Arnav is good programmer"
count = 1
for i in sentence:
    if i == " ":
        count += 1
    else:
        continue
print("Total number of words in the sentence is:- ", count)
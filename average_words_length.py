# For a given sentence, return the average word length. 
# Note: Remember to remove punctuation first.
sentence1 = "Hi all, my name is Tom...I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"

def average_words_length(sentence):
    for i in ",.;!?-_":
        sentence = sentence.replace(i,'')

    words = sentence.split()
    count = 0
    for j in words:
        count += len(j)
    return round(count / len(words),5) #round function to allow only 5 decimal spaces


print(average_words_length(sentence1))
print(average_words_length(sentence2))

print()

def avg_words_length_short(sentence):
    for i in ",.?!;'":
        sentence = sentence.replace(i, '')
    words = sentence.split()
    return round(sum(len(one_word) for one_word in words) / len(words),5)

print(avg_words_length_short(sentence1))
print(avg_words_length_short(sentence2))

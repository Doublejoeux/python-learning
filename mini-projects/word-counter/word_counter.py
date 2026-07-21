#word_counter
import re
def start():
    options= ["start", "quit"]
    start = input("Start or Quit: ").lower()
    if start not in options:
        print("Invalid")
        return True
    elif start == "quit":
        print("End")
        return False
    else:
        text = input("Input text: ").strip()
        if len(text) == 0:
            print("No words")
        else:    
            texts = text.split()
            print(f"total word count: {len(texts)}")
            print(f"total character count with spaces: {len(text)}")
            print(f"total character count without spaces: {len(text.replace(" ",""))}")
            words = re.findall(r'\b\w+\b', text.lower())
            word_freq = {}
            stopwords = {"and", "the", "to", "in", "are", "is", "a", "all", "but"}
            for word in words:
                if word not in stopwords:
                    word_freq[word]= word_freq.get(word, 0)+1
            sorted_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse= True)
            if len(sorted_freq) == 0:
                print("No Significant words found")
            else:    
                top_one = sorted_freq[0:1]
                for word, freq in top_one:
                    print(f"Most frequently used word is {word} and it was used {freq} times")
                top_three = sorted_freq[:3]
                for word, freq in top_three:
                    print(f"{word}: {freq}")
                total_length = sum(len(word) for word in words)
                average_length = total_length / len(words)
                print(f"Average word length: {average_length:.2f}")
        return True
def begin():
    begin = True
    while begin == True:
        begin = start()
begin()

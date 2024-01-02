import time

def word_by_word(text, speed):
    for word in text.split():
        print(word, end=" ", flush=True)
        time.sleep(speed)
    print("")
        
# Example
# Speed in seconds
word_by_word("Example Text, Hello World!", 0.5)

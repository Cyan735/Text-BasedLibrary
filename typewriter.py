import time

def typewriter(text, speed):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
    print("")

# Example
# Speed in seconds
typewriter("Example Text", 0.1)

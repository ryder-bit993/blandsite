import sys
import time


def typeit(text, speed=0.04, end="\n"):
    """Prints text character-by-character with flexible line ending."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write(end)
    sys.stdout.flush()

typeit("Do you want a seizure?")
answer=input(">")
if answer in ["Yes", "yes", "Yeah", "yeah"]:
    typeit("https://www.youtube.com/watch?v=V-KSyjmhwE0")
elif answer in ["no", "No", "Nah", "nah"]:
    typeit("Okay...")
    sys.exit
else:
    typeit("Okay...")

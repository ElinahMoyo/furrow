import sys
sys.path.insert(0, "./src")

from furrow import Plow
from furrow.detectors import NumberDetector, MultipleChoiceDetector

# Chaos text to test both numbers, letters, lookaheads, brackets, and sentences
text = "1. hi there, A) how are you? I have 500 grapes and 20. BTemple C. giant D you 3 things. 100. dont do this!"

# Pass both detectors into the array
engine = Plow(text, detectors=[NumberDetector, MultipleChoiceDetector])

engine.run()

print("TOKENS:")
print(engine.token)

print("\nCOLLECT:")
# Pretty print the list of dictionaries for easier scanning
for item in engine.collect():
    print(item)

print("\nRENDER:")
print(engine.render())

import sys
sys.path.insert(0,"./src")

from furrow import Plow
from furrow.detectors import NumberDetector
# from furrow import engine


text = "1. hi there, 2. how are you? I have 500 grapes and 20. there are 3 things. 100. dont do this!"

engine = Plow(text, detectors = [NumberDetector])

engine.run()
print("TOKENS:")
print(engine.token)


print("\nCOLLECT:")
print(engine.collect())


print("\nRENDER:")
print(engine.render())

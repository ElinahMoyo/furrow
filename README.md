# Furrow 

A lightweight, zero-dependency Python package to slice, group, and format messy text streams (like raw handwriting recognition outputs, chaotic OCR blocks, or unformatted LLM dumps) into separate lines without losing any of your data.

## Installation

```bash
pip install furrow
```

## How to Use It

To format your text cleanly, you need to call the engine's methods sequentially:

```python
from furrow import Plow

# 1. Feed it your raw, smashed-together text block
messy_text = "was1 . i was a girl19.There i with her 500 grapes .7. Amazing!"
engine = Plow(messy_text)

# 2. Run the character boundary scanner (Crucial step!)
engine.run()

# 3. Pull your questions out as a clean list of data blocks
print(engine.collect())
# Output: [{'question_number': '19', 'text': '.There i with her 500 grapes .'}, ...]

# 4. Generate the final text string with line breaks perfectly injected
print(engine.render())
# Output:
# was
# 1. i was a girl
# 19.There i with her 500 grapes .
# 7. Amazing!
```

## The Processing Sequence

Furrow processes your text strings in three distinct, lightweight steps:

*   **Step 1: `engine.run()` (The Tokenizer)** – Steps through your text character by character to find numbers. It maps out their exact start and end coordinates in the string.
*   **Step 2: `engine.collect()` (The Filter)** – Checks the distance between the numbers it found and trailing periods. This allows it to figure out the difference between inline data (like `500 grapes`) and actual question markers (like `19.`).
*   **Step 3: `engine.render()` (The Serializer)** – Uses the coordinate maps from the previous steps to slice into the original string and drop a clean newline (`\n`) right before your valid question indices. 

Everything that isn't a question (like titles, headers, or instructions) is kept completely safe, unmutated, and untouched.

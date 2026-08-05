# Furrow 

A lightweight, zero-dependency Python package to slice, group, and format messy text streams (like raw handwriting recognition outputs, chaotic OCR blocks, or unformatted LLM dumps) into separate lines without losing any of your data.

## Installation

```bash
pip install furrow
```

## How to Use It

To format your text cleanly, you need to call the engine's methods sequentially:

## How to Use It

To format your text cleanly, choose your detectors and call the engine's methods sequentially:

*   **`NumberDetector`**: Finds numbered items like `1.` or `20.` while safely ignoring normal numbers inside sentences (like `500 grapes`).

*   **`MultipleChoiceDetector`**: Finds letter choices `A` through `D` (handles `A.`, `A)`, or even glued text chunks like `BTemple`).


```python
from furrow import Plow
from furrow.detectors import NumberDetector, MultipleChoiceDetector

# 1. Feed it your raw, smashed-together text block

messy_text = "1. hi there, A) testing BTemple 3 things. 100. dont do this!"


engine = Plow(messy_text, detectors=[NumberDetector, MultipleChoiceDetector])

# 2. Run the character boundary scanner (Crucial step!)
engine.run()

# 3. Pull your questions out as a clean list of data blocks
print(engine.collect())

# Output: [{'marker': '1', 'marker_type': 'number', 'text': '. hi there, '}, {'marker': 'A', 'marker_type': 'multiple choice', 'text': ' test '}, ...]

# 4. Generate the final text string with line breaks perfectly injected
print(engine.render())

# Output:
# 1. hi there, 
# A) testing 
# BTemple 3 things. 
# 100. dont do this!
```

## The Processing Sequence

Furrow processes your text strings in three distinct, lightweight steps:

*   **Step 1: `engine.run()` (The Tokenizer)** – Steps through your text character by character using detectors to find numbers and alphanumeric choices. It maps out their exact start, end, and lookahead coordinates in the string.

*   **Step 2: `engine.collect()` (The Filter)** – Filters and clusters tokens based on text layouts. For numbers, it verifies the distance to trailing punctuation to ignore normal quantities (like `3 things`). For choices, it isolates un-spaced markers (like `BTemple`) and injects missing formatting periods.

*   **Step 3: `engine.render()` (The Serializer)** – Uses the coordinate maps from the previous steps to slice into the original string and drop a clean newline (`\n`) right before your valid list boundaries. 


Everything that isn't identified as a marker (like instructions, title headings, or random words) stays completely safe, untouched, and unmutated.

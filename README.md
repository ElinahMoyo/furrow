# Furrow 

A lightweight, zero-dependency Python package to extract, segment, and format structured question chains from unformatted, smashed-together text blocks (OCR, handwriting text dumps, unformatted LLM outputs, or transcripts) without data loss.

## Installation

```bash
pip install furrow
```

## Usage

```python
from furrow import Plow

# 1. Initialize with your raw string
messy_text = "was1 . i was a girl19.There i with her 500 grapes .7. Amazing!"
engine = Plow(messy_text)

# 2. Get questions as a list of dictionaries
print(engine.collect())
# [{'question_number': '19', 'text': '.There i with her 500 grapes .'}, ...]

# 3. Get the text layout with newlines safely injected
print(engine.render())
# Output:
# was
# 1. i was a girl
# 19.There i with her 500 grapes .
# 7. Amazing!
```

## How It Works

Furrow uses a single-pass state machine to parse and structure text layout:

* **State Tracking**: Steps through the text character by character to map the exact indices where number blocks start and end.

* **Noise Filtering**: Measures the distance between identified numbers and trailing periods. This allows it to separate inline data variables (like `500 grapes`) from actual question indices (like `19.`).
* **Data Safety**: Injects newline characters (`\n`) via string slicing. This ensures 100% data preservation of non-question text (headers, footers, intro text).

## API Reference

* **`engine.collect()`**: Compiles and returns a list of question data nodes for databases or JSON storage.
* **`engine.render()`**: Returns the full original text formatted with clean line breaks for UI display.

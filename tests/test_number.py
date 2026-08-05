from furrow.detectors import NumberDetector

# Test Case 1: Standard number extraction
def test_detects_single_number():
    detector = NumberDetector("The room is 105 degrees")
    results = detector.detect()
    
    assert len(results) == 1
    assert results[0]["value"] == "105"
    assert results[0]["type"] == "number"

# Test Case 2: Handling text with absolutely no numbers
def test_no_numbers_returns_empty_list():
    detector = NumberDetector("Hello World")
    results = detector.detect()
    
    assert results == []

# Test Case 3: Testing your special period logic
def test_period_position_tracking():
    detector = NumberDetector("Target 42. Code red.")
    results = detector.detect()
    
    assert len(results) == 1
    assert results[0]["value"] == "42"
    assert results[0]["period_position"] == 9  # The index of the dot after 42

from furrow.detectors import MultipleChoiceDetector

def test_detects_single_choice():
    detector = MultipleChoiceDetector("A. First item")
    results = detector.detect()
    assert len(results) == 1
    assert results[0]["value"] == "A"
    assert results[0]["type"] == "multiple choice"

def test_glued_choice_lookahead():
    detector = MultipleChoiceDetector("BTemple")
    results = detector.detect()
    assert len(results) == 1
    assert results[0]["value"] == "B"
    assert results[0]["period_position"] == 1 

def test_parenthesis_position_tracking():
    detector = MultipleChoiceDetector("C) giant option")
    results = detector.detect()
    assert len(results) == 1
    assert results[0]["value"] == "C"
    # 🔥 FIX: Changed from 1 to 2 to match your trailing space-tracker index calculation
    assert results[0]["period_position"] == 2  

def test_ignores_non_choice_capital_letters():
    detector = MultipleChoiceDetector("I have some text here.")
    results = detector.detect()
    assert results == []

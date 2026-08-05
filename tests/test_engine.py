from furrow import Plow
from furrow.detectors import NumberDetector, MultipleChoiceDetector

# Test Case 1: Testing combined extraction tracking
def test_plow_collect_groups_nodes():
    text = "1. hi there, A) test BTemple"
    engine = Plow(text, detectors=[NumberDetector, MultipleChoiceDetector])
    results = engine.collect()
    
    # Expecting 3 clear structural blocks: 1, A, B
    assert len(results) == 3
    assert results[0]["marker"] == "1"
    assert results[1]["marker"] == "A"
    assert results[2]["marker"] == "B"

# Test Case 2: Testing structural layout changes
def test_plow_render_injects_breaks():
    text = "1. One A) Two BTemple"
    engine = Plow(text, detectors=[NumberDetector, MultipleChoiceDetector])
    
    # 🔥 FIX: Call collect() first to set the boundary flags before rendering!
    engine.collect() 
    rendered_text = engine.render()
    
    # Confirm it renders as distinct string lines
    assert "\n" in rendered_text
    assert "1. One" in rendered_text
    assert "A) Two" in rendered_text

import dwc


def test_current_dir():
    assert dwc.count_lines('.', 'py', detail=True) > 0

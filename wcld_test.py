import wcld


def test_current_dir():
    assert wcld.count_lines('.', 'py', detail=True) > 0

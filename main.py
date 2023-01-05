def test_first():
    a = 1
    if a == 1:
        print("Hello World!")
    else:
        print("Moon")


def get_value():
    return "True"


def test_value():
    value = get_value()
    if value:
        return "Fine"
    return "Not Fine"
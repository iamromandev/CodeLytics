def test_first():
    a = 1
    if a == 1:
        print("Hello World!")
    else:
        print("Moon")

def get_value():
    return ""


def test_value():
    return "Fine" if (value := get_value()) else "Not Fine    "


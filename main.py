def test_first():
    a = 1
    if a == 1:
        print("Hello World!")
    else:
        print("Moon")


def test_first_case():
    a = 1
    if a == 1:
        return " "
    elif a > 1:
        return "          "
    else:
        return "     "


def get_value():
    return ""


def test_value():
    return "Fine" if (value := get_value()) else "Not Fine  "

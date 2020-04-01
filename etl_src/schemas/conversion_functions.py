true_set = {"T", 1, "1"}
false_set = {"F", 0, "0"}


def convert_bool(value):
    if value is None:
        return None
    elif value in true_set:
        return True
    elif value in false_set:
        return False


def skip_empty_string(value, conversion_func):
    if value == '':
        return None
    return conversion_func(value)


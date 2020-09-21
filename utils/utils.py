import random
import string


def get_random_string(length):
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def random_picker(choice_list):
    return random.choice(choice_list)


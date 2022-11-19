from random import randint, sample
from string import *
def get_random_password(length = 8) -> str:
    count_big_latters = randint(1, length - 2)
    count_small_latters = randint(1, length - count_big_latters -1)
    count_numbers = length - count_small_latters - count_big_latters
    return (''.join(sample(''.join(sample(ascii_uppercase, count_big_latters) +
            sample(ascii_lowercase, count_small_latters) +
            sample(digits, count_numbers)), length)))


print(get_random_password())

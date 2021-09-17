from random import choice
from string import ascii_letters, digits


def generate_string(size):
    char_choices = ascii_letters + digits
    return ''.join([choice(char_choices) for char in range(size)])


def get_short_url(instance, size):
    short_url = generate_string(size)
    if instance.__class__.objects.filter(short_url=short_url).exists():
        return get_short_url(size)
    return short_url

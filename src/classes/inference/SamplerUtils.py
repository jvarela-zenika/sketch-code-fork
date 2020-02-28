from __future__ import print_function
from __future__ import absolute_import
from lorem_text import lorem

import string
import random


class SamplerUtils:

    @staticmethod
    def get_random_title():
        return lorem.words(random.randrange(1, 4, 1)).upper()

    @staticmethod
    def get_random_link():
        return lorem.words(random.randrange(2, 5, 1))

    @staticmethod
    def get_random_paragraph():
        return lorem.paragraph()

    @staticmethod
    def get_random_text(length_text=10, space_number=1, with_upper_case=True):
        results = []

        lo

        while len(results) < length_text:
            char = random.choice(string.ascii_letters[:26])
            results.append(char)
        if with_upper_case:
            results[0] = results[0].upper()

        current_spaces = []
        while len(current_spaces) < space_number:
            space_pos = random.randint(2, length_text - 3)
            if space_pos in current_spaces:
                break
            results[space_pos] = " "
            if with_upper_case:
                results[space_pos + 1] = results[space_pos - 1].upper()

            current_spaces.append(space_pos)

        return ''.join(results)

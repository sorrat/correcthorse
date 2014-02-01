# -*- coding: utf-8 -*-
from os.path import abspath, dirname, join

from .xkcd_password import generate_wordlist, generate_xkcdpassword


this_dir = dirname(abspath(__file__))


def correcthorse(wordfile='2of12.txt',
                 word_min_length=4,
                 word_max_length=9,
                 n_words=4,
                 interactive=False,
                 acrostic=False,
                 delim=""):
    """
    Wrapper around `generate_xkcdpassword`.
    Generate password using file '2of12.txt' or '3esl.txt'
    included in the package.
    (Files downloaded from http://wordlist.sourceforge.net/)
    """
    mywords = generate_wordlist(
        wordfile=join(this_dir, wordfile),
        min_length=word_min_length,
        max_length=word_max_length,
    )
    return generate_xkcdpassword(
        wordlist = mywords,
        n_words = n_words,
        interactive = interactive,
        acrostic = acrostic,
        delim = delim
    )
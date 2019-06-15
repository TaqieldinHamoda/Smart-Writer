from random import choice, randint
from parts_of_speech import adjectives, adverbs, helping_verbs, verbs, typos, nouns, coordinate_conjunctions,\
     subordinate_conjunctions, articles

def get_adjective():
    return adjectives[randint(0, len(adjectives) - 1)]


def get_adverb():
    return adverbs[randint(0, len(adverbs) - 1)]


def get_noun():
    return nouns[randint(0, len(nouns) - 1)]


def get_verb():
    return verbs[randint(0, len(verbs) - 1)]


def get_helping_verb():
    return helping_verbs[randint(0, len(helping_verbs) - 1)]


def get_coordinate_conjunction():
    return coordinate_conjunctions[randint(0, len(coordinate_conjunctions) - 1)]


def get_subordinate_conjunction():
    return subordinate_conjunctions[randint(0, len(subordinate_conjunctions) - 1)]


def get_article():
    return articles[randint(0, len(articles) - 1)]


def get_typo(word):
    return typos.get(word, word)


def simple_writer(used: bool = False):  # Add support to adverbs, adjectives,

    sentence = [get_article() if randint(0, 1) else None, get_noun(), get_helping_verb() if randint(0, 1) else None,
                get_verb(), get_adverb() if randint(0, 1) else None, get_article() if randint(0, 1) else None,
                get_adjective() if randint(0, 1) else None, get_noun()]

    while None in sentence:
        sentence.remove(None)

    if randint(1, 10) <= 2:
        position = randint(0, len(sentence) - 1)
        sentence.insert(position, get_typo(sentence[position]))
        sentence.pop(position + 1)

    if used:
        return sentence
    return (" ".join(sentence) + ".").capitalize()


def compound_writer(used: bool = False):

    sentence = simple_writer(True) + [get_coordinate_conjunction()] + simple_writer(True)

    if used:
        return sentence
    return (" ".join(sentence) + ".").capitalize()


def complex_writer(used: bool = False):

    sentence = [get_article() if randint(0, 1) else None, get_noun(), get_helping_verb() if randint(0, 1) else None,
                get_verb(), get_adverb() if randint(0, 1) else None, get_subordinate_conjunction(), get_article() if
                randint(0, 1) else None, get_helping_verb() if randint(0, 1) else None, get_verb(), get_adverb() if
                randint(0, 1) else None,  get_adjective() if randint(0, 1) else None, get_noun()]

    while None in sentence:
        sentence.remove(None)

    for _ in range(5):
        if randint(1, 10) <= 2:
            position = randint(0, len(sentence) - 1)
            sentence.insert(position, get_typo(sentence[position]))
            sentence.pop(position + 1)

    if used:
        return sentence
    return (" ".join(sentence) + ".").capitalize()


def compound_complex_writer():

    return (" ".join(complex_writer(True) + [get_coordinate_conjunction()] + simple_writer(True)) + ".").capitalize()


def smart_writer(length: int, sentence_type: str = None):  # Mixes all the functions above.
    """
    int [, str] -> str

    Takes in how many sentences you want and, optionally, what type of sentence(s) you want.

    'sw' means simple sentence
    'cdw' means compound sentence
    'cxw' means complex sentence
    'ccw' means compound-complex sentence
    """

    sentences = ""
    condition = not sentence_type in ("sw", "cdw", "cxw", "ccw")

    for _ in range(length):

        if condition:
            sentence_type = choice(("sw", "cdw", "cxw", "ccw"))

        if sentence_type == "sw":
            sentences += simple_writer() + " "
        elif sentence_type == "cdw":
            sentences += compound_writer() + " "
        elif sentence_type == "cxw":
            sentences += complex_writer() + " "
        else:
            sentences += compound_complex_writer() + " "

    return sentences


if __name__ == "__main__":
    with open("trial.docx", "w") as word_file:
        word_file.write("Hello world")

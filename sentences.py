'''W05 Prove Assignment'''

import random


def get_determiner(grammatical_number):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "two", "some", "many".
    If grammatical_number == 1, this function will return
    either "the" or "one". Otherwise this function will
    return either "some" or "many".

    Parameter
        grammatical_number: an integer.
            If grammatical_number == 1, this function will return
            a determiner for a single noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """

    # single nouns
    if grammatical_number == 1:
        determiner = ["the", "one"]

    # plural nouns
    else:
        determiner = ["some", "many"]

    # Randomly choose and return a determiner.
    word = random.choice(determiner)
    return word


def get_noun(grammatical_number):
    """Return a randomly chosen noun.
    If grammatical_number == 1, this function will
    return one of these ten single nouns:
        "adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"
    Otherwise, this function will return one of these
    ten plural nouns:
        "adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"

    Parameter
        grammatical_number: an integer that determines
            if the returned noun is single or plural.
    Return: a randomly chosen noun.
    """

    # single nouns
    if grammatical_number == 1:
        noun = ["adult", "bird", "boy", "car", "cat",
                "child", "dog", "girl", "man", "woman"]
    # plural nouns
    else:
        noun = ["adults", "birds", "boys", "cars", "cats",
                "children", "dogs", "girls", "men", "women"]

    # Randomly choose and return a noun.
    word = random.choice(noun)
    return word


def get_verb(grammatical_number, tense):
    """Return a randomly chosen verb. If tense is "past", this
    function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and grammatical_number is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and grammatical_number is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameter
        grammatical_number: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """

    # print(type(tense),tense)
    # past words
    if tense == 'past':
        verb = ["drank", "ate", "grew", "laughed", "thought",
                "ran", "slept", "talked", "walked", "wrote"]

    # present words
    elif tense == 'present':
        if grammatical_number == 1:
            verb = ["drinks", "eats", "grows", "laughs", "thinks",
                    "runs", "sleeps", "talks", "walks", "writes"]

        elif grammatical_number != 1:
            verb = ["drink", "eat", "grow", "laugh", "think",
                    "run", "sleep", "talk", "walk", "write"]

    # future words
    elif tense == 'future':
        verb = ["will drink", "will eat", "will grow", "will laugh",
                "will think", "will run", "will sleep", "will talk",
                "will walk", "will write"]

    # Randomly choose and return a verb.
    word = random.choice(verb)
    return word


def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    prepositions = ["about", "above", "across", "after", "along",
                    "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for",
                    "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over",
                    "past", "to", "under", "with", "without"]

    # Randomly choose and return a preposition.
    word = random.choice(prepositions)
    return word


def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and nouns are singular or plural.
    Return: a prepositional phrase.
    """

    # string
    return f'{get_preposition()} {get_determiner(quantity)} {get_noun(quantity)}'


def main():

    print(f'a. {get_determiner(grammatical_number=1)} {get_noun(grammatical_number=1)} {get_verb(grammatical_number=1, tense="past")} {get_prepositional_phrase(quantity=1)}')
    print(f'b. {get_determiner(grammatical_number=2)} {get_noun(grammatical_number=2)} {get_verb(grammatical_number=2, tense="past")} {get_prepositional_phrase(quantity=2)}')
    print(f'c. {get_determiner(grammatical_number=1)} {get_noun(grammatical_number=1)} {get_verb(grammatical_number=1, tense="present")} {get_prepositional_phrase(quantity=1)}')
    print(f'd. {get_determiner(grammatical_number=2)} {get_noun(grammatical_number=2)} {get_verb(grammatical_number=2, tense="present")} {get_prepositional_phrase(quantity=2)}')
    print(f'e. {get_determiner(grammatical_number=1)} {get_noun(grammatical_number=1)} {get_verb(grammatical_number=1, tense="future")} {get_prepositional_phrase(quantity=1)}')
    print(f'f. {get_determiner(grammatical_number=2)} {get_noun(grammatical_number=2)} {get_verb(grammatical_number=2, tense="future")} {get_prepositional_phrase(quantity=2)}')


if __name__ == '__main__':
    main()

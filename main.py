import gradio as gr
from spellchecker import SpellChecker
from itertools import permutations



def Anagram(words):
    """
    A function that returns an anagram after filtering out the incorrect words.
    It also returns the given word passed to the function whether anagaram is
    generated or not.
    """
    randomize = randomizer(words)
    checker = spellChecker(words)
    # Because set returns only unique words. We convert the 'randomize' variable
    # to set so we can filter out the incorrect spellings from 'checker'
    anagram = set(randomize) - checker
    # we are now left with the correct word(s) as anagram
    return anagram


def spellChecker(word):
    """
    A function that scans a given word returned from the randomizer function for
    incorrect spellings and returns the wrong spellings.
    """
    checker = SpellChecker()
    randomize = randomizer(word)
    incorrect = checker.unknown(randomize)
    return incorrect


def randomizer(word):
    """
    A function to generate a combination of words from a given word passed to the function.
    It returns all the combination of words generated.
    """
    lists = []
    texts = permutations(word)
    #Permutation separated each word. Join them back together.
    for text in texts:
        lists.append(''.join(text))
    return lists



app = gr.Interface(fn=Anagram, inputs='text', outputs='text')

#launching the app
app.launch()


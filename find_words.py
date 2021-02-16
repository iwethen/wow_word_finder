# -*- coding: utf-8 -*-
from itertools import permutations


def make_all_possible_word_list(characters):
    characters_list = [char for char in characters]
    possible_words = []
    for i in range(3, len(characters) + 1):
        permutation_words_list = list(permutations(characters_list, i))
        possible_words += [''.join(word) for word in permutation_words_list]
    return set(possible_words)


def file_to_set(filename):
    with open(filename, 'r', encoding='UTF-8') as src:
        words_list = set(line.rstrip() for line in src)
    return words_list


def search_set(possible_words, all_turkish_words):
    found = []
    for word in possible_words:
        if word in all_turkish_words:
            found.append(word)
    return found


all_turkish_words = file_to_set('all_words.txt')
while 1:
    characters = input('Harfları giriniz! Kapatmak için q giriniz!\n').strip()
    if characters == 'q':
        break
    all_possible_combinations = make_all_possible_word_list(characters)
    founded_words = search_set(all_possible_combinations, all_turkish_words)
    founded_words = sorted(founded_words, key=len)
    for word in founded_words:
        print(word)

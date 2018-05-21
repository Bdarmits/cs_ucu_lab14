import timeit
import random
from linkedbst import LinkedBST


def get_dict(filename):
    '''
    :param filename: file to read from
    :return: list of words from file
    '''
    with open(filename) as f:
        dict_lst = []
        lines = f.readlines()
        c = 0
        for line in lines:
            dict_lst.append(line.strip())
    return dict_lst

def get_random_words(dict_lst):
    '''
    :param dict_lst: list of words
    :return: random 1000 words from list
    '''
    random_words = []
    for i in range(1000):
        word = random.choice(dict_lst)
        random_words.append(word)
    return random_words

def construct_tree(dict_lst, balance=False):
    '''
    :param dict_lst: list of words
    :param balance: True or False  of balance
    :return: tree based on list
    '''
    tree = LinkedBST(dict_lst)
    if balance:
        tree.rebalance()
    return tree

def search_list(lst, words):
    '''
    :param lst: list of words
    :param words: words to search
    :return:
    '''
    for i in range(len(words)):
        lst.index(words[i])


def search_tree(tree, words):
    '''
    :param tree: tree to search in
    :param words: words to search
    :return:
    '''
    """search binary tree for words"""
    for i in range(len(words)):
        tree.find(words[i])


if __name__ == '__main__':
    dict_lst = get_dict("dict_lst.txt")
    random_words = get_random_words(dict_lst)
    tree = construct_tree(random_words)
    balanced_tree = construct_tree(random_words, balance=True)
    search_list(dict_lst, random_words)
    search_tree(tree, random_words)
    search_tree(balanced_tree, random_words)
    print("Time to search list: ", timeit.timeit("search_list(dict_lst, random_words)",number=1,globals=globals()))
    print("Time to search tree: ", timeit.timeit("search_tree(tree, random_words)",number=1,globals=globals()))
    print("Time to search balanced tree: ", timeit.timeit("search_tree(balanced_tree, random_words)",number=1,globals=globals()))

# ex 1:

import random

def get_words_from_file(file):
    with open(file, mode= 'r') as file:
        word_list = file.readlines()
        word_list = [word.replace('\n','') for word in word_list] 
        print (word_list)

# get_words_from_file('/Users/el.sa/Desktop/Visual-Studio-Code/di-bootcamp/week-5/day-4/xp2-w5d4.txt')

def get_random_sentence(word_list, length):
    new_sentence = []
    for i in range(length):
        new_sentence.append(random.choice(word_list))
    return new_sentence

get_random_sentence('/Users/el.sa/Desktop/Visual-Studio-Code/di-bootcamp/week-5/day-4/xp2-w5d4.txt',10)


def main():
    print('This program print random sentence with the length that we want')
    x = int(input('how long you want the sentence to be, between 2 and 20?'))
    if x < 2:
        print('error')
    elif x> 20:
        print('error')
    else: 
        print(get_random_sentence('/Users/el.sa/Desktop/Visual-Studio-Code/di-bootcamp/week-5/day-4/xp2-w5d4.txt',x))

main()




# ex 2:



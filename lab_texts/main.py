from operator import length_hint
import string
import random

def load_words(dict_path):
    words = []
    with open(dict_path) as word_file:
        for line in word_file:
            words.append(line.split()[0])
    return words


def load_meaningful_text(text_path):
    with open(text_path) as file:
        text = file.read().replace('\n', ' ').replace('\r', ' ')
    return text


def generate_random_letters_string(length):
    letters_and_space = string.ascii_letters + ' '
    crypt_rand_string = ''.join(random.choice(letters_and_space) for _ in range(length))
    return crypt_rand_string


def generate_random_words_string(length, dict):
    str = ''
    for _ in range(length):
        rand = random.choice(dict)
        while (rand in str):
            rand = random.choice(dict)
        str += rand
        str += ' '
    str = str[:-1]
    return str
            

def compare_two_texts(text1, text2):
    length = min(len(text1), len(text2))
    cnt = 0
    for i in range(length):
        if text1[i] == text2[i]:
            cnt += 1
    return cnt / length


if __name__ == "__main__":
    # file_paths
    dict_path = 'D:/MAI_Study/Cryptography/lab_texts/words_alpha.txt'
    tale1_path = 'D:/MAI_Study/Cryptography/lab_texts/fairy_tale1.txt'
    tale2_path = 'D:/MAI_Study/Cryptography/lab_texts/fairy_tale2.txt'
    
    # initializing
    english_words = load_words(dict_path)
    text1 = load_meaningful_text(tale1_path)
    text2 = load_meaningful_text(tale2_path)
    rand_words1 = generate_random_words_string(text1.count(' ') + 1, english_words)
    rand_words2 = generate_random_words_string(1000, english_words)
    rand_letters1 = generate_random_letters_string(len(text2))
    rand_letters2 = generate_random_letters_string(1000)

    # comparing
    percentage_of_matches1 = compare_two_texts(text1, text2)
    percentage_of_matches2 = compare_two_texts(text2, rand_letters1)
    percentage_of_matches3 = compare_two_texts(text1, rand_words1)
    percentage_of_matches4 = compare_two_texts(rand_letters1, rand_letters2)
    percentage_of_matches5 = compare_two_texts(rand_words1, rand_words2)
    print('---------------------------------------------------------------------------------------------')
    print(f'Percentage of matches for two meaningful texts = {percentage_of_matches1}')
    print('---------------------------------------------------------------------------------------------')
    print(f'Percentage of matches for meaningful text and text from random letters = {percentage_of_matches2}')
    print('---------------------------------------------------------------------------------------------')
    print(f'Percentage of matches for meaningful text and text from random words = {percentage_of_matches3}')
    print('---------------------------------------------------------------------------------------------')
    print(f'Percentage of matches for two texts from random letters = {percentage_of_matches4}')
    print('---------------------------------------------------------------------------------------------')
    print(f'Percentage of matches for two texts from random words = {percentage_of_matches5}')
    print('---------------------------------------------------------------------------------------------')

    # optimal text length
    lengths = [10, 100, 1000, 10000, 100000]
    for i in range(len(lengths)):
        rand_words_text1 = generate_random_words_string(lengths[i], english_words)
        rand_words_text2 = generate_random_words_string(lengths[i], english_words)
        matches = compare_two_texts(rand_words_text1, rand_words_text2)
        print(f'Percentage of matches for two texts from random words, which have {lengths[i]} words: {matches}')
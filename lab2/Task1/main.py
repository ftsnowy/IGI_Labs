import re
from constants import END_MARKS, NON_END_MARKS


def remove_punctuation(text):
    return "".join(list(filter(lambda x: x not in END_MARKS + NON_END_MARKS, text.strip())))


def is_word(word):
    return word.isalnum() and not word.isdigit()


def is_sentence(sentence):
    sentence = remove_punctuation(sentence)
    return len(list(filter(is_word, sentence))) > 0


def get_words(text):
    text = re.sub(r"[!?.,;:-]", ' ', text)
    words = list(filter(is_word, text.split()))
    return words


def count_word_characters(text):
    words = get_words(text)
    s = 0
    for word in words:
        s += len(word)
    return s


def average_word_length(text: str) -> float:
    words = get_words(text)
    characters = count_word_characters(text)
    try:
        return characters / len(words)
    except ZeroDivisionError:
        return 0


def average_sentence_length(text):
    try:
        return count_word_characters(text) / count_sentences(text)
    except ZeroDivisionError:
        return 0


def count_sentences(text):
    return len(re.findall(r'(?<=\w)+([?!.])+(?= |$)', text))


def count_non_declarative(text: str) -> int:
    total_sentences = re.findall(r'(?<=\w)+([?!.])+(?= |$)', text)
    decl_sentences = re.findall(r'(?<=\w)+([.])+(?= |$)', text)
    return len(total_sentences) - len(decl_sentences)


def top_n_grams(text, n=4, k=10):
    words = get_words(text)
    n_grams = tuple(" ".join(words[i:i+n]) for i in range(len(words)) if i + n <= len(words))
    ngram_count = {}
    for ngram in n_grams:
        if ngram in ngram_count:
            ngram_count[ngram] += 1
        else:
            ngram_count[ngram] = 1
    top_ngrams = sorted(ngram_count.items(), key=lambda x: x[1], reverse=True)[:k]
    answer = []
    for gram in top_ngrams:
        answer.append(gram[0])
    return answer


def main():
    file = open('text.txt', encoding='utf-8')
    text = file.read()
    print(text)
    n = 4
    k = 10
    print("Numbers of sentences in the text = ", count_sentences(text))
    print("Numbers of non-declarative sentences in the text = ", count_non_declarative(text))
    print("Average length of sentences = ", average_sentence_length(text))
    print("Average length of the word in the text = ", average_word_length(text))
    print("top-K repeated N-grams in the text = ", top_n_grams(text))


if __name__ == '__main__':
    main()



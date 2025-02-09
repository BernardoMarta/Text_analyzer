import re
from collections import Counter
from langdetect import detect_langs, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
import langcodes
from textblob import TextBlob

#Constant
DetectorFactory.seed = 0

def main():

    print('\n')
    print('='*90)
    print('Text Analyzer'.center(90))
    print('='*90)
    print('\n')

    text = input('Text: ')
    print('\n')

    count_sentences(text)
    count_words(text)
    number_all_chars(text)
    number_chars_no_spaces(text)
    most_frequent_words(text, n=5)
    get_language(text)
    if (most_prob_language == 'English'): #it only works well in english
        analyze_sentiment(text)

    print('\n')


def count_sentences(text):
    sentences = re.split(r'\. |\.\.\. |\? |\!', text)
    number_sentences = len(sentences)
    print(f'Number of sentences: {number_sentences}')
    return number_sentences

def count_words(text):
    global words
    words = re.findall(r'\b\w+\b', text.lower())
    print(f'Number of words: {len(words)}')
    return len(words)

def number_all_chars(text):
    print(f'Number of all chars: {len(text)}')
    return len(text)

def number_chars_no_spaces(text):
   text_wtout_spaces = text.replace(' ','')
   print(f'Number of characters without spaces: {len(text_wtout_spaces)}')
   return len(text_wtout_spaces)

def most_frequent_words(text, n=5):
    word_counts = Counter(re.findall(r'\b\w+\b', text.lower()))
    most_common = word_counts.most_common(n)
    print(f"Most frequent {n} words:")
    for word, count in most_common:
        print(f"- {word}: {count} times")
    return most_common

def get_language(text):
    try:
        most_prob_language_code = detect_langs(text)[0]
        global most_prob_language
        most_prob_language = langcodes.Language.make(most_prob_language_code.lang).display_name()
        if round(most_prob_language_code.prob,2)*100 < 98:
            print('The model cannot detect the language with enough accuracy. Please enter a longer text.')
            return 0
        print(f'Language: {most_prob_language} (probability: {round(most_prob_language_code.prob,1)*100})%')
        return most_prob_language

    except LangDetectException:
        print('There is an error with language detection. Insert a longer text.')

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        print("Sentiment: Positive")
    elif sentiment < 0:
        print("Sentiment: Negative")
    else:
        print("Sentiment: Neutral")
    return sentiment


if __name__ == "__main__":
    main()

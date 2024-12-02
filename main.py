import nltk
#nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize, sent_tokenize
import pymorphy2


morph = pymorphy2.MorphAnalyzer()
with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

print("Исходный текст:")
print(text)

# Сегментация текста на предложения
sentences = sent_tokenize(text)

print("\nИтог:")
for sentence in sentences:
    words = word_tokenize(sentence)
    for index in range(len(words) - 1):
        word_first = words[index]
        word_second = words[index + 1]
        
        parse_first = morph.parse(word_first)[0]
        parse_second = morph.parse(word_second)[0]
        
        # Проверка, что слова являются существительными или прилагательными
        if (
            (parse_first.tag.POS in {'NOUN', 'ADJF'}) and
            (parse_second.tag.POS in {'NOUN', 'ADJF'})
        ):
            # Проверка падежа, рода и числа
            if (
                parse_first.tag.case == parse_second.tag.case and
                parse_first.tag.gender == parse_second.tag.gender and
                parse_first.tag.number == parse_second.tag.number
            ):
                print(parse_first.normal_form, parse_second.normal_form)

def remove_extra_spaces(sentence):
    words = sentence.split()  # Разделение строки на слова
    cleaned_sentence = " ".join(words)  # Объединение слов с одним пробелом между ними
    return cleaned_sentence


text = "    Это       строка     с  лишними пробелами."
cleaned_text = remove_extra_spaces(text)
print(cleaned_text)
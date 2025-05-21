from string import punctuation


def read_file(filepath):
    with open(filepath, 'r') as f:
        file_contents = f.read()

        return file_contents


def clean_text(text):
    cleaned_text = text.translate(str.maketrans('', '', punctuation)).lower()

    return cleaned_text


def count_words(text):
    words = text.split()
    word_count_dict = {}

    for word in words:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1

    return word_count_dict


def top_ten_words(my_dict, n=10):
    sorted_dict = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)

    return sorted_dict[:n]

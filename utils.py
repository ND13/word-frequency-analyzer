from string import punctuation


def read_file(filepath):
    try:
        with open(filepath, 'r') as f:
            file_contents = f.read()

    except IOError as error:
        print('An error occurred, check file path and file name.')
        print(error)

    else:
        return file_contents


def clean_text(text):
    cleaned_text = text.translate(str.maketrans('', '', punctuation)).lower()

    return cleaned_text


def count_words(text):
    words = text.split()
    word_count_dict = {}

    stopwords = ["—", "a", "an", "and", "the", "of", "in", "on", "for", "to", "with", "by", "at", "is", "it", "this", "that", "be", "as", "from"]

    for word in words:
        if word in stopwords:
            continue
        else:
            word_count_dict[word] = word_count_dict.get(word, 0) + 1

    return word_count_dict


def top_ten_words(my_dict, n=10):
    sorted_dict = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)

    return sorted_dict[:n]

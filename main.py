from utils import read_file, clean_text, count_words, top_ten_words


def main():
    filepath = './samples.txt'

    text = read_file(filepath)

    cleaned_text = clean_text(text)

    word_count = count_words(cleaned_text)

    top_words = top_ten_words(word_count, n=10)

    for word, count in top_words:
        print(f'{word}: {count}')


if __name__ == '__main__':
    main()

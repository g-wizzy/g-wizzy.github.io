from filtering import is_good_word



if __name__ == "__main__":
    
    good_words = []
    def handle_line(line: str) -> str:
        word, pronunciation = line.split(";")[:2]
        if is_good_word(pronunciation):
            return word

    with open("words.dat", "r") as input_file:
        good_words = map(handle_line, input_file.readlines())

    good_words = (word for word in good_words if word is not None)

    with open("good_words.raw", "w") as output_file:
        for line in good_words:
            for word in line.split(","):
                output_file.write(f"{word}\n")
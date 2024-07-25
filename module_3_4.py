def single_root_words(root_word, *other_words):
    same_words = []
    other_words = list(other_words)
    for i in range(len(other_words)):
        root_word = root_word.lower()
        other_word = other_words[i].lower()
        if other_word in root_word or root_word in other_word:
            same_words.append(other_words[i])
    print(same_words)


single_root_words ('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
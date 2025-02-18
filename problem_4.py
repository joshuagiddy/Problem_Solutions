def count_character_in_sentence(sentence, character):
    count = 0
    for c in sentence:
        if c == character:
            count += 1
    return count


sentence = input("Enter a sentence: ")
character = input("Enter a character: ")
print(count_character_in_sentence(sentence, character))



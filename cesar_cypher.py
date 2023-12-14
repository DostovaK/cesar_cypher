"""This program is capable of encrypting and decrypting text
   according to the Caesar algorithm. Please note that functions use ASCII."""

phrase = input('Input a phrase:')


def option_validation():
    """Function that validates options: en- or decryption.
       A user should choose one option."""
    while True:
        option = input('Enter "e" for encryption or "d" for decryption.')
        if option.lower() == 'e' or option.lower() == 'd':
            return option
        else:
            continue


def key_validation():
    """Function that validates substitution cipher.
       It should be a number."""
    while True:
        key = input('Please enter a key. It should be a number.')
        if key.isdigit():
            return key
        else:
            continue


def language_validation():
    """Function that validates language options: english or russian.
       A user should choose one option."""
    while True:
        language = input('Enter "rus" for russian or "eng" for english.')
        if language.lower() == 'rus' or language.lower() == 'eng':
            return language
        else:
            continue


def decryption(
        upper_letter_min, upper_letter_max, lower_letter_min, lower_letter_max
):
    """Function that decrypts a message using ASCII.
    Punctuation marks as well as special signs stay the same."""
    key = key_validation()
    output_result = ''
    for i in range(len(phrase)):
        if (
            32 <= ord(phrase[i]) <= 64 or 91 <= ord(phrase[i]) <= 96
            or 123 <= ord(phrase[i]) <= 126
        ):  # check if it is a punctuation mark or special sign
            output_result += phrase[i]  # if true, just add a character to final sentence
        n = ord(phrase[i]) - int(key)  # replace a character with a decripted one using substitution cipher
        if phrase[i].isupper():  # if a character is capital one than replace it also with capital
            if n < upper_letter_min:  # if a character is out of ASCII range than continue to count it from the range start
                n = upper_letter_max - (upper_letter_min - 1 - n)
            output_result += chr(n)
        if phrase[i].islower():  # same, but with lowercase characters
            if n < lower_letter_min:
                n = lower_letter_max - (lower_letter_min - 1 - n)
            output_result += chr(n)
    return output_result


def encryption(
        upper_letter_min, upper_letter_max, lower_letter_min, lower_letter_max
):
    """Function that encrypts a message using ASCII.
    Punctuation marks as well as special signs stay the same."""
    key = key_validation()
    output_result = ''
    for i in range(len(phrase)):
        if (
            32 <= ord(phrase[i]) <= 64 or 91 <= ord(phrase[i]) <= 96
            or 123 <= ord(phrase[i]) <= 126
        ):  # generally, same situation, but now you are scaling to another side of range
            output_result += phrase[i]
        n = ord(phrase[i]) + int(key)
        if phrase[i].isupper():
            if n > upper_letter_max:
                n = upper_letter_min + (n - (upper_letter_max + 1))
            output_result += chr(n)
        if phrase[i].islower():
            if n > lower_letter_max:
                n = lower_letter_min + (n - (lower_letter_max + 1))
            output_result += chr(n)
    return output_result


def choose_option():
    """This function is main and gatheres all crucial data."""
    option = option_validation()
    language = language_validation()
    if language == 'eng':
        if option == 'e':
            print(encryption(65, 90, 97, 122))  # English encryption
        else:
            print(decryption(65, 90, 97, 122))  # English decryption
    else:
        if option == 'e':
            print(encryption(1040, 1071, 1072, 1103))  # Russian encryption
        else:
            print(decryption(1040, 1071, 1072, 1103))  # Russian decryption


def main():
    choose_option()


if __name__ == "__main__":
    main()

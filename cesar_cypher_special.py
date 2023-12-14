"""In case you would like to encrypt the phrase using the length of each word,
   please use this piece of code. Each word of the string is encrypted
   in cyclic shift by the length of that word.
   """

phrase = input('Input a phrase:').split()
output_result = ''

for j in range(len(phrase)):
    not_letters_counter = 0

    for k in range(len(phrase[j])):
        if phrase[j][k] in ',!.{[''}/]"?<>_-':
            not_letters_counter += 1

    for i in range(len(phrase[j])):
        if (
            32 <= ord(phrase[j][i]) <= 64 or 91 <= ord(phrase[j][i]) <= 96
            or 123 <= ord(phrase[j][i]) <= 126
        ):
            output_result += phrase[j][i]
        n = ord(phrase[j][i]) + int(len(phrase[j]) - not_letters_counter)
        if phrase[j][i].isupper():
            if n > 90:
                n = 65 + (n - (90 + 1))
            output_result += chr(n)
        if phrase[j][i].islower():
            if n > 122:
                n = 97 + (n - (122 + 1))
            output_result += chr(n)
    output_result += ' '


def main():
    print(output_result)


if __name__ == "__main__":
    main()

# You may use following sentences for testing:
# Day, mice. "Year" is a mistake!
# Result: Gdb, qmgi. "Ciev" ku b tpzahrl!
# my name is Python!
# Result: oa reqi ku Veznut!

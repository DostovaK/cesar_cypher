"""In case you do not know the key for decryption,
   you can use this code for enumeration of options
   and then choose the most suitable one.
   26 is the number of letters in english alphabet. """

phrase = input("Please enter a phrase.")
for k in range(1, 26):
    key = k
    output_result = ''
    for i in range(len(phrase)):
        if (
            32 <= ord(phrase[i]) <= 64 or 91 <= ord(phrase[i]) <= 96
            or 123 <= ord(phrase[i]) <= 126
        ):
            output_result += phrase[i]
        n = ord(phrase[i]) - int(key)
        if phrase[i].isupper():
            if n < 65:
                n = 90 - (64 - n)
            output_result += chr(n)
        if phrase[i].islower():
            if n < 97:
                n = 122 - (96 - n)
            output_result += chr(n)
    print(output_result)

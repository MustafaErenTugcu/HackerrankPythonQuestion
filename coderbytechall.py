def EquivalentKeypresses(strArr):
    def process_keypresses(keypresses):
        output = []
        for char in keypresses:
            if char == "-B":
                if output:
                    output.pop()
            else:
                output.append(char)
        return ''.join(output)

    str1, str2 = strArr

    printable_str1 = process_keypresses(str1.split(','))
    printable_str2 = process_keypresses(str2.split(','))

    return str(printable_str1 == printable_str2).lower()

# keep this function call here 
print(EquivalentKeypresses(input()))
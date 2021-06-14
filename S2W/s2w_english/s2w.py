rules = {
    "Numbers":
    {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
        "hundred": 100
    },
    "Tuples":
    {
        "single": 1,
        "double": 2,
        "triple": 3,
        "quadruple": 4,
        "quintuple": 5,
        "sextuple": 6,
        "septuple": 7,
        "octuple": 8,
        "nonuple": 9,
        "decuple": 10
    },
    "General":
    {
        "C M": "CM",
        "P M": "PM",
        "D M": "DM",
        "A M": "AM"
    }
}


class Spoken2Written:
    def __init__(self, text):
        self.rules = rules
        self.input = text
        self.output = ''

    def convert(self):
        words = self.input
        words = words.replace(".", " .")
        words = words.replace(",", " ,")
        words = words.split()
        i = 0
        numbers = self.rules['Numbers']
        tuples = self.rules['Tuples']
        general = self.rules['General']
        while i < len(words):
            if i+1 == len(words):
                self.output = self.output + " " + words[i]
                i = i+1
            else:
                word = words[i]
                next_word = words[i+1]
                if word.lower() in numbers.keys() and (next_word.lower() == 'dollars' or next_word.lower() == 'dollar'):
                    self.output = self.output + \
                        " $"+str(numbers[word.lower()])
                    i = i+2
                elif word.lower() in tuples.keys() and len(next_word) == 1:
                    self.output = self.output + \
                        " "+(next_word*tuples[word.lower()])
                    i = i+2
                elif (word+" "+next_word) in general.keys():
                    self.output = self.output+" "+word+next_word
                    i = i+2
                else:
                    self.output = self.output+" "+words[i]
                    i = i+1
        self.output = self.output.replace(" .", ".")
        self.output = self.output.replace(" ,", ",")
        self.output = self.output[1:]


def convert_s2w(text):
    obj = Spoken2Written(text)
    obj.convert()
    return obj.output


# convert_s2w('triple A')

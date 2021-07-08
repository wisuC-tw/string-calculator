import re


class StringCalculator():
    def __init__(self) -> None:
        pass

    def parse(self, number_string, delimiter=',|\n'):
        # split by comma or newline
        return re.split(delimiter, number_string)

    def extract_delimiter(self, input_string):
        if input_string == '':
            return '', ''
        elif input_string[:2] == '//':
            result = input_string.split('\n')
            delimiter = result[0][-1]
            number_string = result[1]
            return delimiter, number_string
        else:
            return '', input_string

    def add(self, input_string):
        delimiter, number_string = self.extract_delimiter(input_string)

        if number_string == "":
            return 0

        if delimiter == '':
            number_strings = self.parse(number_string)
        else:
            number_strings = self.parse(number_string, delimiter)

        return sum([int(num) for num in number_strings])

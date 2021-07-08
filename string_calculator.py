import re


class StringCalculator():
    def __init__(self) -> None:
        pass
    
    def parse(self, number_string, delimiter=',|\n'):
        # split by comma or newline
        return re.split(delimiter, number_string)

    def extract_delimiter(self, input_string):
        if input_string == '':
            return ('', '')
        elif input_string[:2] == '//': # contains delimiter
            result = input_string.split('\n')
            delimiter = result[0][-1]
            number_string = result[1]
            return (delimiter, number_string)
        else:
            return ('', input_string)
        
        # Regex = f”//{delimiter}\n{.+}”
        # f'([0-9{delimiter}]+)'

        # return (a, b)

    def add(self, number_string):
        if number_string == "":
            return 0
        
        number_strings = self.parse(number_string)
        numbers = [int(num) for num in number_strings]

        return sum(numbers)

    def calculate(self, input_string):
        delimiter, number_string = self.extract_delimiter(input_string)
        if delimiter == '':
            number_strings = self.parse(number_string)
        else:
            number_strings = self.parse(number_string, delimiter)
        
        numbers = [int(num) for num in number_strings]

        return sum(numbers)
        
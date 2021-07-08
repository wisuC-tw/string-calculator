import re


class StringCalculator():
    def __init__(self) -> None:
        pass
    
    def parse(self, number_string, delimiter=',|\n'):
        # split by comma or newline
        return re.split(delimiter, number_string)

    def extract_delimiter(self,input_string):
        pass

    def add(self, number_string):
        if number_string == "":
            return 0
        
        number_strings = self.parse(number_string)
        numbers = [int(num) for num in number_strings]

        return sum(numbers)
 
import inflect

class Converters:
    """This class includes two methods for converting numbers.
    
    StandardFormat: Converts an integer into a string with comma separators.
    NumberToWords: Converts a string representation of a number into words.
    """
    def StandardFormat(num: int):
        """Converts an integer into a string with comma separators.
        
        Args:
        num: int, the number to be converted.
        
        Returns:
        str: The string representation of the number with comma separators.
        """
        return "{:,}".format(num)
    
    def NumberToWords(num: int):
        """Converts a string representation of a number into words.
        
        Args:
        num: str, the string representation of the number to be converted.
        
        Returns:
        str: The string representation of the number in words.
        """
        p = inflect.engine()
        return p.number_to_words(num).title()

def AllResults(num: int):
    """Converts an integer into both a string with comma separators and a string representation of the number in words.
    
    Args:
    num: int, the number to be converted.
    
    Returns:
    dict: A dictionary with two keys: "standard" (the string representation of the number with comma separators) and "word" (the string representation of the number in words).
    """
    StandardFormat = Converters.StandardFormat(num=num)
    Worded = Converters.NumberToWords(StandardFormat)
    return{
        "standard": StandardFormat,
        "word": str(Worded)
    }
import inflect
class Converters:
    def StandardFormat(num:int):
        return "{:,}".format(num)
    def NumberToWords(num:int):
        p = inflect.engine()
        return p.number_to_words(num).title()
def AllResults(num:int):
    StandardFormat=Converters.StandardFormat(num=num)
    Worded=Converters.NumberToWords(StandardFormat)
    return{
        "standard": StandardFormat,
        "word": str(Worded)
    }

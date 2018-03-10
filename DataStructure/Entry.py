from Parsing.ParseError import ParseError


class Entry:
    def __init__(self, wave_type, onset, offset, tags):
        self.type = wave_type
        if wave_type not in ["P", "QRS", "T", "INV"]:
            raise ParseError("Type " + wave_type + " is not valid")
        self.onset = onset
        self.offset = offset
        self.tags = tags

    def is_tagged_with(self, tag):
        if tag in self.tags:
            return True
        return False


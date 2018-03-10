from Parsing.ParseError import ParseError


class Entry:
    def __init__(self, type, onset, offset, tags):
        self.type = type
        if type not in ["P", "QRS", "T", "INV"]:
            raise ParseError("Type " + type + " is not valid")
        self.onset = onset
        self.offset = offset
        self.tags = tags

    def is_tagged_with(self, tag):
        if tag in self.tags:
            return True
        return False


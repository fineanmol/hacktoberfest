class StringReverser:
    def __init__(self, original):
        self.original = original
        self.reversed = ""

    def reverse_recursive(self, s=None):
        if s is None:
            s = self.original
        if len(s) == 0:
            return ""
        return self.reverse_recursive(s[1:]) + s[0]

    def reverse_with_unicode(self):
    
        import unicodedata
        normalized = unicodedata.normalize('NFC', self.original)
        self.reversed = ''.join(reversed([char for char in normalized]))
        return self.reversed

    def reverse(self):
        
        if any(ord(c) > 127 for c in self.original):
            return self.reverse_with_unicode()
        else:
            self.reversed = self.reverse_recursive()
            return self.revers
text = "¡Hola! 👋🏼"
reverser = StringReverser(text)
print("Original:", text)
print("Reversed:", reverser.reverse())

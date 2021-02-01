class Translator():
    def __init__(self):
        self.data={"zh":"I am chinese",
                    "ar":"I am egyptian"}

    def translate(self, src, tgt, text):
        return self.data[tgt]

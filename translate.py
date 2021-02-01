class Translator():
    def __init__(self):
        self.data={"zh":"I am chinese",
                    "ar":"I am egyptian"}
        self.langs = ["zh -> ar" , "ar -> zh", "ar -> fr" , "fr -> ar"]

    def supported_languages(self):
        return self.langs

    def translate(self, src, tgt, text):
        return self.data[tgt]

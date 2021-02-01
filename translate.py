from fairseq.models.transformer import TransformerModel
from tqdm import tqdm
from farasa.segmenter import FarasaSegmenter
import pandas as pd
import numpy as np


class Translator():
    def __init__(self):
        self.data={"zh":"I am chinese",
                    "ar":"I am egyptian"}
        self.langs = ["zh -> ar" , "ar -> zh", "ar -> fr" , "fr -> ar"]

    def supported_languages(self):
        return self.langs

    def translate(self, src, tgt, text):
        return self.data[tgt]

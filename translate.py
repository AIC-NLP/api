from fairseq.models.transformer import TransformerModel
from farasa.segmenter import FarasaSegmenter
import re


class Translator():
    def __init__(self):
        
        self.langs = ["zh -> ar" , "ar -> zh", "ar -> fr" , "fr -> ar"]
        self.segmenter = FarasaSegmenter(interactive=True)
        self.models = {
            "ar2zh": TransformerModel.from_pretrained(
                "/home/nlp-mt-rowan-api/mt-api/checkpoints/checkpoints_ar2zh",
                checkpoint_file='/home/nlp-mt-rowan-api/mt-api/checkpoint_best.pt',
                data_name_or_path='/home/nlp-mt-rowan-api/mt-api/data-bin',
                bpe='subword_nmt',
                bpe_codes='/home/nlp-mt-rowan-api/mt-api/data-bin/code'
            ),
            "zh2ar": TransformerModel.from_pretrained(
                "/home/nlp-mt-rowan-api/mt-api/checkpoints/checkpoints_zh2ar",
                checkpoint_file='/home/nlp-mt-rowan-api/mt-api/checkpoint_best.pt',
                data_name_or_path='/home/nlp-mt-rowan-api/mt-api/data-bin',
                bpe='subword_nmt',
                bpe_codes='/home/nlp-mt-rowan-api/mt-api/data-bin/code'
            )
        }

    def supported_languages(self):
        return self.langs

    def translate(self, src, tgt, text):
        # chinese is segmented arabic is not
        src2trg = src + "2" + tgt
        model = self.models[src2trg]
        model.cuda()
        if src == "ar":
            text = self.segment_ar(text)
            text = text.replace("+", "+ ")
        output = model.translate(text)
        if tgt == "ar":
            output = output.replace("+ ", "")
        return output

        

    def segment_ar(self, sent: str):
        segmented = self.segmenter.segment(sent)
        toks = segmented.split(" ")
        ret_sent = ""
        for tok in toks:
            segments = re.split("(?<=[+])", tok)
            for i in range(len(segments)):
                ret_sent = ret_sent + segments[i] + " "
        ret_sent = ret_sent.strip()


        return ret_sent

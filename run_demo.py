import requests
import json

translation_api_url= 'http://MT_API/translate'

def translate_request(txt, src, tgt):
    payload = {"text":txt,  "source":src,  "target":tgt}
    headers = {'Content-Type': 'application/json'}
    res = requests.post(translation_api_url, json=payload, headers=headers)
    return res.json()['output']
    

def main():
    # input.txt is an arabic file
    f_input = open("input.txt",'r')

    # files of the output of translation from ar --> (en, fr, zh)
    # f_output_en = open("output.en",'w')
    f_output_fr = open("output.fr",'w')
    f_output_zh = open("output.zh",'w')

    # file of the output of translation from (en, fr, zh) --> ar
    f_output_en_ar = open("output.en-ar",'w')
    f_output_fr_ar = open("output.fr-ar",'w')
    f_output_zh_ar = open("output.zh-ar",'w')
    f_pivot_zh_ar_en = open("pivot.zh-ar-en",'w')

    supported models are ar <--> (zh,en,fr)
    supported_languages = {"ar" : [["zh", f_output_zh, f_output_zh_ar],
                                   ["en", f_output_en, f_output_en_ar],
                                   ["fr", f_output_fr, f_output_fr_ar]]}

    for line in f_input:
        for lang1 in supported_languages:
            for lang2, file1, file2 in supported_languages[lang1]:
                # Translate ar --> (en, fr, zh)
                text = translate_request(line, lang1, lang2)
                file1.write(text+'\n')

                # Reverse the translation (en, fr, zh) --> ar
                text = translate_request(text, lang2, lang1)
                file2.write(text+'\n')

# pivot approach
    f_output_en = open("output.en",'r')

    for line in f_output_en:
        print(line)
        text = translate_request(line, "en", "zh")
        text = translate_request(text, "zh", "en")
        final = translate_request(text, "en", "ar")
        f_pivot_zh_ar_en.write(final+'\n')

    

    print("Done translating file to all languages and back to src language")

if __name__ == "__main__":
    main()

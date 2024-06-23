from translate import Translator
import requests

def translate_text(lang_from, lang_to, text):
    try:
        translator= Translator(from_lang = lang_from, to_lang = lang_to)
        translation = translator.translate(text)
        return translation
    except:
        return "We are unable to process your request. Please try again in sometime"

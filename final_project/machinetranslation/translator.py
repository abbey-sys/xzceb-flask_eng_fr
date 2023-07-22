"""
   Below Line will import MyMemoryTranslator from deep_translator
"""
from deep_translator import MyMemoryTranslator

def englishToFrench(english_text):
    """
       This function will translate test from English to French
    """
    #write the code here
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text

def frenchToEnglish(french_text):
    """
       This function will translate test from French to English
    """
    #write the code here
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
    
"""
This module can translate text from French to English and vice versa
using IBM Watson
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)

translator = LanguageTranslatorV3(
    version="2018-05-01",
    authenticator=authenticator
)
translator.set_service_url(url)

def english_to_french(english_text):
    """
    This function takes an english words/sentences as input and returns a
    french translations
    """
    if english_text == "":
        french_text = ""
    elif english_text is None:
        french_text = None
    else:
        french_text = translator.translate(english_text,
        model_id="en-fr").get_result()['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    This function takes a French words/sentences as input and returns an
    English translations
    """
    if french_text == "":
        english_text = ""
    elif french_text is None:
        english_text = None
    else:
        english_text = translator.translate(french_text,
        model_id="fr-en").get_result()['translations'][0]['translation']
    return english_text

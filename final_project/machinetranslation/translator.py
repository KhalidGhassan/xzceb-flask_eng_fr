
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv


load_dotenv()

apikey = os.environ['IBM_API_KEY']
url = os.environ['IBM_URL']
authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def englishToFrench(englishText):
    translation = language_translator.translate(
        text=englishText,
        source='en',
        target='fr'
    ).get_result()
    frenchText = translation['translations'][0]['translation']
    return frenchText
def frenchToEnglish(frenchText):
    translation = language_translator.translate(
        text=frenchText,
        source='fr',
        target='en'
    ).get_result()
    englishText = translation['translations'][0]['translation']
    return englishText



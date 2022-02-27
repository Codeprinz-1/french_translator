import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['API_KEY']
url = os.environ['URL']
version = os.environ['VERSION']


authenticator = IAMAuthenticator(apikey=apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    frenchText = language_translator.translate(text=englishText, model_id='en-fr').get_result()['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    englishText = language_translator.translate(text=frenchText, model_id='fr-en').get_result()['translations'][0]['translation']
    return englishText
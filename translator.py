import time
from threading import Thread
from itertools import cycle
import requests
from languages import LANGUAGES, LANGUAGES_REVERSED


API_KEY = "Put your API key here"

loaded = False
def main():
    global loaded

    if not API_KEY:
        raise RuntimeError("> API_KEY not defined")

    print("=" * 56)
    print("TRANSLATOR".center(56))
    print("=" * 56)

    text = input("\n> Text to translate: ").strip()

    if not text:
        raise ValueError("> Text cannot be empty")

    print("\nAvailable Languages")
    print("-------------------")

    for index, (symbol, language) in enumerate(LANGUAGES.items(), 1):
        print(f"{index}. {symbol} - {language}")

    target_language = get_target_language()

    thread = Thread(target=loading)
    thread.start()

    translated_text = translate(text, target_language)

    loaded = True
    thread.join()

    print("=" * 56)
    print("Translation Complete")
    print("=" * 56)
    print(f"Original : {text}")
    print(f"Translated: {translated_text}")
    print("=" * 56)

def get_target_language():
    target = input("\nTarget language: ").strip()
    
    if target.upper() in LANGUAGES:
        target = target.upper()
    elif target.capitalize() in LANGUAGES_REVERSED:
        target = LANGUAGES_REVERSED[target.capitalize()]
    else:
        raise ValueError("> Target language is invalid or not supported")

    return target

def translate(text, target_language):
    response = requests.post(
        "https://api-free.deepl.com/v2/translate",
        headers={
            "Authorization": f"DeepL-Auth-Key {API_KEY}"
        },
        data={
            "text": text,
            "target_lang": target_language
        }
    )

    if response.status_code != 200:
        raise ValueError(f"> {response.text}")

    translated = response.json()["translations"][0]["text"]

    return translated

def loading():
    global loaded

    for c in cycle("|/-\\"):
        if loaded:
            return
        print(f"\r⏳ Translating... {c}", end="", flush=True)
        time.sleep(0.1)

if __name__ == "__main__":
    main()

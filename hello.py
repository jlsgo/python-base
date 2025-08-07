#! /usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente 
o programa exibe a mensagem correspondente.

Como usar:
Tenha a variavel lang devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py    
"""
# Dunder ex e boas praticas
__version__ = "0.0.1"
__author__ = "Jhon Gonçalves"
__license__ = "Unlicense"

import os 
import sys 
    
arguments = { "lang":"None","count": "1",}
for arg in sys.argv[1:]:
    # TODO: tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("--").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()
    arguments[key] = value


current_language = arguments["lang"]
if current_language  == "None":
    if "LANG" in os.environ:
        current_language = os.environ["LANG"]
    else:
        current_language = input("Choose a language: ")

current_language = current_language[:5]    

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_ES": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
    "ru_RU": "Привет, мир!",
    "de_DE": "Hallo, Welt!",
    "ja_JP": "こんにちは、世界！",
    "ko_KR": "안녕, 세상!",
    "zh_CN": "你好，世界！",
    "zh_TW": "你好，世界！",
    "ar_SA": "مرحبا بالعالم!",  
    "hi_IN": "नमस्ते, दुनिया!",
    "tr_TR": "Merhaba, Dünya!",
    "nl_NL": "Hallo, Wereld!",
    "sv_SE": "Hej, världen!",
    "da_DK": "Hej, verden!",
    "fi_FI": "Hei, maailma!",
    "pl_PL": "Witaj, świecie!",
} 



print(msg[current_language] * int(arguments["count"]))
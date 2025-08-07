#!/usr/bin/env python3
"""Hello World Multi Linguas.

Depending on the language configured in the environment, the program displays the
corresponding message.

How to use:

Set the LANG environment variable, e.g.:

    export LANG=pt_BR

Or provide it via the --lang CLI argument.

Or the user will be prompted to enter it.

Execution:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.3"
__author__ = "Jhon Gonçalves"
__license__ = "Unlicense"

import argparse
import logging
import os
import sys

# Configure logging
logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "WARNING").upper(),
    format="%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s",
)
log = logging.getLogger(__name__)


# Message translations
MESSAGES = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_ES": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

def main():
    """Main function to run the script."""
    parser = argparse.ArgumentParser(
        description="Prints 'Hello, World!' in different languages."
    )
    parser.add_argument(
        "--lang",
        metavar="LANGUAGE",
        help="The language to use (e.g., pt_BR, en_US)",
        default=None,
    )
    parser.add_argument(
        "--count",
        metavar="N",
        type=int,
        help="Number of times to print the message",
        default=1,
    )
    args = parser.parse_args()

    # Determine language with precedence: CLI > ENV > Input
    current_language = args.lang or os.getenv("LANG") or input("Choose a language: ")
    current_language = current_language.split(".")[0]

    # Safely get the message with a fallback to English
    message = MESSAGES.get(current_language, MESSAGES["en_US"])

    print(message * args.count)

if __name__ == "__main__":
    main()

from googletrans import LANGUAGES, Translator


def _normalize_lang(lang):
    """Normalize language input, including common Cyrillic homoglyphs."""
    if lang is None:
        return ""

    replacements = str.maketrans(
        {
            "\u0410": "A",
            "\u0412": "B",
            "\u0415": "E",
            "\u041a": "K",
            "\u041c": "M",
            "\u041d": "H",
            "\u041e": "O",
            "\u0420": "P",
            "\u0421": "C",
            "\u0422": "T",
            "\u0425": "X",
            "\u0430": "a",
            "\u0435": "e",
            "\u043e": "o",
            "\u0440": "p",
            "\u0441": "c",
            "\u0445": "x",
            "\u0443": "y",
        }
    )
    return str(lang).strip().translate(replacements).lower()


def _language_code(lang):
    language = _normalize_lang(lang)

    if language in LANGUAGES:
        return language

    for code, name in LANGUAGES.items():
        if language == name.lower():
            return code

    return None


def TransLate(str, lang):
    target_code = _language_code(lang)

    if not target_code:
        return f"Error: language '{lang}' was not found."

    try:
        translator = Translator()
        return translator.translate(str, dest=target_code).text
    except Exception as error:
        return f"Error: translation failed ({error})."


def LangDetect(txt):
    try:
        translator = Translator()
        return translator.detect(txt)
    except Exception as error:
        return f"Error: language detection failed ({error})."


def CodeLang(lang):
    language = _normalize_lang(lang)

    if language in LANGUAGES:
        return LANGUAGES[language].capitalize()

    code = _language_code(language)
    if code:
        return code

    return f"Error: language '{lang}' was not found."


def main():
    txt = input("Enter text to translate: ").strip()
    lang = input("Enter target language name or ISO-639 code: ").strip()

    print(txt)
    print(LangDetect(txt))
    print(TransLate(txt, lang))
    print(CodeLang(lang))


if __name__ == "__main__":
    main()

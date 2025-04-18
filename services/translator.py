from googletrans import Translator

translator = Translator()

def translate_comments_to_english(comments):
    translated = []
    for comment in comments:
        try:
            translated_comment = translator.translate(comment, dest='en').text
            translated.append(translated_comment)
        except Exception as e:
            print("Error:", e)
            translated.append(comment)  # fallback
    return translated

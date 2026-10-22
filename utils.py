def clean(text):
    return text.strip().lower()


def shout(text):
    return clean(text).upper()


def whisper(text):
    return clean(text) + '...'

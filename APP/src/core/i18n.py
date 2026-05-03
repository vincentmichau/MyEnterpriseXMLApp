
import json
from pathlib import Path

I18N_DIR = Path(__file__).parent.parent / 'i18n'

class I18N:
    def __init__(self, lang='fr'):
        self.load(lang)

    def load(self, lang):
        path = I18N_DIR / f"{lang}.json"
        self.lang = lang
        self.data = json.loads(path.read_text(encoding='utf-8')) if path.exists() else {}

    def t(self, key):
        return self.data.get(key, key)

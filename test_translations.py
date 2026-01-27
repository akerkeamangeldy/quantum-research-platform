# Quick test of translation system
import sys

# Simulate the TRANSLATIONS structure
TRANSLATIONS = {
    'en': {
        "global": {
            "title": "QUANTUM RESEARCH WORKBENCH v4.0.2",
            "language_en": "🇬🇧 EN",
            "language_ru": "🇷🇺 RU"
        },
        "home_page": {
            "hero_title": "Quantum Research Workbench"
        }
    },
    'ru': {
        "global": {
            "title": "КВАНТОВЫЙ ИССЛЕДОВАТЕЛЬСКИЙ ЦЕНТР v4.0.2",
            "language_en": "🇬🇧 EN",
            "language_ru": "🇷🇺 RU"
        },
        "home_page": {
            "hero_title": "Квантовый Исследовательский Центр"
        }
    }
}

def t(key, lang='en', fallback=None):
    """Test translation function"""
    lang_dict = TRANSLATIONS.get(lang, TRANSLATIONS.get('en', {}))
    
    if '.' in key:
        keys = key.split('.')
        value = lang_dict
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                value = None
                break
        if value:
            return value
    
    return fallback if fallback else key

# Test cases
print("Testing English:")
print(f"  global.title: {t('global.title', 'en')}")
print(f"  global.language_en: {t('global.language_en', 'en')}")
print(f"  home_page.hero_title: {t('home_page.hero_title', 'en')}")

print("\nTesting Russian:")
print(f"  global.title: {t('global.title', 'ru')}")
print(f"  global.language_ru: {t('global.language_ru', 'ru')}")
print(f"  home_page.hero_title: {t('home_page.hero_title', 'ru')}")

print("\nExpected Russian title: Квантовый Исследовательский Центр")

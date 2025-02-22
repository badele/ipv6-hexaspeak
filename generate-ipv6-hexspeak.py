#!/usr/bin/env python3

import argparse

WORD_MIN_LEN = 3
hexspeak_MAP = {
    "a": "a",
    "b": "b",
    "c": "c",
    "d": "d",
    "e": "e",
    "f": "f",
    "g": "9",
    "i": "1",
    "l": "1",
    "o": "0",
    "s": "5",
    "t": "7",
    "z": "2",
}

RATIO = {
    100: "✅",
    80: "🟦",
    60: "🟨",
    40: "🟧",
    20: "🟥",
}


# Get ratio key
# ex: 75 -> 80
def get_ratio_key(value):
    key = round(value, -1)

    while key > 0 and key not in RATIO:
        key -= 10

    if key > 0:
        return key

    return 20


# return emoji
def get_emoji(key):
    return RATIO[key]


# Convert work to hexspeak
def word_to_hexspeak(word):
    try:
        return "".join(hexspeak_MAP[char] for char in word)
    except KeyError:
        return ""


def split_to_ipv6(word):
    return ":".join(word[i : i + 4] for i in range(0, len(word), 4))


def split_to_ipv6_with_shift(word):
    return word[:2] + ":" + split_to_ipv6(word[2:])


# Output markdown result
def output_markdown(characters):
    print("# Table of contents")
    keys = sorted(characters.keys(), reverse=True)
    for key in keys:
        print(f"- [near {int(key)}% ratio ({len(characters[key])})](#{key}-characters)")

    keys = sorted(characters.keys(), reverse=True)
    for key in keys:
        for line in characters[key]:
            print(line)


# Get ratio similarity
def get_ratio_similarity(word, hexspeak):
    similarity = 0
    for idx in range(len(word)):
        if word[idx] == hexspeak[idx]:
            similarity += 1
    return similarity / len(word) * 100


def main():
    parser = argparse.ArgumentParser(description="Convertir des mots en hexspeak.")
    parser.add_argument("filename", type=str, help="Fichier contenant les mots")
    args = parser.parse_args()

    try:
        with open(args.filename) as file:
            words = file.read().splitlines()
    except FileNotFoundError:
        print(f"Erreur: fichier '{args.filename}' introuvable.")
        return

    ratios = {}
    for idx in range(len(words)):
        word = words[idx]
        hexspeak = word_to_hexspeak(word)

        word_len = len(hexspeak)

        if word_len < WORD_MIN_LEN:
            continue

        if hexspeak:
            ratio_key = get_ratio_key(get_ratio_similarity(word, hexspeak))
            emoji = get_emoji(ratio_key)

            if ratio_key not in ratios:
                ratios[ratio_key] = [
                    f"""
## near {ratio_key} ratio
| % | word | hexspeak | offset ipv6 hexspeak | ipv6 hexspeak |
| - | - | - | - | - |"""
                ]

            ratios[ratio_key].append(
                f"| {emoji} |{word}|{hexspeak.upper()}|{split_to_ipv6_with_shift(hexspeak.upper())}|{split_to_ipv6(hexspeak.upper())}|"
            )

    output_markdown(ratios)


if __name__ == "__main__":
    main()

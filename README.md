# IPv6 hexspeak

Here is a small tool that allows you to find words that can be inserted into an
IPv6 address.

Here are some examples

| %  | word   | hexspeak | offset ipv6 hexspeak | ipv6 hexspeak |
| -- | ------ | -------- | -------------------- | ------------- |
| ✅ | dead   | DEAD     | DE:AD                | DEAD          |
| 🟦 | cable  | CAB1E    | CA:B1E               | CAB1:E        |
| 🟦 | iot    | 107      | 10:7                 | 107           |
| 🟦 | acid   | AC1D     | AC:1D                | AC1D          |
| 🟦 | casa   | CA5A     | CA:5A                | CA5A          |
| 🟨 | office | 0FF1CE   | 0F:F1CE              | 0FF1:CE       |
| 🟨 | doc    | D0C      | D0:C                 | D0C           |
| 🟨 | access | ACCE55   | AC:CE55              | ACCE:55       |
| 🟧 | bloc   | B10C     | B1:0C                | B10C          |

## Languages hexspeak

| Language              | ~ #words |
| --------------------- | -------- |
| [English](english.md) | 9300     |
| [French](french.md)   | 4200     |

## Generate

[On Nixos](https://nixos.org/)

```bash
nix shell nixpkgs#wordlists
WORDLISTSPATH=$(wordlists_path)
ENGLISH="seclists/Miscellaneous/lang-english.txt"
FRENCH="seclists/Miscellaneous/lang-french-full.txt"


awk '{ print length, $0 }' "${WORDLISTSPATH}/${ENGLISH}" | sort -n -k1,1 -k2 | cut -d ' ' -f2- > wordlist.txt
python generate-ipv6-hexspeak.py wordlist.txt > english.md

awk '{ print length, $0 }' "${WORDLISTSPATH}/${FRENCH}" | sort -n -k1,1 -k2 | cut -d ' ' -f2- > wordlist.txt
python generate-ipv6-hexspeak.py wordlist.txt > french.md
```

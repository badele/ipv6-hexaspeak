# IPv6 hexspeak

Here is a small tool that allows you to find words that can be inserted into an
IPv6 address.

Here are some examples

| %  | word   | hexspeak | IPv6 example   |
| -- | ------ | -------- | -------------- |
| ✅ | dead   | DEAD     | FD00:DEAD::    |
| 🟦 | cables | CAB1E5   | FD00:CAB1:E5:: |
| 🟦 | iot    | 107      | FD00:107::     |
| 🟦 | acid   | AC1D     | FD00:AC1D::    |
| 🟦 | casa   | CA5A     | FD00:CA5A::    |
| 🟨 | office | 0FF1CE   | FD00:0FF1:CE:: |
| 🟨 | doc    | D0C      | FD00:D0C::     |
| 🟨 | access | ACCE55   | FD00:ACCE:55:: |
| 🟧 | bloc   | B10C     | FD00:B10C::    |

## Languages hexspeak

| Language              | ~ #words |
| --------------------- | -------- |
| [English](english.md) | 9300     |
| [French](french.md)   | 4200     |
| [Spanish](spanish.md) | 65       |

## Generate

[On Nixos](https://nixos.org/)

```bash
nix shell nixpkgs#wordlists
WORDLISTSPATH=$(wordlists_path)
ENGLISH="seclists/Miscellaneous/lang-english.txt"
SPANISH="seclists/Miscellaneous/lang-spanish.txt"
FRENCH="seclists/Miscellaneous/lang-french-full.txt"


awk '{ print length, $0 }' "${WORDLISTSPATH}/${ENGLISH}" | sort -n -k1,1 -k2 | cut -d ' ' -f2- > wordlist.txt
python generate-ipv6-hexspeak.py wordlist.txt > english.md

awk '{ print length, $0 }' "${WORDLISTSPATH}/${FRENCH}" | sort -n -k1,1 -k2 | cut -d ' ' -f2- > wordlist.txt
python generate-ipv6-hexspeak.py wordlist.txt > french.md

awk '{ print length, $0 }' "${WORDLISTSPATH}/${SPANISH}" | sort -n -k1,1 -k2 | cut -d ' ' -f2- > wordlist.txt
python generate-ipv6-hexspeak.py wordlist.txt > spanish.md
```

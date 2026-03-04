#!/usr/bin/env python3

import base64
import binascii
import urllib.parse
import html
import codecs
import sys

ENCODING_TYPES = {
    "1": "Base16", "2": "Base32", "3": "Base64", "4": "Base85",
    "5": "Binary", "6": "Decimal", "7": "URL", "8": "HTML",
    "9": "Hex String", "10": "ROT13"
}

def encode(type, text):
    try:
        b = text.encode("utf-8")
        match type:
            case "1": return base64.b16encode(b).decode()
            case "2": return base64.b32encode(b).decode()
            case "3": return base64.b64encode(b).decode()
            case "4": return base64.b85encode(b).decode()
            case "5": return " ".join(f"{x:08b}" for x in b)
            case "6": return " ".join(str(x) for x in b)
            case "7": return urllib.parse.quote(text)
            case "8": return html.escape(text)
            case "9": return binascii.hexlify(b).decode()
            case "10": return codecs.encode(text, "rot_13")
        return None
    except Exception as e:
        return f"[Error] {e}"

def decode(type, text):
    try:
        t = text.strip()
        match type:
            case "1": return base64.b16decode(t.upper()).decode()
            case "2": return base64.b32decode(t.upper()).decode()
            case "3": return base64.b64decode(t).decode()
            case "4": return base64.b85decode(t).decode()
            case "5": return bytes(int(x, 2) for x in t.split()).decode()
            case "6": return bytes(int(x) for x in t.split()).decode()
            case "7": return urllib.parse.unquote(text)
            case "8": return html.unescape(text)
            case "9": return binascii.unhexlify(t).decode()
            case "10": return codecs.decode(text, "rot_13")
        return None
    except Exception as e:
        return f"[Error] {e}"

def main():
    while True:
        print("\n[1] Encode  [2] Decode  [0] Keluar")
        act = input("> ").strip()

        if act == "0":
            print("Bye.")
            break
        if act not in ("1", "2"):
            print("Bye.")
            continue

        for k, v in ENCODING_TYPES.items():
            print(f"{k}. {v}")

        type = input("> ").strip()
        if type not in ENCODING_TYPES:
            print("Bye.")
            continue

        text = input("> ").strip()
        if not text:
            print("Bye.")
            continue

        print(f"\n[{ENCODING_TYPES[type]}]")

        if act == "1":
            print("Encode :", encode(type, text))
        else:
            print("Decode :", decode(type, text))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)

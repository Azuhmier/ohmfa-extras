# FNAME: playground.py
# USAGE: python -i .\scripts\playground.py
from __future__ import annotations
import inspect
import pydoc
import json
import os
from pathlib import Path
from typing import List
import codecs
import sys
import encodings
import pkgutil
import encodings.aliases

def hexdump(b: bytes, width=16):
    for i in range(0, len(b), width):
        chunk = b[i:i+width]
        hexpart = " ".join(f"{x:02x}" for x in chunk)
        asciipart = "".join(chr(x) if 32 <= x < 127 else "." for x in chunk)
        print(f"{i:08x}  {hexpart:<{width*3}}  {asciipart}")

from difflib import SequenceMatcher
from typing import Callable, List, Optional
from unicodedata import combining, normalize
import re


def find_index(strlist: List[str], value: str, ratio: float = 0.75) -> int:
    for index in range(0, len(strlist)):
        if match(a=strlist[index], b=value, ratio=ratio):
            return index

    return -1


def find_regexpr_index(strlist: List[str], regexpr: str, preprocessfn: Optional[Callable] = None) -> int:
    if not preprocessfn:
        preprocessfn = lambda x: x

    for index in range(0, len(strlist)):
        if re.search(re.compile(regexpr), preprocessfn(strlist[index])):
            return index

    return -1


def match(a: str, b: str, ratio: float = 0.75) -> bool:
    return SequenceMatcher(a=a, b=b).ratio() >= ratio


def remove_accents(string: str) -> str:
    return "".join([c for c in normalize("NFKD", string) if not combining(c)])

# sus2ymst

[![PyPI - Version](https://img.shields.io/pypi/v/sus2ymst.svg)](https://pypi.org/project/sus2ymst/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sus2ymst)

Convert Ched SUS to YMST(world dai star) txt chart format.

## Installation
```bash
pip install sus2ymst
```

## Usage
```python
import sus2ymst

with open("test.sus", "r") as f:
    sus_text = f.read()
    notation_text, error = sus2ymst.loads(sus_text)
    print(notation_text)
    print(error)
```


## Chart specifications
Charts are written in sus format.
Editor is assumed to be Ched.

| YMST                             | Ched                                          |
| ------------------------------------ | --------------------------------------------- |
| Tap Notes | Tap Notes |
| Critical Notes | Critical Notes |
| Flick Notes | Flick + Swing up Air |
| Hold Notes (Blue) | Slide Notes |
| Scratch hold notes (Purple) | Swing up Air at the end of the slide |
| Critical hold notes | Critical notes at the start of the slide |
| Critical Scratch Hold Notes | Critical Notes at Start of Slide |
| Scratch Notes (the one above the hold) | Flick + Swing Air in the middle of the slide |
| Relay point for hold and scratch hold | Relay point for slide |
| Jump Scratch | Flick to overlap the start and end points of the scratch hold you want to connect |
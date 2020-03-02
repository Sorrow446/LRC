# LRC
Rough LRC lyrics parser written in Python.

## Usage
Parse local lrc:
```python
import lrc

parsed = lrc.parse(r"G:\1.lrc")
```
Parse LRC written in FLAC file:
```python
import lrc

parsed = lrc.parse(r"G:\1.flac")
```

## Exceptions
#### NoLyricsError
No lyrics could be found in the source.
#### ParseError
Your LRC file isn't valid.

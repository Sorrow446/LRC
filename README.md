# LRC
Rough LRC lyrics parser written in Python.

## Usage
Parse local LRC:
```python
import lrc

parsed = lrc.parse(r"G:\1.lrc")
```
Parse LRC written in FLAC file:
```python
import lrc

parsed = lrc.parse(r"G:\1.flac")
```
Get all text:
```python
text = [line['text'] for line in parsed]
```
Get line total:
```python
total = len(parsed)
```

## Output
LRCs will be parsed in a lists of dicts
```
[{'min': '00', 'sec': '00', 'hun': '00', 'text': 'x'}, {'min': '00', 'sec': '23', 'hun': '29', 'text': "y"}, {'min': '00', 'sec': '23', 'hun': '90', 'text': "z"}]
```
min: minutes,
sec: seconds,
hun: second hundredths

## Exceptions
|Exception|Info|
| --- | --- |
|NoLyricsError|No lyrics could be found in the source.
|ParseError|LRC file is not valid.

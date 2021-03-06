# LRC
Rough timed LRC lyrics parser written in Python.

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

## Params
|Param|Info|Default
| --- | --- | --- |
|-|Local LRC or FLAC file path.|-|
|frame|Which frame to read lyrics from in FLAC files.|lyrics

## Output
LRCs are parsed into a list of dicts.
```
[{'min': '00', 'sec': '00', 'hun': '00', 'text': 'x'}, {'min': '00', 'sec': '23', 'hun': '29', 'text': "y"}, {'min': '00', 'sec': '23', 'hun': '90', 'text': "z"}]
```
|Key|Info|
| --- | --- |
|min|Minutes
|sec|Seconds
|hun|Second hundredths
|text|Lyrics

## Exceptions
|Exception|Info|
| --- | --- |
|NoLyricsError|No lyrics could be found in the source.
|ParseError|Lyrics are not valid.

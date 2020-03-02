# First.
import re

# Third.
from mutagen.flac import FLAC


REGEX = "^\[(\d{2})\:(\d{2})\.(\d{2})\](.+)"

class NoLyricsError(Exception):
	pass

class ParseError(Exception):
	pass

def from_lrc_file(lrc):
	with open(lrc, encoding="UTF-8") as f:
		return f.readlines()

# Tested with mp3tag only.		
def from_flac(f, frame):
	audio = FLAC(f)
	lyrics = audio.get(frame)
	if not lyrics:
		raise NoLyricsError("Frame \"{}\" does not contain any lyrics.".format(frame))
	lyrics = [x.split("\r\n") for x in lyrics]
	return lyrics[0]

def parse(src, frame="lyrics"):
	num = 0
	parsed = []
	if src.endswith(".flac"):
		lyrics = from_flac(src, frame=frame)
	else:
		lyrics = from_lrc_file(src)
	for line in lyrics:
		if line.strip():
			num += 1
			m = re.match(REGEX, line)
			try:
				parsed.append({
					"min": m.group(1),
					"sec": m.group(2),
					"hun": m.group(3),
					"text": m.group(4).strip()
				})
			except AttributeError:
				raise ParseError("Failed to parse line #{}. Line is invalid.".format(num))
	if not parsed:
		raise NoLyricsError("Source does not contain any lyrics.")
	return parsed

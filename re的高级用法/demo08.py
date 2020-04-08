import re

it = re.finditer(r"\d+", "12a32bc43jf3")
for match in it:
    print(match.group())
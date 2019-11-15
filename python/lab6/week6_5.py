import re

sample_text="""
Mouse,Michael,Mr,10-01-2001
Duckington,Donald,Mr,23-02-2004
Mouse,Maisie,Mrs,12-03-2005
"""

# Use parantheses to capture sections
pattern = r'^(\w+),(\w+),(\w+),([0-9-]+)$'


# The splitlines method returns a list of lines
for line in sample_text.splitlines():
    match = re.match(pattern, line)
    if match:
        print("{} {} {} found".format(
            match.group(3), match.group(1),
            match.group(2)))

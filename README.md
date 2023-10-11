# WHY

Obsidian now doesn't support tiff now, nor in the future.

If you have tiff image in notes, it will not be displayed.

# HOW TO USE

1. convert all tiff to png
`for i in $(find . -name "*.tiff"); python tiff_conventer.py $i $i.png`

2. update notes' image link
`for i in $(find . -name "*.md"); python note_converter.py $i`


# NOTE!

Script notes_converter.py will override our notes, use with caution!

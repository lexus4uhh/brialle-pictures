from PIL import Image

def braille_to_unicode(dots):
    braille_byte = 0
    for dot in dots:
        if 1 <= dot <= 8:
            braille_byte |= (1 << (dot - 1))

    return chr(0x2800 + braille_byte)

def print_symbols(symbols, output_file=None, row_delimiter='\n'):
    output = []
    for row in symbols:
        output.append(''.join(row) + row_delimiter)
    result = ''.join(output)
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result)
    print(result)

def get_symbols(path):
    img = Image.open(path)
    img = img.convert("1")
    width, height = img.size
    new_width = width - (width % 2)
    new_height = height - (height % 4)
    img = img.crop((0, 0, new_width, new_height))
    data = img.load()

    symbols = []
    for y in range(0, new_height, 4):
        row = []
        for x in range(0, new_width, 2):
            s = []
            if not data[x, y]:
                s.append(1)
            if not data[x, y+1]:
                s.append(2)
            if not data[x, y+2]:
                s.append(3)
            if not data[x+1, y]:
                s.append(4)
            if not data[x+1, y+1]:
                s.append(5)
            if not data[x+1, y+2]:
                s.append(6)
            if not data[x, y+3]:
                s.append(7)
            if not data[x+1, y+3]:
                s.append(8)
            row.append(braille_to_unicode(s))
        symbols.append(row)
    return symbols

while True:
    try:
        a = get_symbols(input('type in path to image (.png), Ctrl+C to exit\n\n'))
        print_symbols(a, input("output path (can be None): "))
    except Exception as e:
        print(f'retry, error: {e}')
    
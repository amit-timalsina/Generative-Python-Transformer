import os
from curtsies.fmtfuncs import cyan, bold, green, red, yellow

MAX_CHAR_LENGTH = 512
MIN_CHAR_LENGTH = 20

NEWLINECHAR = '<N>'

d = 'repos'
paths = []
for dirpath, dirnames, filenames in os.walk(d):
    for f in filenames:
        path = os.path.join(dirpath, f)
        paths.append(path)
print(len(paths))
with open('python_text_data_file', 'a') as f:
    for path in paths:
        try:
            d = open(path, 'r').read()
            fd = d.replace("\n", NEWLINECHAR)

            if 100 < len(fd) <= MAX_CHAR_LENGTH:
                f.write(fd+'\n')

            else:
                sd = fd.split(f'{NEWLINECHAR}{NEWLINECHAR}')
                substring = ''
                for split in sd:
                    substring += split + f'{NEWLINECHAR}{NEWLINECHAR}'
                    if MIN_CHAR_LENGTH <= len(substring) <= MAX_CHAR_LENGTH:
                        f.write(substring + '\n')
                        substring = ''
                    else:
                        print('Substring not found')
                        print('\nClearing substring')
                        substring = ''
        except Exception as e:
            print(str(e))
        
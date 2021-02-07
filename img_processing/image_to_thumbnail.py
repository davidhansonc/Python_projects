import os, sys
from PIL import Image

new_size = (300, 300)

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + "_thumb" + \
            os.path.splitext(infile)[1]
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.thumbnail(new_size)
                im.save(outfile, "JPEG")
                print(im.size)
        except OSError:
            print("cannot create thumbnail for", infile)
# Example to demonstrate simple image file manipulation
# using the PIL module
#
# See http://effbot.org/imagingbook/introduction.htm
#  for the documentation and tutorial for this module
#
# J. Weible

from PIL import Image

def main():
    #image_filename = input('Enter the image filename to use:')
    image_filename = 'mountain-meadow.jpg'

    im = Image.open(image_filename)
    im.show('Original full-size')

    xsize, ysize = im.size
    print('The image file  are:', xsize, 'by', ysize, 'pixels.')

    # shrink it down to 1/64th the size
    small = im.resize((xsize // 8, ysize // 8), Image.BILINEAR)
    small.show('Small version')
    xsize, ysize = small.size
    print('The small image file dimensions are:', xsize, 'by', ysize, 'pixels.')

    t = one_tile(small)
    t.show('One seamless repeatable tile')
    xsize, ysize = t.size
    print('The tile image file dimensions are:', xsize, 'by', ysize, 'pixels.')

    tiling = repeat_tiles(t, 3, 3)
    tiling.show('Completed tiling')
    return

def one_tile(image: Image.Image) -> Image.Image:
    """Create a new seamless image "tile", from flipping the original horizontally
    and vertically, and joining the 4 together into one new image."""
    width, height = image.size

    new = Image.new("RGB", (width * 2, height * 2))
    # paste a copy of provided image into upper-left quadrant:
    new.paste(image, (0, 0, width, height))

    # now flip the image horizontally and paste into upper-right quadrant:
    flip = image.transpose(Image.FLIP_LEFT_RIGHT)
    new.paste(flip, (width, 0, width*2, height))

    # now flip the image vertically and paste into lower-right quadrant:
    flip = flip.transpose(Image.FLIP_TOP_BOTTOM)
    new.paste(flip, (width, height, width*2, height*2))

    # now flip the image horizontally and paste into lower-left quadrant:
    flip = flip.transpose(Image.FLIP_LEFT_RIGHT)
    new.paste(flip, (0, height, width, height*2))

    return new

def repeat_tiles(image: Image.Image, w, h) -> Image.Image:
    """Given a single image, repeat it in a grid w*h times."""
    width, height = image.size
    new = Image.new("RGB", (width * w, height * h))
    for x in range(w):
        for y in range(h):
            start_x = width * x
            start_y = height * y
            new.paste(image, (start_x, start_y, start_x + width, start_y + height))
    return new

if __name__ == '__main__':
    main()

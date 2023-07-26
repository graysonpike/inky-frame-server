import cairocffi as cairo
from io import BytesIO
from PIL import Image


def print_cairo_version():
    print(f"The cairo version is {cairo.cairo_version_string()}.")


def get_blank_surface_bytes():
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 500, 500)
    ctx = cairo.Context(surface)

    # Set the colour (white)
    ctx.set_source_rgb(1, 1, 1)

    # Draw a rectangle the size of the surface
    ctx.rectangle(0, 0, 500, 500)

    # Fill the rectangle
    ctx.fill()

    # Set the colour (black) for the text
    ctx.set_source_rgb(0, 0, 0)

    # Set the font and size
    ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(25)

    # Draw the text
    ctx.move_to(100, 100)  # move to position
    ctx.show_text("Hello, World!")
    surface.write_to_png("hello_world.png")
    image = Image.frombuffer('RGBA', (500, 500), surface.get_data(), 'raw', 'BGRA', 0, 1)
    image = image.convert('RGB')
    bytes = BytesIO()
    image.save(bytes, format='JPEG')
    bytes.seek(0)
    return bytes


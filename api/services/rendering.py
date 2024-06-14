import cairocffi as cairo
from io import BytesIO
from PIL import Image

WIDTH = 800
HEIGHT = 480


def get_hello_world_jpg() -> BytesIO:
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)

    # Set the colour (white)
    ctx.set_source_rgb(1, 1, 1)

    # Draw a rectangle the size of the surface
    ctx.rectangle(0, 0, WIDTH, HEIGHT)

    # Fill the rectangle
    ctx.fill()

    # Set the colour (black) for the text
    ctx.set_source_rgb(0, 0, 0)

    # Set the font and size
    ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(65)

    # Draw the text
    extents = ctx.text_extents("Hello, World!")
    print("Extents:")
    print(extents)
    ctx.move_to((WIDTH/2) - (extents[2]/2), (HEIGHT/2) + (extents[3]/2))
    ctx.show_text("Hello, World!")
    surface.write_to_png("hello_world.png")
    image = Image.frombuffer('RGBA', (WIDTH, HEIGHT), surface.get_data(), 'raw', 'BGRA', 0, 1)
    image = image.convert('RGB')
    byte_stream = BytesIO()
    image.save(byte_stream, format='JPEG')
    byte_stream.seek(0)
    return byte_stream

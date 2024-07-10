"""SSD1309 demo (flip)."""
from time import sleep
from machine import Pin, SPI  # type: ignore
from xglcd_font import XglcdFont
from ssd1309 import Display


def test():
    """Test code."""
    spi = SPI(1, baudrate=10000000, sck=Pin(14), mosi=Pin(13))
    # Initialize display flipped 180 degrees
    display = Display(spi, dc=Pin(4), cs=Pin(5), rst=Pin(2), flip=True)

    print("Loading font.  Please wait.")
    bitstream = XglcdFont('fonts/Bitstream_Vera35x32.c', 35, 32)

    display.draw_bitmap("images/no_wifi32x32.mono", 0, 0, 32, 32, invert=True)
    display.draw_text(45, 0, "WiFi", bitstream)
    display.present()
    sleep(3)

    display.flip(False)  # No flip which is the default
    display.present()
    sleep(3)

    display.flip()  # Flip 180 degrees
    display.present()

    sleep(10)
    display.flip(False)
    display.cleanup()
    print('Done.')


test()

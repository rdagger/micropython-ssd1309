"""SSD1309 demo (images)."""
from time import sleep
from machine import Pin, SPI
from ssd1309 import Display


def test():
    """Test code."""
    spi = SPI(1, baudrate=10000000, sck=Pin(14), mosi=Pin(13))
    display = Display(spi, dc=Pin(4), cs=Pin(5), rst=Pin(2))

    display.draw_bitmap("images/eyes_128x42.mono", 0, display.height // 2 - 21, 128, 42)
    display.present()
    sleep(5)

    display.clear_buffers()
    display.draw_bitmap("images/doggy_jet128x64.mono", 0, 0, 128, 64, invert=True)
    display.present()
    sleep(5)

    display.clear_buffers()
    display.draw_bitmap("images/invaders_48x36.mono", 0, 14, 48, 36, rotate=90)
    display.draw_bitmap("images/invaders_48x36.mono", 40, 14, 48, 36)
    display.draw_bitmap("images/invaders_48x36.mono", 92, 14, 48, 36, rotate=270)
    display.present()

    sleep(10)
    display.cleanup()
    print('Done.')


test()

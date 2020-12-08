"""SSD1309 demo (shapes)."""
from time import sleep
from machine import Pin, SPI
from ssd1309 import Display


def test():
    """Test code."""
    spi = SPI(1, baudrate=10000000, sck=Pin(14), mosi=Pin(13))
    display = Display(spi, dc=Pin(4), cs=Pin(5), rst=Pin(2))

    display.draw_rectangle(1, 1, 30, 30)
    display.fill_rectangle(6, 6, 20,20)

    display.fill_circle(50, 16, 14)
    display.draw_circle(50, 16, 10, invert=True)

    coords = [[106, 0], [106, 60], [70, 11], [127, 30], [70, 49], [106, 0]]
    display.draw_lines(coords)

    display.fill_ellipse(16, 48, 15, 8)
    display.draw_ellipse(16, 48, 8, 15)

    display.fill_polygon(5, 50, 48, 8)
    display.draw_polygon(7, 50, 48, 15)

    display.draw_line(117, 63, 127, 53)
    display.draw_vline(127, 53, 10)
    display.draw_hline(117, 63, 10)

    display.present()

    sleep(10)
    display.cleanup()
    print('Done.')


test()

"""SSD1309 demo (scroll)."""
from time import sleep
from machine import Pin, SPI  # type: ignore
from ssd1309 import Display
from xglcd_font import XglcdFont


def test():
    """Test code."""
    bally = XglcdFont('fonts/Bally7x9.c', 7, 9)

    spi = SPI(2, baudrate=10000000, sck=Pin(12), mosi=Pin(11))  # Lolin S3 SPI 2
    display = Display(spi, dc=Pin(16), cs=Pin(10), rst=Pin(18))
    # spi = SPI(1, baudrate=10000000, sck=Pin(14), mosi=Pin(13))  # ESP32 SPI 1
    # display = Display(spi, dc=Pin(4), cs=Pin(5), rst=Pin(2))
    # i2c = I2C(0, freq=400000, scl=Pin(5), sda=Pin(4))  # Pico I2C bus 1
    # display = Display(i2c=i2c, rst=Pin(2))

    display.clear()
    display.draw_rectangle(0, 0, 128, 64)
    display.fill_circle(63, 31, 10)
    coords = [[0, 0], [63, 31], [127, 0]]
    display.draw_lines(coords)

    display.draw_text(7, 47, "Horizontal Scroll", bally)
    display.present()
    display.scroll_horizontal_setup()
    display.scroll_start()
    sleep(8)

    display.draw_text(7, 47, " Vertical Scroll  ", bally)
    display.present()
    display.scroll_setup(direction=['up'])
    display.scroll_start()
    sleep(4.2)

    display.draw_text(7, 47, " Diagonal Scroll  ", bally)
    display.present()
    display.scroll_setup(direction=['left', 'down'], vertical_speed=2)
    display.scroll_start()
    sleep(8.4)

    display.draw_text(7, 47, "   Split Scroll  ", bally)
    display.present()
    display.scroll_horizontal_setup(direction='left', end_page=43, interval=7)
    display.scroll_start()
    sleep(5.5)

    display.draw_text(7, 47, "   Split Scroll  ", bally)
    display.present()
    display.scroll_setup(direction=['up'], total_rows=44, interval=1)
    display.scroll_start()
    sleep(14.5)

    display.cleanup()
    print('Done.')


test()

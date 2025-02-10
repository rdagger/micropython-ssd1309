"""SSD1309 demo (scroll manual)."""
from random import choice
from time import sleep
from machine import Pin, SPI  # type: ignore
from ssd1309 import Display


def test():
    """Test code."""
    spi = SPI(2, baudrate=10000000, sck=Pin(12), mosi=Pin(11))  # Lolin S3 SPI2
    display = Display(spi, dc=Pin(16), cs=Pin(10), rst=Pin(18))
    # spi = SPI(1, baudrate=10000000, sck=Pin(14), mosi=Pin(13))  # ESP32 SPI1
    # display = Display(spi, dc=Pin(4), cs=Pin(5), rst=Pin(2))
    # i2c = I2C(0, freq=400000, scl=Pin(5), sda=Pin(4))  # Pico I2C bus1
    # display = Display(i2c=i2c, rst=Pin(2))

    # Invader demo
    display.clear()
    display.draw_bitmap("images/invaders_48x36.mono", 0, 14, 48, 36)
    display.present()

    for _ in range(2):
        for _ in range(80):
            display.scroll_horizontal_manual()
            sleep(.03)  # Minimum time delay is 2/Frame Frequency
        for _ in range(80):
            display.scroll_horizontal_manual(direction='left')
            sleep(.03)  # Minimum time delay is 2/Frame Frequency
    display.scroll_stop()

    # Saucer demo
    display.clear()
    display.draw_bitmap("images/saucer_48x26.mono", 14, 0, 48, 26, invert=True)
    y = 16  # Starting terrain height
    for x in range(display.width):  # Draw initial terrain loop
        y = y + choice([-1, 1])  # Shift Y up or down randomly
        y = max(0, min(y, display.height // 2 - 1))  # Ensure Y in range
        display.draw_pixel(x, y+32)  # Draw current terrain pixel
    display.present()

    for _ in range(512):
        # Clear left most column
        display.write_cmd(display.COLUMN_ADDRESS)  # Set columns to write
        display.write_cmd(0)  # Minimum column
        display.write_cmd(0)  # Maximum column
        display.write_cmd(display.PAGE_ADDRESS)  # Set pages to write
        display.write_cmd(0)  # Minimum page
        display.write_cmd(7)  # Maximum page
        display.write_data(bytearray(8))

        # Scroll lower 4 pages of screen horizontally left 1 column
        display.scroll_horizontal_manual(direction="left", start_page=4)

        # Draw next terrain pixel
        display.write_cmd(display.COLUMN_ADDRESS)  # Set columns to write
        display.write_cmd(127)  # Minimum column
        display.write_cmd(127)  # Maximum column
        display.write_cmd(display.PAGE_ADDRESS)  # Set pages to write
        display.write_cmd(4)  # Minimum page
        display.write_cmd(7)  # Maximum page
        y = y + choice([-1, 1])  # Shift Y up or down randomly
        y = max(0, min(y, display.height // 2 - 2))  # Ensure Y in range
        page = y // 8  # Determine page
        bit_index = y % 8  # Determine which bit in that page byte to set
        data = bytearray(4)  # Initialize array of 8 bytes
        data[page] = 1 << bit_index  # Set the pixel to display
        display.write_data(data)  # Write pixel
        sleep(.04)  # Minimum time delay is 2/Frame Frequency
    display.cleanup()
    print('Done.')


test()

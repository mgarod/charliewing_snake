# Compilation and Installation

Use the pip package `mpy-cross`

`python -m mpy_cross snake.py`
`python -m mpy_cross text_display.py`

Obtain `font8x5.bin` and place it alongside your `code.py`: https://github.com/adafruit/Adafruit_CircuitPython_framebuf/tree/master/examples

# Usage

```python
import board
import busio
import adafruit_is31fl3731
 
import snake
import text_display

i2c = busio.I2C(board.SCL, board.SDA)
display = adafruit_is31fl3731.CharlieWing(i2c)

if __name__ == '__main__':
    while 1:
        snake.play_game(display)
        text_display.show_text("Mike", display)
```

# Features
- Game speed progresses as snake grows (1.2 sec per move initially)
- Two types of snake AI (Euclidean vs Manhattan distances)
- Snake flashes on death, and clears the board.

# TODO
- Can give the snake more look-ahead (e.g. prune moves which have 0 subsequent moves)

# Acknowledgements
- Text scrolling code is largely taken from https://learn.adafruit.com/adafruit-15x7-7x15-charlieplex-led-matrix-charliewing-featherwing/python-circuitpython#text-scrolling-example-6-44

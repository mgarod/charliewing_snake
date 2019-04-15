# Compile

Use the pip package `mpy-cross`

`python -m mpy_cross snake.py -o snake.mpy`

# Usage

```python
import board
import busio
import adafruit_is31fl3731
 
import snake

i2c = busio.I2C(board.SCL, board.SDA)
display = adafruit_is31fl3731.CharlieWing(i2c)

if __name__ == '__main__':
    while 1:
        snake.play_game(display)     
```

# Features
- Game speed progresses as snake grows (1.2 sec per move initially)
- Two types of snake AI (Euclidean vs Manhattan distances)
- Snake flashes on death, and clears the board.
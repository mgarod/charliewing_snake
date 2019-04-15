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
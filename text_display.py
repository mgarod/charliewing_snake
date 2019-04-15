from time import sleep

import adafruit_framebuf


def show_text(text, display):
    # Create a framebuffer for our display
    buf = bytearray(32)  # 2 bytes tall x 16 wide = 32 bytes (9 bits is 2 bytes)
    fb = adafruit_framebuf.FrameBuffer(buf,
        display.width, display.height, adafruit_framebuf.MVLSB)

    frame = 0 # start with frame 0
    for i in range(len(text) * 12):
        fb.fill(0)
        fb.text(text, -i + display.width, 0, color=1)

        # to improve the display flicker we can use two frames
        # fill the next frame with scrolling text, then
        # show it.
        display.frame(frame, show=False)
        # turn all LEDs off
        display.fill(0)
        for x in range(display.width):
            # using the FrameBuffer text result
            bite = buf[x]
            for y in range(display.height):
                bit = 1 << y & bite
                # if bit > 0 then set the pixel brightness
                if bit:
                    display.pixel(x, y, 50)

        # now that the frame is filled, show it.
        display.frame(frame, show=True)
        frame = 0 if frame else 1
    display.fill(0)
    sleep(1)


if __name__ == '__main__':
    while 1:
        show_text("Mike", display)

import pyautogui, sys, time
from PIL import ImageGrab
print('Press Ctrl-C to quit.')
if __name__ == "__main__":
    while True:
        # Get the current mouse position
        x, y = pyautogui.position()

        # Capture the screen and get the color at the current mouse position
        screen = ImageGrab.grab()
        color = screen.getpixel((x, y))

        # Prepare the string to display the position and color
        positionStr = f'X: {str(x).rjust(4)} Y: {str(y).rjust(4)} RGB: ({color[0]}, {color[1]}, {color[2]})'

        # Print the string, overwriting the last printed line
        print(positionStr)
        time.sleep(1)

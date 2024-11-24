import time
import pyautogui
from PIL import ImageGrab


def click_positions():
    # Replace these coordinates with the positions where you want to click
    positions = [(2692, 2338), (2321, 1624), (2482, 2218), (2820, 165)]
    #second one is to change
    pyautogui.moveTo(positions[0][0], positions[0][1])  # Move the mouse to the specified position
    pyautogui.click()
    time.sleep(10)
    color = (0, 0, 0)
    found_color = False
    for j in range(60):
        for i in range(1, 4):
            pyautogui.moveTo(positions[i][0], positions[i][1])  # Move the mouse to the specified position
            if i == 2:
                color = ImageGrab.grab().getpixel((positions[i][0], positions[i][1]))
            pyautogui.click()  # Simulate a mouse click
            if color == (255, 69, 68):
                found_color = True  # Set flag to true
                print("Color detected! Breaking the loops.")
                break
            time.sleep(1)  # Add a small delay between clicks if needed
        if found_color:
            break
def wait_until_time(target_time):
    TIME_FRAME = 3600
    while True:
        current_time = time.strftime("%H:%M")
        print(current_time)

        # Calculate the time difference in minutes
        time_diff = (int(target_time.split(":")[0]) * 60 + int(target_time.split(":")[1])) - \
                    (int(current_time.split(":")[0]) * 60 + int(current_time.split(":")[1]))

        # Adjust the sleep interval based on the time difference
        if 30 < time_diff <= 90:
            TIME_FRAME = 300  # Check every 30 seconds if 5 to 10 minutes away
        elif 5 < time_diff <= 30:
            TIME_FRAME = 60  # Check every 10 seconds if 1 to 5 minutes away
        elif 0 <= time_diff <= 5:
            TIME_FRAME = 20  # Check every 10 seconds if 1 to 5 minutes away

        if current_time == target_time:
            click_positions()
            print(f"Mouse clicks performed at {target_time}")
            break

        time.sleep(TIME_FRAME)  # Wait for the next check

# Call the function

if __name__ == "__main__":
    wait_until_time("09:59")

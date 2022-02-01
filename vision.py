import numpy as np
import cv2
import mss.tools
import pyautogui


with mss.mss() as sct:
    monitor_number = 2
    mon = sct.monitors[monitor_number]

    line_middle = {
        "top": mon["top"] + 70,  # 100px from the top
        "left": mon["left"] + 498+107,  # 100px from the left
        "width": 108,
        "height": 108,
        "mon": monitor_number,
    }

    line_right = {
        "top": mon["top"] + 70,  # 100px from the top
        "left": mon["left"] + 498+214,  # 100px from the left
        "width": 108,
        "height": 108,
        "mon": monitor_number,
    }

    position = 2
    while True:
        while position == 2:
            middle = sct.grab(line_middle)
            middle = cv2.cvtColor(np.array(middle), cv2.COLOR_BGR2GRAY)
            middle = cv2.Canny(np.array(middle), 70, 70)
            if np.count_nonzero(np.array(middle)) > 1210 and position == 2:
                position = 3
                pyautogui.press('right')

        while position == 3:
            right = sct.grab(line_right)
            right = cv2.cvtColor(np.array(right), cv2.COLOR_BGR2GRAY)
            right = cv2.Canny(np.array(right), 70, 70)
            if np.count_nonzero(np.array(right)) > 1210 and position == 3:
                position = 2
                pyautogui.press('left')

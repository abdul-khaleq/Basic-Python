import pyautogui
n = int(input())
print(n)#
for i in range(1, n+1):
    for j in range(0, i):
        pyautogui.write('#', interval=0.25)
    pyautogui.press('enter')
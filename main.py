import pyautogui
from time import sleep
from mouseinfo import mouseInfo
#mouseInfo()

pyautogui.click(182,878,duration=1)
sleep(1)
pyautogui.write('chrome')
sleep(1)
pyautogui.press('enter')
sleep(3)
pyautogui.hotkey('win', 'up')
pyautogui.write('https://zoom.us/signin#/login')
pyautogui.press('enter')
sleep(1)
pyautogui.click(954,313,duration=1)
sleep(1)
pyautogui.write('tomas@sdr.senado.leg.br')
sleep(1)
pyautogui.click(967,384,duration=1)
sleep(1)
pyautogui.write('91033958@Toa')
pyautogui.click(1041,493)
sleep(3)
pyautogui.click(77,352)

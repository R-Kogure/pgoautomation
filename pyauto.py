import tkinter as tk
import pyautogui
from pyautogui import moveTo, moveRel, click, doubleClick, dragTo, dragRel, position, PAUSE
from time import sleep

pyautogui.FAILSAFE = True

sleep(6)#6秒の待機時間のうちに画面を表示させておく


#------ 座標の定義 ------
start_x = 200
end_x = 1700
start_y = 138
end_y = 748
setloc_x = 520
setloc_y = 1045


#------ 移動の待機時間の定義 ------
move_duration = 1.5
drag_duration = 2.5


#------ 移動の繰り返しの回数 ------
num_movex = 5
num_movey = 4
maxrep = 2*(num_movex + num_movey)


#----------------------- 移動量の定義 -----------------------
interval_x = (end_x - start_x)//25
interval_y = (end_y - start_y)//7


num = 0
while True:
    if num < num_movex:#右移動
        num += 1
        for i in range(25):
            moveTo(start_x + interval_x*i, end_y, duration = move_duration)
            doubleClick()
            moveTo(setloc_x, setloc_y, duration = move_duration)
            click()
        moveTo(end_x, end_y, duration = move_duration)
        dragRel(-interval_x*25, 0, duration = drag_duration)


    elif num < num_movex + num_movey: #上移動
        num += 1
        #↑
        for i in range(7):
            moveTo(start_x+40, end_y - interval_y*i, duration = move_duration)
            doubleClick()
            moveTo(setloc_x, setloc_y, duration = move_duration)
            click()
        moveTo(start_x+100, start_y, duration = move_duration)
        dragRel(0, interval_y*7, duration =drag_duration)
        if num == maxrep//2:
            dragRel(interval_x*25, 0, duration = drag_duration)

    elif num < 2*num_movex + num_movey:#左移動
        num += 1
        for i in range(25):
            moveTo(end_x - interval_x*i, end_y, duration = move_duration)
            doubleClick()
            moveTo(setloc_x, setloc_y, duration = move_duration)
            click()
        moveTo(start_x, end_y, duration = move_duration)
        if num < 2*num_movex + num_movey:
            dragRel(interval_x*25, 0, duration = drag_duration)
        if num == 2*num_movex + num_movey:
            dragRel(0, -interval_y*7, duration =drag_duration)
    
    else: #下移動
        num += 1
        for i in range(7):
            moveTo(start_x+40, start_y + interval_y*i, duration =move_duration)
            doubleClick()
            moveTo(setloc_x, setloc_y, duration = move_duration)
            click()
        moveTo(start_x, end_y, duration = move_duration)
        if num < maxrep:
            dragRel(0, -interval_y*7, duration =drag_duration)
       
        if num == maxrep:
            num = 0

import re

import pyautogui

import __img__


def print_white(s):
    print('\033[1;30m' + s + '\033[0m')


def print_red(s):
    print('\033[1;31m' + s + '\033[0m')


def print_lavender(s):
    print('\033[1;35m' + s + '\033[0m')


def keyboard_event(action_value, param_value):
    # 热键,输入
    if action_value == '热键':
        args = param_value.split(',')
        pyautogui.hotkey(*args)
        return
    print_red("事件无效：" + action_value)


mouse_coordinate_stack = []


def get_coordinate(location_value):
    if location_value is None:
        return None
    # 判断是否是是直接坐标
    match = re.match(r"\(-?\d+/-?\d+\)", location_value)
    if match is not None:
        coordinate = location_value.replace('(', '').replace(')', '').split('/')
        x = int(coordinate[0])
        y = int(coordinate[1])
        return pyautogui.Point(x, y)
    else:
        # 判断是否是是通过图像匹配坐标
        coordinate = __img__.get_coordinate(location_value)
        if coordinate is not None:
            return coordinate
    return None


# 移动至,继续移动,单击,双击,右击,滑鼠点击,滑鼠上滑,滑鼠下滑
def mouse_event(location_index, location_value, action_value, param_value):
    # 不需要坐标的
    # if action_value == '滑鼠点击':
    if action_value == '滑鼠上滑':
        pyautogui.scroll(int(param_value))
        return
    if action_value == '滑鼠下滑':
        pyautogui.scroll(-(int(param_value)))
        return
    if action_value == '复位':
        coordinate = mouse_coordinate_stack.pop()
        mouse_event_(coordinate, pyautogui.moveTo)
        return

    # 需要坐标的
    coordinate = get_coordinate(location_value)
    if coordinate is None:
        print_red('这个单元格有点问题呢：' + location_index)
        return

    if action_value == '移动至':
        mouse_event_(coordinate, pyautogui.moveTo)
        return
    if action_value == '继续移动':
        pyautogui.move(coordinate.x, coordinate.y)
        return
    if action_value == '单击':
        mouse_event_(coordinate, pyautogui.leftClick)
        return
    if action_value == '双击':
        mouse_event_(coordinate, pyautogui.doubleClick)
        return
    if action_value == '右击':
        mouse_event_(coordinate, pyautogui.rightClick)
        return

    print_red("事件无效：" + action_value)


def mouse_event_(coordinate, func):
    if coordinate.x == 0 and coordinate.y == 0:
        func()
    else:
        mouse_coordinate_stack.append(coordinate)
        func(coordinate.x, coordinate.y)
    return

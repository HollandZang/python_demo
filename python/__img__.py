import pyautogui


def get_coordinate(img):
    # 先只判断相对目录
    location = pyautogui.locateOnScreen(r'..\imgs\\' + img)
    if location is None:
        print('匹配不到资源图片：' + img)
        return None
    else:
        coordinate = pyautogui.center(location)
        return coordinate

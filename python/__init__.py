import time

import __util__
import __xlsx__


class Counter:
    index = 0
    time = 0

    def __init__(self, index, time):
        self.index = index
        self.time = time


sheet = __xlsx__.get_job_sheet('CSDN_点赞.xlsx')
index = 3

loop_stack = []

while index != -1:
    event_index = 'B' + str(index)
    event_value = sheet[event_index].value
    location_index = 'C' + str(index)
    location_value = sheet[location_index].value
    action_index = 'D' + str(index)
    action_value = sheet[action_index].value
    param_index = 'E' + str(index)
    param_value = sheet[param_index].value
    loop_index = 'F' + str(index)
    loop_value = sheet[loop_index].value

    if event_value is None:
        __util__.print_white('任务结束，单元格为空：' + event_index)
        exit(0)
    __util__.print_lavender('开始执行任务第 ' + str(index) + ' 行')

    if event_value == '循环开始':
        loop_stack.append(Counter(index + 1, int(loop_value)))
    if event_value == '循环结束':
        counter = loop_stack.pop()

        if counter.time > 1:
            counter.time -= 1
            loop_stack.append(counter)
            index = counter.index
        else:
            index += 1
            pass
        continue
    if event_value == '鼠标事件':
        __util__.mouse_event(location_index, location_value, action_value, param_value)
    if event_value == '键盘事件':
        __util__.keyboard_event(action_value, param_value)
    if event_value == '休眠':
        time.sleep(int(param_value))

    index += 1
    time.sleep(0.1)

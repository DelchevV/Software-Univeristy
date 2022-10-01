# from collections import deque
#
#
# def time_func(start_time):
#     seconds = int(start_time[2])
#     mins = int(start_time[1])
#     hours = int(start_time[0])
#     if seconds + 1 > 60:
#         seconds = 0
#         mins += 1
#     else:
#         seconds += 1
#     if mins > 60:
#         mins = 0
#         hours += 1
#     start_time=[hours,mins,seconds]
#     return start_time
#
#
# product_que = deque()
# robot_info = input().split(";")
# robot_info=deque(robot_info)
# starting_time = input().split(':')
# starting_time=[int(i) for i in starting_time]
# while True:
#     product = input()
#     if product == "End":
#         break
#     product_que.append(product)
# print(product_que)
#
# counter=0
# while product_que:
#     starting_time[2]+=1
#     starting_time = time_func(starting_time)
#     current_rob=robot_info.popleft()
#     name,timer = current_rob.split("-")
#     if counter==timer:
#         robot_info.append(current_rob)
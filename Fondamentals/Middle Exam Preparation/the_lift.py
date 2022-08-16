




# waiting_people=int(input())
# is_waiting_people=True
# is_free_spots=True
# state_of_the_lift=list(map(int,input().split()))
# for waggon in range(len(state_of_the_lift)):
#
#     current_free_spaces=0
#     if state_of_the_lift[waggon]<4:
#         if waiting_people>=4:
#             current_free_spaces = 4-state_of_the_lift[waggon]
#         else:
#             current_free_spaces=waiting_people
#         state_of_the_lift[waggon]+=current_free_spaces
#         waiting_people-=current_free_spaces
#     if waiting_people<=0:
#         print("The lift has empty spots!")
#         print(" ".join(str(st) for st in state_of_the_lift))
#         is_free_spots=False
#         break
# if waiting_people!=0:
#     for people in state_of_the_lift:
#         if people<4:
#             is_waiting_people=False
#             print(f"There isn't enough space! {waiting_people} people in a queue!")
#             print(" ".join(str(st) for st in state_of_the_lift))
#             break
# if  is_waiting_people and  is_free_spots:
#     print(" ".join(str(st) for st in state_of_the_lift))
#

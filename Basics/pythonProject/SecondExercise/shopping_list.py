budget=float(input())
video_card_pices=int(input())
processor_pices=int(input())
ram_pices=int(input())

video_card=250
processor=video_card*video_card_pices*0.35
ram=video_card*video_card_pices*0.1

total_video_card=video_card*video_card_pices
total_processor=processor*processor_pices
total_ram=ram*ram_pices

final=total_processor+total_ram+total_video_card

if video_card_pices>processor_pices:
    final=final-final*0.15
diffrence=abs(final-budget)
if final>budget:
    print(f"Not enough money! You need {diffrence:.2f} leva more!")
else:
    print(f"You have {diffrence:.2f} leva left!")
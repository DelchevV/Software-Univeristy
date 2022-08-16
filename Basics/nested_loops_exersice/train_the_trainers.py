judge_count=int(input())
command=input()
marks=0
all_marks_count=0
all_marks_sum=0

while command!="Finish":
    for i in range(judge_count):
        current_mark=float(input())
        marks+=current_mark
        all_marks_count+=1
        all_marks_sum+=current_mark
    average=marks/judge_count
    print(f"{command} - {average:.2f}.")
    average=0
    marks=0
    command=input()
final_average=all_marks_sum/all_marks_count
print(f"Student's final assessment is {final_average:.2f}.")

#deposite_amount=float(input())
#deposite_duration=int(input())
#year_percentage=float(input())

#sum=deposite_amount+deposite_duration*((deposite_amount*year_percentage)/12)
#print(sum)

deposite=float(input())
months=int(input())
annual_interest_percent=float(input())

annual_interest=deposite*annual_interest_percent/100
mounthly_interest= annual_interest/12
total_sum=deposite + mounthly_interest*months
print(total_sum)
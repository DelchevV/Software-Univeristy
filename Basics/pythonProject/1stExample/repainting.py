poliester_price=1.50
paint_price=14.50
paint_disolve_price=5.00
bags=0.40

poliester=float(input())
paint=float(input())
paint_disolve=float(input())
work_hours=int(input())

total_poliester=(poliester+2)*poliester_price
total_paint=(paint+paint*0.1)*paint_price
total_paint_disolve=paint_disolve*paint_disolve_price
total_supllies_price=total_paint+total_poliester+total_paint_disolve+bags
work_hours_cost=total_supllies_price*work_hours*0.30
final_price=total_supllies_price+work_hours_cost


print(final_price)


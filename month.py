print("month list='January,feb,march,april,may,jun,july,augest,septeber.octomber,descember")
month=input (print("enter month name"))
if month =='feb':
    print("no of days=28/29")
elif month  in("april","jun","septeber","november"):
    print("no of days=30")
elif month  in("January","march","may","july","augest","octomber","descember"):
    print("no of days =31")
else:
    print("invalid month name")

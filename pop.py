p-agadir = 500000
p-marrakech = 3000000
nbr-ans = 0
while p-marrakech > p-agadir:
p-agadir = p-agadir*1.08
p-marrakech = p-marrakech + 50000
nbr-ans = nbr-ans + 1
print("agadir dépasse marrakech apres",nbr-ans,"ans")

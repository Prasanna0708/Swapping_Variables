pc = 50000
laptop = 75000


pc = pc ^ laptop
laptop = pc ^ laptop
pc = pc ^ laptop

print(pc)
print(laptop)
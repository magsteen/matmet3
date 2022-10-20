

f_1 = lambda x : 4*x - 3
f_2 = lambda x : (4*x - 3)**2
f_3 = lambda x : (4*x - 3)**3
f_4 = lambda x : (4*x - 3)**(1/3)

print(f_1(0.74) - f_1(3/4))
print(f_2(0.74) - f_2(3/4))
print(f_3(0.74) - f_3(3/4))
print(f_4(0.74) - f_4(3/4))

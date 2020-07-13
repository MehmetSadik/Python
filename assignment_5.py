fb = []
i = 0
for i in range(-2, 8):
    if i < 0: fb.append(1)
    else: fb.append(fb[i] + fb[i+1])
    
print(fb)

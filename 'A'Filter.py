L = ['AUSHIM','LEEMA','AKHTAR','HIBA','NISANTH','AMAR']
count = 0
for i in L:
    if i[0] in 'aA':
        count += 1
        print(i)
print("Appearing",count,"times.")

ways = [0]*201
ways[0] = 1
for coins in [1,2,5,10,20,50,100,200]:
    for i in range(coins, 201):
        ways[i] += ways[i-coins]
print (ways[200])


# Function to check for bukhar based on temperature

def bukhaar_hai(temp):
    if(temp >37 and temp < 39):
        print("halka bukhar")
    elif temp>=39:
        print("Tez Bukhar")
    else:
        print("No")

bukhaar_hai(39)
bukhaar_hai(38)

bukhaar_hai(37)
i=1
while i<=5:
    print(i)
    i=i+1
 
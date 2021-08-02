#Design a Python Script to convert a given number to a roman number
sinp=input("Enter an integral number<=1000 : ")
digs=[]
r_n=str
try:#Using try/except to avoid string inputs
    int(sinp)
except:
    print("Invalid Input")
    exit()
if int(sinp) <= 0:
    print("Enter a number greater than zero")
    exit()
elif int(sinp) > 1000:
    print("A number <= 1000 should be entered")
    exit()

inp=int(sinp)
for dig in (sinp):# Splitting the number into digits and adding it to a list digs
    digs.append(int(dig))
#Creating three dictionaries for ones, tens and hundredths places
ones={0: '',1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
tens= {0: '',1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}
hds={0: '',1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D',6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'}

for k,v in ones.items():##For ones place
    if k == digs[len(digs)-1]:
            r_n=str(v)[::-1]
if len(sinp) >= 2:                                              #For example, if we take 14, the roman numeral is
    for k, v in tens.items(): # For tens digit                 #IV, from the dictionary we get the output for ones
        if k== digs[len(digs)-2]:                               #place as IV and for the tens place X, combining the two,
            r_n=r_n+v[::-1]                                     #we need to get four in the 
if len(sinp) == 3:                                              # four becomes VI
    for k,v in hds.items():#For hundredths place                #ten remains as X
        if k == digs[0]:                                        #the combined is VIX
            r_n = r_n+v[::-1]                                   #to avoid this we reverse the string XIV

if len(sinp) <= 3:
    print(r_n[::-1])
elif inp==1000:
    print("M")

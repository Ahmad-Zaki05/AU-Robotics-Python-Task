card_no = input ("Enter card number: ")

card_name = "Invalid"

if card_no[0] == '4':
    card_name = "Visa"
elif card_no[0:2] == "34" or card_no[0:2] == "37":
    card_name = "American Express"
elif int (card_no[0:2]) >= 51 and int (card_no[0:2]) <= 55:
    card_name = "MasterCard"
    
f = len (card_no) % 2
sum = 0
for (i, c) in enumerate (card_no):
    if i % 2 == f:
        x = int (c) * 2;
        while x > 0:
            sum += x % 10;
            x = x // 10
    else :
        sum += int (c)

if (sum  % 10 != 0):
    card_name = "Invalid"
    
print (card_name)

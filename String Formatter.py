def all_upper (s):
    x = ord ('a') - ord ('A')
    ns = ""
    for (c) in s:
        if c >= 'a' and c <= 'z':
            ns += chr (ord (c) - x)

    return ns

def all_lower (s):
    x = ord ('a') - ord ('A')
    ns = ""
    for (c) in s:
        if c >= 'A' and c <= 'z':
            ns += chr (ord (c) + x)

    return ns

def capital (s):
    ns = ""
    if s[0] >= 'a' and s[0] <= 'z':
        ns += chr (ord (s[0]) - (ord ('a') - ord ('A')))
    else :
        ns += s[0]

    ns += s[1:]

    return ns

def rev (s):
    ns = s[-1::-1]

    return ns

def format_string (s, l):
    for f in l:
        if f == 'uppercase':
            s = all_upper (s)
        elif f == 'lowercase':
            s = all_lower (s)
        elif f == 'reverse':
            s = rev (s)
        elif f == 'capitalize':
            s = capital (s)

    return s


s = input ("Enter string: ")
print ("You can format the string as follows:")
print ("enter uppercase to make the whole string\'s characters in uppercase")
print ("enter lowercase to make the whole string\'s characters in lowercase")
print ("enter reverse to reverse the string")
print ("enter capitalize to make first character of the string captial")

n = int (input ("Enter the number of operations you want: "))

print ("Start entering the operation you want each on a new line")

l = []

for i in range (n):
    l.append (input ())

s = format_string (s, l)

print (s)


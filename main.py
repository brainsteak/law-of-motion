#bismillah
print(" _       _ _ ")
print("| | ___ | (_)")
print("| |/ _ \| | |")
print("| | (_) | | |")
print("|_|\___/|_|_|")
print("              ")
print("Put values, if not have then write '?'")
a=input("Value of a(m/s^2):")
v=input("Value of v(m/s):")
u=input("Value of u(m/s):")
t=input("Value of t(s):")
if a=='?':
    print("a:",float(v)-float(u)/float(t)," m/s^2")

if v=='?':
    print("v:",float(u)+float(a)*float(t)," m/s")

if u=='?':
    print("u:",float(v)-float(a)*float(t)," m/s")

if t=='?':
    print("t:",float(v)-float(u)/float(a)," s")

else:
    print("You have all the values :)")

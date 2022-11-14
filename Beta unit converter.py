print("writen by Th3y C@ll m3 Am!r")
print("at first you HAVE to say to me which kind unit you want to convert")
print("then you can say what do you actually want to convert")
def Fahrenheit_to_Celsius(F):
    C = (F-32)*5/9
    print(c)
def Celsius_to_Fahrenheit(C):
    F = C*9/5+32
    print (F)
########################################
def Kilometer_to_Meter(KM):
    M = KM*1000
    print (M)
def Kilometer_to_Centimeter(KM):
    CM = KM*100000
    print (CM)
def Meter_to_Kilometer(M):
    KM = M/1000
    print (KM)
def Meter_to_Centimeter(M):
    CM = M*100
    print (CM)
def Centimeter_to_Kilometer(CM):
    KM = CM/100000
    print (KM)
def Centimeter_to_Meter(CM):
    M = CM/100
    print (M)
#not enough
########################################
def Second_to_Minute(S):
    M = S/60
    print (M)
def Minute_to_Second(M):
    S = M*60
    print (S)
def Minute_to_Hour(M):
    H = M/60
    print (H)
def Hour_to_Minute(H):
    M = H*60
    print(M)
def Second_to_Hour(S):
    H = S/3600
    print(H)
def Hour_to_Second(H):
    S = H*3600
    print(S)
#not enough
##############################################################
def Radical(R):
    N = R**(1/RISHE)
    print(N)
#perfect(gg)
##############################################################
z = str(input("which unit you want to convert ?: "))
if z == "temperature":
    t = str(input("what to what??: "))
    if t == "celesius to fahrenheit":
        c = int(input("enter a celesius value: "))
        Celsius_to_Fahrenheit(c)
    if t == "fahrenheit to celesius":
        f = int(input("enter a fahrenheit value: "))
        Fahrenheit_to_Celsius(f)
#enough(nice)
#############################################################

if z == "distance":
    d = str(input("what to what??: "))
    if d == "kilometer to meter":
        km = int(input("enter a kilometer value:  "))
        Kilometer_to_Meter(km)
    if d == "kilometer to centimeter":
        km = int(input("enter a kilometer value:  "))
        Kilometer_to_Centimeter(km)
    if d == "meter to kilometer":
        m = int(input("enter a meter value:  "))
        Meter_to_Kilometer(m)
    if d == "meter to centimeter":
        m = int(input("enter a meter value:  "))
        Meter_to_Centimeter(m)
    if d == "centimeter to kilometer":
        cm = int(input("enter a centimeter value:  "))
        Centimeter_to_Kilometer(cm)
    if d == "centimeter to meter":
        cm = int(input("enter a centimeter value:  "))
        Centimeter_to_Meter(cm)
############################################################

if z == "time":
    t = str(input("what to what??: "))
    if t == "hour to second":
        h = int(input("enter a hour value: "))
        Hour_to_Second(h)
    if t == "hour to minute":
        h = int(input("enter a hour value: "))
        Hour_to_Minute(h)
    if t == "minute to second":
        m = int(input("enter a minute value:  "))
        Minute_to_Second(m)
    if t == "minute to hour":
        m = int(input("enter a minute value:  "))
        Minute_to_Hour(m)
    if t == "second to minute":
        s = int(input("enter a second value:  "))
        Second_to_Minute(s)
    if t == "second to hour":
        s = int(input("enter a second value:  "))
        Second_to_Hour(s)
#############################################################
if z == "Radical":
    RISHE = int(input("rishe chand?"))
    r = int(input("enter a value: "))
    Radical(r)

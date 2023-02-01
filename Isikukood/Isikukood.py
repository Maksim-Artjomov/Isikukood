from omamoodul import *

ikood=""
while True:
    ikood=input("Sisesta isikukood: ")
    if pikkus(ikood)==False:
        print("Liiga oikk või lühike isikukood!")
    else:
        print("11 sümbolid")
        s=sugu(ikood)
        if s=="Viga!":
            print("Esimene täht ei ole õige!")
        else:
            print(s)
            if sunnipaev(ikood)=="Viga!":
                print("2-7 tähed on valesti sisestatud!")
            else:
                lause(ikood)

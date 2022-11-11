def hora12(hora,minutos):
    if hora<12 and hora>=0:

          pm_am(True,hora,minutos)
    elif hora>12 and hora <24:
        hora-=12
        pm_am(False,hora,minutos)
    elif hora==12:
        pm_am(False,hora,minutos)
    elif hora==24:
        pm_am(True,00,minutos)
def pm_am(manha:bool,hora,minutos):
    if manha:
        print(f"O formato da hora em 12 horas é {hora}:{minutos}AM")
    else:
        print(f"O formato da hora em 12 horas é {hora}:{minutos}PM")
hora=0
while (hora>=0):
    print("Primeiro digite as horas e depois de dar enter os minutos:(digite um numero negativo para horas para finalizar)")
    hora=int(input("digite as horas"))
    minutos=int(input("digite os minutos:"))
    hora12(hora,minutos)
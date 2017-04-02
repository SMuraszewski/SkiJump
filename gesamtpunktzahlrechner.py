# Skispringen Gesamtpunktzahl Rechner
# Man rechnet die Gesamtpunktzahl, inbegriffen Windregel und Gateregel
# Sebastian Muraszewski 2017

KPoints = float(input('K-Point:'))

Gate = str(input('Hat die Anlauflänge verändert?(j/n):'))
if Gate == str('j'):
    GateStart = int(input('Startgate:'))
    GateNo = int(input('Aktuellegate:'))
    GateMeters = float(input('Veränderung die Gate in Metern(oft 0.5 Meter pro Gate):'))
    GateFactor = float(input('Punktwert pro Meter:'))
    GatePoints = round(float(-GateMeters * GateFactor), 1)

else:
    GatePoints = 0

Distance = float(input('Weite:'))
extraDistance = float(Distance - KPoints)

if KPoints < float('100'):
    DistancePoints = float(60 + 2 * extraDistance)

elif KPoints < float('170'):
    DistancePoints = float(60 + 1.8 * extraDistance)

elif KPoints >= float('170'):
    DistancePoints = float(120 + 1.2 * extraDistance)

JudgeA = float(input('Punktrichter A:'))
JudgeB = float(input('Punktrichter B:'))
JudgeC = float(input('Punktrichter C:'))
JudgeD = float(input('Punktrichter D:'))
JudgeE = float(input('Punktrichter E:'))
Judges = float(JudgeA + JudgeB + JudgeC + JudgeD + JudgeE)
Marks = (str(JudgeA), str(JudgeB), str(JudgeC), str(JudgeD), str(JudgeE))
Highest = float(max(Marks))
Lowest = float(min(Marks))
JudgesPoints = float(Judges - Highest - Lowest)

Wind = float(input('Wind(Metern pro Sekunde, schreib Rückenwind mit Minus):'))
if Wind < float('0'):
    WindFactorTail = float(input('Wind-faktor für Rückenwind:'))
    WindPoints = round(float(Wind * -WindFactorTail), 1)

elif Wind == float('0'):
    WindPoints = 0

elif Wind > float('0'):
    WindFactorHead = float(input('Wind-faktor für Aufwind :'))
    WindPoints = round(float(Wind * -WindFactorHead), 1)

Total = GatePoints + DistancePoints + JudgesPoints + WindPoints

if Total < float('0'):
	Total = 0

else:
 	Total = Total

print('Punkte:', Total)
input('\nDrücken Sie die Eingabetaste um Programm zu schließen.')
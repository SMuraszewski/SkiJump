# Kalkulator not w skokach narciarskich
# Oblicza notę zawodnika, biorąc również pod uwagę rekompensatę za wiatr i belkę startową
# Sebastian Muraszewski 2017

KPoints = float(input('Punkt K:'))

Gate = str(input('Czy doszło do zmiany belki?(t/n):'))
if Gate == str('t'):
    GateStart = int(input('Belka, z której zaczynała się seria:'))
    GateNo = int(input('Aktualna belka:'))
    GateMeters = float(input('Różnica w metrach (najczęściej 0.5 metra na każdą belkę):'))
    GateFactor = float(input('Współczynnik zmiany belki:'))
    GatePoints = round(float(-GateMeters * GateFactor), 1)

else:
    GatePoints = 0

Distance = float(input('Dystans:'))
extraDistance = float(Distance - KPoints)

if KPoints < float('100'):
    DistancePoints = float(60 + 2 * extraDistance)

elif KPoints < float('170'):
    DistancePoints = float(60 + 1.8 * extraDistance)

elif KPoints >= float('170'):
    DistancePoints = float(120 + 1.2 * extraDistance)

JudgeA = float(input('Sędzia A:'))
JudgeB = float(input('Sędzia B:'))
JudgeC = float(input('Sędzia C:'))
JudgeD = float(input('Sędzia D:'))
JudgeE = float(input('Sędzia E:'))
Judges = float(JudgeA + JudgeB + JudgeC + JudgeD + JudgeE)
Marks = (str(JudgeA), str(JudgeB), str(JudgeC), str(JudgeD), str(JudgeE))
Highest = float(max(Marks))
Lowest = float(min(Marks))
JudgesPoints = float(Judges - Highest - Lowest)

Wind = float(input('Wiatry(metery na sekundę, wiatr z tyłu skoczni przyjmuje ujemną wartość):'))
if Wind < float('0'):
    WindFactorTail = float(input('Współczynnik dla wiatru z tyłu skoczni:'))
    WindPoints = round(float(Wind * -WindFactorTail), 1)

elif Wind == float('0'):
    WindPoints = 0

elif Wind > float('0'):
    WindFactorHead = float(input('Współczynnik dla wiatru pod narty:'))
    WindPoints = round(float(Wind * -WindFactorHead), 1)

total = GatePoints + DistancePoints + JudgesPoints + WindPoints


print('Łącznie:', total)
input('\nNaciśnij Enter, żeby zamknąć')
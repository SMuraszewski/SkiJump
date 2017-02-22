# Ski jumping points calculator
# Calculate total number of points, including gate and wind compensation
# Sebastian Muraszewski 2017

KPoints = float(input('K-Point:'))

Gate = str(input('Has the gate changed?(y/n):'))
if Gate == str('y'):
    GateStart = int(input('Base gate:'))
    GateNo = int(input('Actual gate:'))
    GateMeters = float(input('Difference in meters:'))
    GateFactor = float(input('Gate factor:'))
    GatePoints = round(float(-GateMeters * GateFactor), 1)

else:
    GatePoints = 0

Distance = float(input('Distance:'))
extraDistance = float(Distance - KPoints)

if KPoints < float('100'):
    DistancePoints = float(60 + 2 * extraDistance)

elif KPoints < float('170'):
    DistancePoints = float(60 + 1.8 * extraDistance)

elif KPoints >= float('170'):
    DistancePoints = float(120 + 1.2 * extraDistance)

JudgeA = float(input('Judge A:'))
JudgeB = float(input('Judge B:'))
JudgeC = float(input('Judge C:'))
JudgeD = float(input('Judge D:'))
JudgeE = float(input('Judge E:'))
Judges = float(JudgeA + JudgeB + JudgeC + JudgeD + JudgeE)
Marks = (str(JudgeA), str(JudgeB), str(JudgeC), str(JudgeD), str(JudgeE))
Highest = float(max(Marks))
Lowest = float(min(Marks))
JudgesPoints = float(Judges - Highest - Lowest)

Wind = float(input('Wind(meters per second, write tail wind with minus):'))
if Wind < float('0'):
    WindFactorTail = float(input('Wind factor for tail wind:'))
    WindPoints = round(float(Wind * -WindFactorTail), 1)

elif Wind == float('0'):
    WindPoints = 0

elif Wind > float('0'):
    WindFactorHead = float(input('Wind factor for head wind:'))
    WindPoints = round(float(Wind * -WindFactorHead), 1)

total = GatePoints + DistancePoints + JudgesPoints + WindPoints


print('Total:', total)
input('\nPress Enter to end the program')
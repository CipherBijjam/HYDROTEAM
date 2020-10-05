import csv
from collections import defaultdict

def weighted_decay_wqi(stationwise, station, alpha, num_neigh):
    m = num_neigh 
    if len(stationwise[station]) < m:
        m = len(stationwise[station])
    denm = ((1 - pow(alpha, m)) * alpha)/(pow(alpha, m) * (1 - alpha))
    num = 0

    for j in range(1, m+1):
        num += (1/pow(alpha,j)) * float(stationwise[station][-j][4])
    predicted_wqi = num/denm
    return predicted_wqi

def findWQI(filename):
    f = open(filename, 'r')
    rows = csv.DictReader(f)
    stationwise = defaultdict(lambda : [])
    stations = set()
    for row in rows:
        stationwise[row['Station']].append([row['TEMP'], row['TDS'], row['pH'], row['TURB'], row['WQI']])
        stations.add(row['Station'])
    ans = dict()
    for station in stations:
        val = weighted_decay_wqi(stationwise, station, 2.03, 10)
        ans[station] = val
    out_f = open("output.csv", "w")
    for station in stations:
        out_f.write(str(station) + "," + str(ans[station]) + "\n")
    out_f.close()

findWQI("input.csv")
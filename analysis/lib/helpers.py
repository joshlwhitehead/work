import csv

nm415 = 0
nm445 = 1
nm480 = 2
nm515 = 3
nm555 = 4
nm590 = 5
nm630 = 6
nm680 = 7
clear = 8
nir = 9

def getNameFromIndex(i):
    if i == nm415:
        return '415nm'
    if i == nm445:
        return '445nm'
    if i == nm480:
        return '480nm'
    if i == nm515:
        return '515nm'
    if i == nm555:
        return '555nm'
    if i == nm590:
        return '590nm'
    if i == nm630:
        return '630nm'
    if i == nm680:
        return '680nm'
    if i == clear:
        return 'clear'
    if i == nir:
        return 'nir'


def safeFloat(v):
    try:
        return float(v)
    except(ValueError, TypeError):
        return float('NaN')


def safeInt(v):
    try:
        return int(v)
    except(ValueError, TypeError):
        return float('NaN')


def loadCsvDataAsInt(csvPath):
    data = []
    with open(csvPath, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(list(map(safeInt, row)))

    return data

def loadCsvDataAsFloat(csvPath):
    data = []
    with open(csvPath, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(list(map(safeFloat, row)))

    return data





colorMap = [
  '#f44336', # red
  '#673ab7', # deep-purple
  '#03a9f4', # light-blue
  '#4caf50', # green
  '#ffc107', # amber
  '#00bcd4', # cyan
  '#3f51b5', # indigo
  '#e91e63', # pink
  '#8bc34a', # light-green
  '#9c27b0', # purple
  '#2196f3', # blue
  '#009688', # teal
  '#cddc39', # lime
  '#ff9800', # orange
  '#ff5722', # deep-orange
  '#795548', # brown
  '#607d8b', # blue-grey
  '#b71c1c', # red darken-4
  '#311b92', # deep-purple darken-4
  '#01579b', # light-blue darken-4
  '#1b5e20', # green darken-4
  '#f57f17', # yellow darken-4
  '#880e4f', # pink darken-4
  '#1a237e', # indigo darken-4
  '#006064', # cyan darken-4
  '#33691e', # light-green darken-4
  '#ff6f00', # amber darken-4
  '#4a148c', # purple darken-4
  '#0d47a1', # blue darken-4
  '#004d40', # teal darken-4
  '#827717', # lime darken-4
  '#e65100', # orange darken-4
  '#bf360c', # deep-orange darken-4
  '#3e2723', # brown darken-4
  '#263238', # blue-grey darken-4
  '#d32f2f', # red darken-2
  '#512da8', # deep-purple darken-2
  '#0288d1', # light-blue darken-2
  '#388e3c', # green darken-2
  '#f9a825', # yellow darken-3
  '#c2185b', # pink darken-2
  '#303f9f', # indigo darken-2
  '#0097a7', # cyan darken-2
  '#689f38', # light-green darken-2
  '#ffa000', # amber darken-2
  '#7b1fa2', # purple darken-2
  '#1976d2', # blue darken-2
  '#00796b', # teal darken-2
  '#afb42b', # lime darken-2
  '#f57c00', # orange darken-2
  '#e64a19', # deep-orange darken-2
  '#5d4037', # brown darken-2
  '#455a64', # blue-grey darken-2
  '#ff5252', # red accent-2
  '#7c4dff', # deep-purple accent-2
  '#40c4ff', # light-blue accent-2
  '#2e7d32', # green darken-3
  '#ff4081', # pink accent-2
  '#536dfe', # indigo accent-2
  '#00e5ff', # cyan accent-3
  '#76ff03', # light-green accent-3
  '#ffab00', # amber accent-4
  '#e040fb', # purple accent-2
  '#448aff', # blue accent-2
  '#1de9b6', # teal accent-3
  '#ffab40', # orange accent-2
  '#ff3d00', # deep-orange accent-3
  '#ff1744', # red accent-3
  '#f50057', # pink accent-3
  '#651fff', # deep-purple accent-3
  '#3d5afe', # indigo accent-3
  '#00b0ff', # light-blue accent-3
  '#00e676', # green accent-3
  '#00b8d4', # cyan accent-4
  '#64dd17', # light-green accent-4
  '#4db6ac', # teal lighten-2
  '#d500f9', # purple accent-3
  '#2979ff', # blue accent-3
  '#00bfa5', # teal accent-4
  '#aeea00', # lime accent-4
  '#ff9100' # orange accent-3
]

def getColor(i):
  return colorMap[i % (len(colorMap) - 1)]

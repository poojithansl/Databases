
def line2record(line):
    size = len(line)
    line = line.strip()
    svalues = line.split(',')
    values = list(map(int, svalues))
    return (size, values)

def record2line(record):
    svalues = list(map(str, record))
    outstring = ','.join(svalues) + '\n'
    return outstring


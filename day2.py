def reader(filename):
    reports = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            numbers = line.strip().split()
            reports.append(list(map(int, numbers)))
    return(reports)

def issafe(report):
    '''
    Deems if report is safe aka always decreases OR always increases,
    has no repeating numbers and does not increase or decrease
    by more than 3
    '''
    order = []
    for i in range(len(report)):
        if i==0:
            next
        else:
            if (report[i]>report[i-1]):
                if (abs(report[i] - report[i-1])<=3):
                    order.append(True) # Trues if increasing ok
                else:
                    order.append(False)
            elif (report[i]<report[i-1]):
                if (abs(report[i] - report[i-1])<=3):
                    order.append(False) # Falses if decreasing ok
                else:
                    order.append(True)
            elif (report[i]==report[i-1]):
                order.append('notok')
    allsame = all(element==order[0] for element in order)
    return(allsame)

def safereports(reports):
    ratings = []
    dampenedratings = []
    for report in reports:
        safety = issafe(report)
        ratings.append(safety)
        dampenedratings.append(safety)
        if safety==False:
            for i in range(len(report)):
                r = report[:]
                r.pop(i)
                #print(r, report)
                if (issafe(r)):
                    dampenedratings.append(True)
                    print(r, issafe(r))
                    break
    return(ratings.count(True), dampenedratings.count(True), len(dampenedratings))

reports = reader('/Users/piiamt/Documents/codes/Python/day2.txt')
test = reader('/Users/piiamt/Documents/codes/Python/day2test.txt')
print(safereports(reports))

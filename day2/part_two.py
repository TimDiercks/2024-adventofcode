import re

test = False
filePath = './test_input.txt' if test else './input.txt'

regex = r'\s'

with open(filePath, 'r') as f:
    data = f.read()
    data = data.split('\n')
    reactor_reports = [re.split(regex, d) for d in data if len(d) > 0]

def is_report_safe(report) -> bool:
    for i in range(len(report)):
        one_removed_report = report[0:i] + report[i+1:]
        differences = [int(b)-int(a) for (a,b) in zip(one_removed_report[:-1], one_removed_report[1:])]
        
        first_increasing = differences[0] > 0
        is_safe = all([x != 0 and abs(x) <= 3 and (x > 0) == first_increasing for x in differences])
        if is_safe:
            print(i, report, one_removed_report)
            return True
    return False

amount_safe_reports = sum(is_report_safe(report) for report in reactor_reports)
print(f"Safe reports: {amount_safe_reports}")
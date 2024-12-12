from functools import reduce

safety_level_distance = {'min':1, 'max':3}
reports = []
safe_reports_v1 = []
safe_reports_v2 = []

# Processing base data
with open('./data.txt', 'r') as data:
    for report in data.read().split('\n'):
        reports.append([int(level) for level in report.split(' ')])

# Checks
def distance_check(report):
    safe = True
    prev_level = None
    for level in report:
        if prev_level:
            distance = abs(prev_level-level)
            safe = safe and (safety_level_distance['min'] <= distance <= safety_level_distance['max'])
        prev_level = level
    return safe

def sequence_check(report):
    return (report == sorted(report) or report == sorted(report, reverse=True))

def checks_v2(report):
    result = distance_check(report) and sequence_check(report)
    if not result:
        posible_reports = []
        results = []
        for index in range(0, len(report)):
            posible_report = report.copy()
            posible_report.pop(index)
            posible_reports.append(posible_report)
            
        for posible_report in posible_reports:
            results.append(distance_check(posible_report) and sequence_check(posible_report))
        
        result = reduce(lambda accum, curr: accum or curr, results)

    return result

# Filter safe reports v1
for report in reports:
    safe = distance_check(report) and sequence_check(report)
    if safe:
        safe_reports_v1.append(report)

# Filter safe reports v2
for report in reports:
    safe = checks_v2(report)
    if safe:
        safe_reports_v2.append(report)

# Results
print('Result 1:')
print(len(safe_reports_v1))
print('\n')
print('Result 2:')
print(len(safe_reports_v2))
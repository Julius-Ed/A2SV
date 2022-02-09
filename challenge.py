
def activityNotifications(expenditure, d):

    transferAmount = [0] * 200

    for cashFlow in expenditure:
        transferAmount[cashFlow] += 1

    
    counter = 0
    for cashFlow in transferAmount:
        cashFlow += transferAmount[cashFlow]

        if d % 2 == 0 and cashFlow == (d + 1) // 2:
            median = cashFlow
        elif cashFlow == d // 2:
            median = cashFlow

    return median



spending = [2, 3, 4, 2, 3, 6, 8, 4, 5]
print(activityNotifications(spending, 4))

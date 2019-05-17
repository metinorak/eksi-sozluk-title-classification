def score_positive(test, pre):
    test_pre = zip(test,pre)
    count_true_positive = 0
    count_false_positive = 0
    
    
    for x,y in test_pre:
        if (x == 0 and y == 1):
            count_false_positive += 1
        
        elif (x == 1 and y == 1): 
            count_true_positive += 1
            
    if (count_true_positive + count_false_positive) == 0:
        return 0
    return count_true_positive/ (count_true_positive + count_false_positive)


def score_exclude_true_negative(test, pre):
    test_pre = zip(test,pre)
    count_true_positive = 0
    count_false_positive = 0
    count_false_negative = 0
    
    
    for x,y in test_pre:
        if (x == 0 and y == 1):
            count_false_positive += 1
        
        elif (x == 1 and y == 1): 
            count_true_positive += 1
        elif (x == 1 and y == 0):
            count_false_negative += 1
            
    if (count_true_positive + count_false_positive + count_false_negative) == 0:
        return 0
    return count_true_positive/ (count_true_positive + count_false_positive + count_false_negative)
#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here

    ###store list of errors
    error = abs(predictions - net_worths)

    ###zip up an unclean cleaned_data list
    cleaned_data = zip(ages, net_worths, error)

    ###sort the unclean clean data by error
    cleaned_data.sort(key=lambda tup: tup[2])

    #delete the last 10 entries which have the greatest error
    cleaned_data = cleaned_data[:81]

    return cleaned_data


# ECOR 1042 Lab 6 - Individual submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Kial Leroux-Malone"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101257343"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-22"

#==========================================#
# Place your histogram function after this line

from matplotlib import pyplot as plt

def histogram(list_: list[dict], string: str) -> None:
    """
    return the plot of a histogram depended upon string
    
    preconditions: None
    
    >>> histogram([{'Health': 4, 'Age': 10, 'School': 'GP'}, {'Health': 3, 'Age': 17, 'School': 'BP'}, {'Health': 3, 'Age': 12, 'School': 'GG'}], 'Health')
    None
    >>> histogram([{'Health': 4, 'G_Avg': 1.0, 'School': 'GP'}, {'Health': 3, 'G_Avg': 3.0, 'School': 'BP'}, {'Health': 3, 'G_Avg': 6.0, 'School': 'GG'}], 'G_Avg')
    None
    >>> histogram([{'Health': 4, 'Age': 10, 'School': 'GP'}, {'Health': 3, 'Age': 17, 'School': 'BP'}, {'Health': 3, 'Age': 12, 'School': 'GG'}], 'School')
    None
    """
    counting = {}
    
    for dictionary in list_:
        values = dictionary[string]
        
        if type(values) == float:
            values = int(values)
        if values not in counting:
            counting[values] = 0
        counting[values] += 1       
        
    figure1 = plt.figure(1, (5,5))
    plt.title(f'Histogram {string}')
    plt.xlabel(string)
    plt.ylabel('Counting')
    plt.bar(x = counting.keys(), height = counting.values())    
    plt.show()
    
    return None
# Do NOT include a main script in your submission

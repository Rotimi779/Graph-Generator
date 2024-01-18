# ECOR 1042 Lab 6 - Individual submission for text_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Nitten Purewal"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101270706"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-22"

#==========================================#
# Place your script for your text_UI after this line

import load_data
import sort
import histogram
import curve_fit
#import matplotlib.pyplot as plt
#import numpy as np


def main():
    """
    """
    while True:
        user_input = input("The available commands are \n  L)oad Data \n  S)ort Data \n  C)urve Fit \n  H)istogram \n  E)xit \n  Please type your command:")

        command = user_input.strip().lower()

        if command == "l":
            file_name = input("Please enter the name of the file:")
            if file_name != "student-test.csv" and file_name != "student-mat.csv":
                print("File not loaded. Please, load a valid file first.")
                
            attr = input("Please enter the attribute to use as a filter:")

            if attr == 'All':
                print(load_data.add_average(load_data.load_data(file_name, ('All', '0'))))

            else:
                value = input("Please enter the value of the attribute:")
                load_data_output = load_data.add_average(load_data.load_data(file_name, (attr, value)))
                print(load_data_output)

        if command == "s":
            file_name = input("Please enter the name of the file:")
            if file_name != "student-test.csv" and file_name != "student-mat.csv":
                print("File not loaded. Please, load a valid file first.")                
            
            attr_sort = input("Please enter the attribute you want to use for sorting,'Age','StudyTime' ,'Failures','G_Avg':")
            dic = load_data.add_average(load_data.load_data(file_name, ('All', '0')))
            order = input("Ascending (A) or Descending (D) order:")
            display = input("Data Sorted. Do you want to display the data?, Y or N:")
            
            display = display.strip().lower()
            order.strip().upper()
            attr_sort.strip().lower()
            
            if display == 'y':
                
                print(sort.sort_by_key(dic, order, attr_sort))
               
                    
            if display == 'n':
                print(None)
                    
                
        if command == "c":
            file_name = input("Please enter the name of the file:")
            if file_name != "student-test.csv" and file_name != "student-mat.csv":
                print("File not loaded. Please, load a valid file first.")            
            curve_attr = input("Please enter the attribute you want to use to find the best fit for G_Avg:")
            poly_order = int(input("Please enter the order of the polynomial to be fitted:"))
            dic = load_data.add_average(load_data.load_data(file_name, ('All', '0')))
            
            print(curve_fit.curve_fit(dic, curve_attr, poly_order))
            
        if command == "h":
            file_name = input("Please enter the name of the file:")
            
            if file_name != "student-test.csv" and file_name != "student-mat.csv":
                print("File not loaded. Please, load a valid file first.")            
            dic = load_data.add_average(load_data.load_data(file_name, ('All', '0')))
            hist_attr = input("Please enter the attribute you want to use for plotting:")
            
            print(histogram.histogram(dic, hist_attr))
            
        if command == "e":
            break
        
        if command != "l" and command != "s" and command != "c" and command != "h" and command != "e":
            print("Please choose a valid entry")
        
        
            
            


if __name__ == "__main__":
    main()







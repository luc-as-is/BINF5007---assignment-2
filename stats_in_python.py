import sys
import math


def load_data(filepath:str, column:int)->tuple[list, int]:
    # TODO - Complete the function so it loads the data from the file into a list
    # The function returns a tuple that contains the list of values and the total number 
    # of values in the column
    coldata = []
    count = 0
    with open (filepath, 'r') as infile:
        for line in infile:
            count += 1
            try:
                num = float(line.split("\t")[column])  
                if math.isnan(num) == False:
                    coldata.append(num)
                else:
                    pass
            except IndexError:
                print(f"ERROR: There were no valid list index (Column {column}) in file: {filepath}")
                sys.exit()
            except ValueError:
                pass
        if coldata == []:
                print(f"ERROR:There were no valid numbers in Column {column} in file: {filepath}")
                sys.exit()
    return [coldata,count,len(coldata)]


def calculate_average(numbers:list)->float:
    # TODO - Complete the function to return the average of the list of numbers
    mean = sum(numbers)/len(numbers)
    return mean


def get_max_and_min(numbers:list)->tuple[float, float]:
    # TODO - Complete the function to return a tuple with the maximum and minimum
    # values in the list, in that order
    max_number=max(numbers)
    min_number = min(numbers)
    return (max_number,min_number)


def calculate_variance(numbers:list)->float:
    # TODO - Complete the function to return the variance of the numbers in the list
    if len(numbers) == 1:
        variance = 0
    else:
        mean = calculate_average(numbers)
        sq_diff = []
        for num in numbers:
            sq_diff.append((num - mean) **2)
        variance = sum(sq_diff)/(len(numbers)-1)
    return variance


def calculate_std_dev(numbers:list)->float:
    # TODO - Complete the function to return the standard deviation of the numbers in the list
    std_dev = math.sqrt(calculate_variance(numbers))
    return std_dev


def calculate_median(number:list)->float:
    # TODO - Complete the function to return the median of the numbers in the list
    sort_list = sorted(number)
    if len(sort_list) % 2 == 0:
        ind1 = int(len(sort_list)/2)
        ind2 = int(ind1 -1)
        median = (sort_list[ind1] + sort_list[ind2]) /2
        return float(median)
    else:
        ind = len(sort_list)//2
        median = sort_list[ind]
        return float(median)
    

file = 'labs/assignment2/BINF5007---assignment-2/data_file2.txt'
data_column = 4

print(file)
print(f'Column {data_column}')

dat = load_data(file,data_column)

print(f'Count = {dat[1]}')
print(f'ValidNum = {dat[2]}')
print(f'Average = {calculate_average(dat[0])}')
print(f'Maximum = {get_max_and_min(dat[0])[0]}')
print(f'Minimum = {get_max_and_min(dat[0])[1]}')
print(f'Variance = {calculate_variance(dat[0])}')
print(f'Standard Deviation = {calculate_std_dev(dat[0])}')
print(f'Median = {calculate_median(dat[0])}')
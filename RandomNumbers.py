# Random Numbers
import datetime

def add_all_digits_v2(number):
    """
    Add all digits until it's a single digit
    """
    while len(number) > 1:
        sum = 0
        for digit in number:
            sum += int(digit)
        number = str(sum)
    return number
# Move this adding all digits to a function
def add_all_digits(number):
    sum = 0
    for digit in number:
        sum += int(digit)
    return sum


def random_numbers():
    current_time = datetime.datetime.now()
    # Convert the whole string to number removing special characters
    whole_big_number = current_time.strftime("%Y%m%d%H%M%S")
    # Add each digit of the number
    sum1 = add_all_digits(whole_big_number)

    # Take out the last two digits of the number
    last_two_digits = whole_big_number[-2:]

    # Consider last two digits as years and get the timestamp excatly those years back
    years = int(last_two_digits)
    years_back = datetime.datetime.now() - datetime.timedelta(days=years * 365)

    # Now again add all the digits of this timestamp
    whole_big_number_2 = years_back.strftime("%Y%m%d%H%M%S")
    sum2 = add_all_digits(whole_big_number_2)

    # Add the two sums
    final_sum = sum1 + sum2
    return final_sum


def random_v2(digit):
    """
    This function takes current time stamp and returns last two digits of the timestamp
    """
    current_time = datetime.datetime.now()
    microseconds = current_time.microsecond
    last_digit = microseconds % 10
    dividend = 10**digit
    """ #Determine if last digit even or odd
    if last_digit % 2 == 0:
        #If even, return last digit
        dividend = 10
    else:
        #If odd, return last two digits
        dividend = 100
    #Determine if last digit is prime
    if last_digit == 2 or last_digit == 3 or last_digit == 5 or last_digit == 7:
        dividend = 1000 """
    random = microseconds % dividend
    return random

def random_4_digit():
    """
    This function takes current time stamp and returns last 4 digits of the timestamp
    """
    current_time = datetime.datetime.now()
    microseconds = current_time.microsecond
    random = microseconds % 10000
    return random

def random_3_digit():
    """
    This function takes current time stamp and returns last 3 digits of the timestamp
    """
    current_time = datetime.datetime.now()
    microseconds = current_time.microsecond
    random = microseconds % 1000
    return random

def PRNG(digit):
    import psutil

    total_threads = sum(p.num_threads() for p in psutil.process_iter())
    random = total_threads % 10**digit if digit else total_threads
    return random

def plot_random_numbers():
    import time

    # Generate these random numbers for 1 minute of time
    # And then plot a graph of these numbers against time
    import matplotlib.pyplot as plt
    import numpy as np

    # Generate random numbers for 3 minutes of time
    start_time = time.time()
    end_time = start_time + 1  # 1 sec

    time_values = []
    y_axis = [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
        31,
        32,
        33,
        34,
        35,
        36,
        37,
        38,
        39,
        40,
        41,
        42,
        43,
        44,
        45,
        46,
        47,
        48,
        49,
        50,
        51,
        52,
        53,
        54,
        55,
        56,
        57,
        58,
        59,
        60,
        61,
        62,
        63,
        64,
        65,
        66,
        67,
        68,
        69,
        70,
        71,
        72,
        73,
        74,
        75,
        76,
        77,
        78,
        79,
        80,
        81,
        82,
        83,
        84,
        85,
        86,
        87,
        88,
        89,
        90,
        91,
        92,
        93,
        94,
        95,
        96,
        97,
        98,
        99,
        100,
    ]
    random_values = []
    p_random_values = []
    while time.time() < end_time:
        #My random Number
        current_time = datetime.datetime.now()
        random_number = PRNG(1)
        random_values.append(random_number)

        time_values.append(current_time)
        #Python's random number
        p_random = np.random.randint(10)
        p_random_values.append(p_random)
        
        print(f"My random number is {random_number}")
        print(f"Python's random number is {p_random}")
        

    # Plot the graph of random numbers
    plt.plot(time_values, random_values)
    plt.plot(time_values, p_random_values)
    plt.xlabel("Time")
    plt.ylabel("Random Number")
    plt.title("Random Numbers vs Time")
    plt.legend()
    plt.show()


import psutil

""" # Get disk usage
disk_usage = psutil.disk_usage('/')
print(disk_usage)

# Get disk partitions
disk_partitions = psutil.disk_partitions()
print(disk_partitions) """

# Get disk I/O statistics
disk_io = psutil.disk_io_counters()
print(disk_io)
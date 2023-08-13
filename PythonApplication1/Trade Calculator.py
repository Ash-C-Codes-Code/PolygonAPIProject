from polygon import RESTClient
import datetime
import numpy

CLIENT = RESTClient(api_key="n7T7pW1Ius5xnMnQmOe_37XNGLNWavdu")
ticker = "AAPL"

class dailyData:
    """
    Class that is identical to the object returned by the API call
    """
    high: 0
    low: 100000
    open: 0
    close: 0
    timestamp: 0

# start off by setting todays date as the start/end date.
startDateInput = datetime.datetime.now()
endDateInput = datetime.datetime.now()

def formatInputDates(date):
    """
    format the date (dd/mm/YYYY), used double check that the input is correctly formatted.

    : param1 date: The start date or end date to format.

    """
    try:
        returnValue = datetime.datetime.strptime(date, "%d/%m/%Y")
    except:
        returnValue = ""

    return returnValue

def formatDates(date):
    """
    format the date (YYYY-mm-dd), used to format in the way Polygon accepts.

    : param1 date: The start date or end date to format.

    """
    returnValue = datetime.datetime.strptime(date, "%d/%m/%Y")
    returnValue = returnValue.strftime("%Y-%m-%d")

    return returnValue

def getInputs():
    """
    Get the start date using user input, then check its correctly formatted.
    Then get the end date the same way and check again.

    """
    global startDateInput
    global endDateInput

    startDateInput = input("Enter the start date in dd/mm/yyyy format, or to exit input exit: ")
    if (startDateInput.upper() == "EXIT"):
        exit()

    while (formatInputDates(startDateInput) == ""):
        startDateInput = input("Invalid input, enter the start date in dd/mm/yyyy format, or to exit input exit: ")
        if (startDateInput.upper() == "EXIT"):
            exit()

    endDateInput = input("Enter the end date in dd/mm/yyyy format, or to exit input exit: ")
    if (endDateInput.upper() == "EXIT"):
        exit()

    while (formatInputDates(endDateInput) == ""):
        endDateInput = input("Invalid input, enter the end date in dd/mm/yyyy format, or to exit input exit: ")
        if (endDateInput.upper() == "EXIT"):
            exit()

def getData():
    """
    Handles the API call.
    Calculate the highest and lowest values between the date inputs
    """
    global startDateInput
    global endDateInput

    # List Aggregates (Bars)
    aggs = []
    highest = dailyData()
    highest.high = 0
    lowest = dailyData()
    lowest.low = 100000
    for a in CLIENT.list_aggs(ticker=ticker, multiplier=1, timespan="day", from_=formatDates(startDateInput), to=formatDates(endDateInput), limit=50000):
        print(a)
        #print("High: " + str(a.high))
        #print("Low: " + str(a.low))
        #print("Open: " + str(a.open))
        #print("Close: " + str(a.close))
        #timestamp must be divided by 1000 to be able to be converted to a datetime object
        #print("Timestamp: " + datetime.datetime.fromtimestamp(a.timestamp/1000).strftime("%d/%m/%Y"))
        aggs.append(a)
        if (a.high > highest.high):
            highest = a
        if (a.low < lowest.low):
            lowest = a

    print("Highest: " + str(highest.high) + ", on " + datetime.datetime.fromtimestamp(highest.timestamp/1000).strftime("%d/%m/%Y"))
    print("Lowest: " + str(lowest.low) + ", on " + datetime.datetime.fromtimestamp(lowest.timestamp/1000).strftime("%d/%m/%Y"))
    calculateData(aggs)

def sortByTimestamp(a):
    """
    Returns the time stamp of the days values
    Used for sorting

    """
    return a.timestamp

def calculateData(data):
    """
    Calculates the average of each day

    """
    #Calculate the averages
    data.sort(key=sortByTimestamp)
    averages = []
    for point in data:
        #Calculate the average by finding the middle value between the highest and lowest points in a day
        difference = point.high - point.low
        print("High: " + str(point.high) + ", Low: " + str(point.low))
        average = round(point.low + (difference / 2), 2)
        print("Average: " + str(average))
        averages.append(average)
    print(averages)
    #Do the averages show to be increasing or decreasing
    #If an increase of 4%-15% then increasing, if increasing by 15% or more strongly increasing
    #If an decrease of 4%-15% then decreasing, if decreasing by 15% or more strongly decreasing
    #If increasing/decreasing within 4% then it is stable
    increased = "increasing"
    calculation = averages[-1] - averages[0]
    percentageAmount = 0
    if (calculation >= 0):
        percentageAmount = round(((averages[0] + calculation) / averages[0]) * 100, 2)
        print("Interest: " + str(percentageAmount - 100) + "%")
    else:
        percentageAmount = round(((averages[0] + (calculation * -1)) / averages[0]) * 100, 2)
        print("Decrease: " + str(percentageAmount - 100) + "%")
        increased = "decreasing"

    if (percentageAmount <= 4):
        print("Stock is stable at " + str(percentageAmount - 100) + "% " + increased)
    else:
        strongChange = ""
        if (percentageAmount >= 15):
            strongChange = "Strongly "

        print("Stock has been " + strongChange + increased + " with a rate of " + str(percentageAmount - 100) + "%")
    #Percentage difference between each average
    index = 0
    print("Length of Averages " + str(len(averages)))
    if (len(averages) >= 2):
        for a in averages:
            if (index < len(averages) - 1):
                difference = averages[index + 1] - a
                startDate = datetime.datetime.fromtimestamp(data[index].timestamp/1000).strftime("%d/%m/%Y")
                endDate = datetime.datetime.fromtimestamp(data[index + 1].timestamp/1000).strftime("%d/%m/%Y")
                if (difference > 0):
                    percentageAmount = round((a + difference) / a, 2) * 100
                    print("Increase of " + str(percentageAmount - 100) + "% between " + startDate + " and " + endDate + ".")
                elif (difference < 0):
                    percentageAmount = round((a + difference * -1) / a, 2) * 100
                    print("Decrease of " + str(percentageAmount - 100) + "% between " + startDate + " and " + endDate + ".")
                else:
                    print("No Changes between " + startDate)
                index += 1
    else:
        print("Dates given can not allow a calculation of averages")




#
def calculateData():
    """
    Get the user inputs and then confirm with the user.
    They can then choose to input again.
    Then gets the data.

    """
    global startDateInput
    global endDateInput

    getInputs()
    userConfirmation = input("Do you want to get the data from " + startDateInput + " to " + endDateInput + " ? (Y/N) ")
    while (not(userConfirmation == 'Y' or userConfirmation == 'N')):
        userConfirmation = input("Input invalid, do you want to get the data from " + startDateInput + " to " + endDateInput + " ? (Y/N) ")

    if (userConfirmation == 'N'):
        getInputs()
    else:
        getData()
        main()

def selling():
    print("Yet to be implemented...")
    main()

def buying():
    print("Yet to be implemented....")
    main()

def main():
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    print("|-----------------------------------------TRADE CALCULATOR-----------------------------------------|")
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n\n")
    print("1: Show Trends")
    print("2: Selling")
    print("3: Buying")
    print("4: Exit")
    choice = input("\nEnter the number option depending on what action you want to carry out:")
    match choice:
        case "1":
            calculateData()
        case "2":
            selling()
        case "3":
            buying()
        case "4":
            exit()

main()
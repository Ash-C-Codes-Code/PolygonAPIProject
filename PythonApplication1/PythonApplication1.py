from polygon import RESTClient
import datetime
import json

CLIENT = RESTClient(api_key="n7T7pW1Ius5xnMnQmOe_37XNGLNWavdu")
ticker = "AAPL"

class dailyData:
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
        #print("Timestamp: " + datetime.datetime.fromtimestamp(a.timestamp/1000).strftime("%d/%m/%Y"))
        aggs.append(a)
        if (a.high > highest.high):
            highest = a
        if (a.low < lowest.low):
            lowest = a

    #print(aggs)
    print("Highest: " + str(highest.high) + ", on " + datetime.datetime.fromtimestamp(highest.timestamp/1000).strftime("%d/%m/%Y"))
    print("Lowest: " + str(lowest.low) + ", on " + datetime.datetime.fromtimestamp(lowest.timestamp/1000).strftime("%d/%m/%Y"))

#
def main():
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


main()
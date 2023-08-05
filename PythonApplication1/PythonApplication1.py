from polygon import RESTClient
import datetime
import json

CLIENT = RESTClient(api_key="n7T7pW1Ius5xnMnQmOe_37XNGLNWavdu")
ticker = "AAPL"

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
    for a in CLIENT.list_aggs(ticker=ticker, multiplier=1, timespan="day", from_=formatDates(startDateInput), to=formatDates(endDateInput), limit=50000):
        print(a)
        print("High: " + str(a.high))
        print("Low: " + str(a.low))
        print("Open: " + str(a.open))
        print("Close: " + str(a.close))
        print("Timestamp: " + datetime.datetime.fromtimestamp(a.timestamp/1000).strftime("%d/%m/%Y"))
        aggs.append(a)

    print(aggs)

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

    #[Agg(open=196.235, high=196.73, low=195.28, close=195.605, volume=35281426.0, vwap=195.8486, timestamp=1690862400000, transactions=477616, otc=None), Agg(open=195.04, high=195.18, low=191.8507, close=192.58, volume=50388811.0, vwap=192.9395, timestamp=1690948800000, transactions=620582, otc=None)]


main()
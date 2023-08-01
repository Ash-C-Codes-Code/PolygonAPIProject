from polygon import RESTClient
import datetime

CLIENT = RESTClient(api_key="n7T7pW1Ius5xnMnQmOe_37XNGLNWavdu")
ticker = "AAPL"

# start off by setting todays date as the start/end date.
startDate = datetime.datetime.now()
endDate = datetime.datetime.now()

def formatInputDates(date):
    """
    format the date (dd/mm/YYYY), used double check that the input is correctly formatted.

    : param1 date: The start date or end date to format.

    """
    return date.strftime("%d-%m-%Y")

def formatDates(date):
    """
    format the date (YYYY/mm/dd), used to format in the way Polygon accepts.

    : param1 date: The start date or end date to format.

    """
    return date.strftime("%Y-%m-%d")

def getInputs():
    """
    Get the start date using user input, then check its correctly formatted.
    Then get the end date the same way and check again.

    """
    startDateInput = input("Enter the start date in dd/mm/yyyy format, or to exit input exit: ")
    if (startDateInput.upper() == "EXIT"):
        exit()
    while (startDateInput == formatInputDates(startDateInput)):
        startDateInput = input("Enter the start date in dd/mm/yyyy format, or to exit input exit: ")
        if (startDateInput.upper() == "EXIT"):
            exit()
    endDateInput = input("Enter the end date in dd/mm/yyyy format, or to exit input exit: ")
    if (endDateInput.upper() == "EXIT"):
        exit()
    while (endDateInput == formatInputDates(endDateInput)):
        endDateInput = input("Enter the start date in dd/mm/yyyy format, or to exit input exit: ")
        if (endDateInput.upper() == "EXIT"):
            exit()

def getData():
    # List Aggregates (Bars)
    aggs = []
    for a in CLIENT.list_aggs(ticker=ticker, multiplier=1, timespan="minute", from_=formatDates(startDate), to=formatDates(endDate), limit=50000):
        aggs.append(a)

    print(aggs)

#
def main():
    """
    Get the user inputs and then confirm with the user.
    They can then choose to input again.
    Then gets the data.

    """
    getInputs()
    userConfirmation = input("Do you want to get the data from " + startDate + " to " + endDate + " ? (Y/N) ")
    while (userConfirmation != "Y" or userConfirmation != "N"):
        userConfirmation = input("Input invalid, do you want to get the data from " + startDate + " to " + endDate + " ? (Y/N) ")
    if (userConfirmation == "N"):
        getInputs()
    else:
        getData()

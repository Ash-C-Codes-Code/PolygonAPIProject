from token import NUMBER
from polygon import RESTClient
from currency_converter import CurrencyConverter
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QDateEdit
from PyQt6.QtCore import Qt, QDateTime
from PyQt6.QtGui import QFont
import datetime


CLIENT = RESTClient(api_key="n7T7pW1Ius5xnMnQmOe_37XNGLNWavdu")
ticker = "AAPL"
c = CurrencyConverter()
APP = QApplication([])

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
    notConfirmed = True
    stockToSell = "AAPL"
    tickerNames = [];
    tickers = []
    count = 0;
    #Get list of all possible stock codes
    for a in CLIENT.list_tickers(market='stocks', limit=100):
        tickers.append(a.ticker);
        tickerNames.append(a.name);
        count = count + 1;
        print(str(count) + ": " + a.name + " (" + a.ticker + ")");
        
    # while (notConfirmed):
    #     stockToSell = input("Enter the code for the stock you want to check: ")
    #     if (stockToSell != ""):
    #         confirmationDecision = input("Are you sure you want to check " + stockToSell + " stock? (Y/N) ")
    #         if (confirmationDecision == "Y"):
    #             notConfirmed = False

    # for a in CLIENT.list_aggs(ticker=stockToSell, multiplier=1, timespan="day", from_=formatDates(startDateInput), to=formatDates(endDateInput), limit=50000):
    #     print(a)
    #     #print("High: " + str(a.high))
    #     #print("Low: " + str(a.low))
    #     #print("Open: " + str(a.open))
    #     #print("Close: " + str(a.close))
    #     #timestamp must be divided by 1000 to be able to be converted to a datetime object
    #     #print("Timestamp: " + datetime.datetime.fromtimestamp(a.timestamp/1000).strftime("%d/%m/%Y"))
    #     aggs.append(a)
    #     if (a.high > highest.high):
    #         highest = a
    #     if (a.low < lowest.low):
    #         lowest = a

    # print("Highest: " + str(highest.high) + ", on " + datetime.datetime.fromtimestamp(highest.timestamp/1000).strftime("%d/%m/%Y"))
    # print("Lowest: " + str(lowest.low) + ", on " + datetime.datetime.fromtimestamp(lowest.timestamp/1000).strftime("%d/%m/%Y"))
    # calculateData(aggs)

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
        print("Increase: " + str(percentageAmount - 100) + "%")
    else:
        percentageAmount = round(((averages[0] + (calculation * -1)) / averages[0]) * 100, 2)
        print("Decrease: " + str(percentageAmount - 100) + "%")
        increased = "decreasing"

    if ((percentageAmount-100) <= 4):
        print("Stock is stable at " + str(percentageAmount - 100) + "% " + increased)
    else:
        strongChange = ""
        if ((percentageAmount-100) >= 15):
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
def confirmDates():
    """
    Get the user inputs and then confirm with the user.
    They can then choose to input again.
    Then gets the data.

    """
    global startDateInput
    global endDateInput
    
    #GUI Window for the trends
    trendsWindow = QMainWindow();
    trendsWindow.setWindowTitle("Trade Calculator - Trends");
    titleLayout = QHBoxLayout();
    datesLayout = QHBoxLayout();
    buttonLayout = QHBoxLayout();
    dateAndButtonVLayout = QVBoxLayout();

    #Create GUI Labels and Title
    title = QLabel('TRADE CALCULATOR - TRENDS');
    title.setFont(QFont("Futura", 50, 15));
    title.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignBottom);
    
    startDateLabel = QLabel('Start Date:');
    startDateLabel.setFont(QFont("Futura", 15, 8));
    startDateLabel.setAlignment(Qt.AlignmentFlag.AlignLeft);
    startDateLabel.setFixedSize(100, 40);
    
    endDateLabel = QLabel('End Date:');
    endDateLabel.setFont(QFont("Futura", 15, 8));
    endDateLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter);
    endDateLabel.setFixedSize(100, 40)
    
    #Create GUI confirm and back button
    backBtn = QPushButton(text='Back');
    backBtn.setFont(QFont("Futura", 10, 5));
    backBtn.setFixedSize(100, 50);
    
    confirmBtn = QPushButton(text='Confirm');
    confirmBtn.setFont(QFont("Futura", 15, 10));
    confirmBtn.setFixedSize(250, 40);
    
    #Create GUI Date pickers for start/end date
    startDate = QDateEdit();
    startDate.setCalendarPopup(True);
    startDate.setAlignment(Qt.AlignmentFlag.AlignTop);
    startDate.setFixedSize(250, 40);
    startDate.setDateTime(QDateTime.addDays(QDateTime.currentDateTime(), -7));
    endDate = QDateEdit();
    endDate.setCalendarPopup(True);
    endDate.setAlignment(Qt.AlignmentFlag.AlignTop);
    endDate.setFixedSize(250, 40);
    endDate.setDateTime(QDateTime.currentDateTime());
    endDate.setMaximumDateTime(QDateTime.currentDateTime());
    startDate.setMaximumDateTime(QDateTime.addDays(endDate.dateTime(), -1));
    endDate.setMinimumDateTime(QDateTime.addDays(startDate.dateTime(), 1));
    
    
    #Add all widgets to their respective layouts
    titleLayout.addWidget(backBtn);
    titleLayout.addWidget(title);
    datesLayout.addWidget(startDateLabel);
    datesLayout.addWidget(startDate);
    datesLayout.addWidget(endDateLabel);
    datesLayout.addWidget(endDate);
    buttonLayout.addWidget(confirmBtn);
    buttonLayout.setAlignment(Qt.AlignmentFlag.AlignRight);
    buttonsWidget = QWidget();
    buttonsWidget.setLayout(buttonLayout);
    datesWidget = QWidget();
    datesWidget.setLayout(datesLayout);
    dateAndButtonVLayout.addWidget(datesWidget);
    dateAndButtonVLayout.addWidget(buttonsWidget);
    
    
    #Set the layout widgets and add to windows
    titleWidget = QWidget();
    titleWidget.setLayout(titleLayout);
    trendsWindow.setMenuWidget(titleWidget);
    dateAndButtonWidget = QWidget();
    dateAndButtonWidget.setLayout(dateAndButtonVLayout);
    trendsWindow.setCentralWidget(dateAndButtonWidget);
    trendsWindow.resize(1000, 500);
    
    #functions for button clicks
    def confirmBtnClicked():
        print("Confirm Clicked");
        trendsWindow.close();
        getData();
        
    def backBtnClicked():
        print("Back Clicked");
        trendsWindow.close();
        main();
        
    #Calls for when buttons are clicked
    confirmBtn.clicked.connect(confirmBtnClicked);
    backBtn.clicked.connect(backBtnClicked);
    
    trendsWindow.show();

    # getInputs()
    # userConfirmation = input("Do you want to get the data from " + startDateInput + " to " + endDateInput + " ? (Y/N) ")
    # while (not(userConfirmation == 'Y' or userConfirmation == 'N')):
    #     userConfirmation = input("Input invalid, do you want to get the data from " + startDateInput + " to " + endDateInput + " ? (Y/N) ")

    # if (userConfirmation == 'N'):
    #     getInputs()
    # else:
    #     getData()
    #     main()

def selling():
    sellingWindow = QMainWindow();
    sellingWindow.setWindowTitle("Trade Calculator - Selling");
    aggs = []
    #preNow = datetime.datetime.now()
    #now = datetime.datetime.now()
    #print(preNow)
    #print(now)
    #print(preNow.strftime("%Y-%m-%d"))
    #print(now.strftime("%Y-%m-%d"))
    errored = True
    index = 0
    latestDate = datetime.datetime.now()
    notConfirmed = True
    stockToSell = "AAPL"

    while (notConfirmed):
        stockToSell = input("Enter the code for the stock you want to sell: ")
        if (stockToSell != ""):
            confirmationDecision = input("Are you sure you want to sell " + stockToSell + " stock? (Y/N) ")
            if (confirmationDecision == "Y"):
                notConfirmed = False

    ## Do a for each loop where we do a try catch around this for each loop, increasing the number of days that we are taking away from now until the for each succeeds
    while (errored):
        if index != 0:
            latestDate = datetime.datetime.now() - datetime.timedelta(days=index)
        try:
            print(latestDate.strftime("%Y-%m-%d"))
            for a in CLIENT.list_aggs(ticker=stockToSell, multiplier=10, timespan="minute", from_=latestDate.strftime("%Y-%m-%d"), to=latestDate.strftime("%Y-%m-%d"), limit=5000):
                print(a)
                print("Time: " + datetime.datetime.fromtimestamp(a.timestamp/1000).strftime("%d/%m/%Y %H:%M:%S"))
                aggs.append(a)
            errored = False
        except:
            errored = True
            index += 1
    print("Last Price: " + str(aggs[-1].high) + " - " + str(aggs[-1].low) + " GBP at " + datetime.datetime.fromtimestamp(aggs[-1].timestamp/1000).strftime("%d/%m/%Y %H:%M:%S"));
    hasStock = input("Do you want to sell? (Y/N) ")
    if (hasStock == "Y"):
        amountToGain = 0
        stockAmount = input("How much stock (in Units) do you have? ")
        sellAmount = input("How much stock (in Units) do you want to sell, enter 'ALL' if you want to sell all the stock? ")
        difference = aggs[-1].high - aggs[-1].low
        sellValue = round(aggs[-1].low + (difference / 2), 2)
        if (sellAmount.upper() == 'ALL'):
            print("All selected")
            print("Amount recieved after selling: " + str(round(sellValue * float(stockAmount), 2)) + "(GBP)")
            amountToGain = round(sellValue * float(stockAmount), 2)
        else:
            print("All not selected")
            print("Amount recieved after selling: " + str(round(sellValue * float(sellAmount), 2)) + "(GBP)")
            print("Amount of units left after selling: " + str(float(stockAmount) - float(sellAmount)) + " Units")
            amountToGain = round(sellValue * float(sellAmount), 2)
    
        convertLoop = True;
        while (convertLoop):
            doConvert = input("Would you like to convert the amount into a different currency? (Y/N)");
            if (doConvert == "Y"):
                convertedAmount = convertToCurrency(amountToGain);
                if (convertedAmount == "Invalid currency code"):
                    print ("Could not convert, due to invalid currency code");
                elif (convertedAmount == "Could not find the date of the last currency conversion"):
                    print("Could not convert, due to the invalid currency conversion");
                else:
                    print("After conversion: " + convertedAmount + " .");
                    convertLoop = False;
            elif (doConvert == "N"):
                convertLoop = False;
        main()
    else:
        main()



   
        
        
def convertToCurrency(amountToGain):
    """
    Asks the user what currency they want to convert to                
    Converts to that currency using API to get current values and returns                
    """                
    userCurrencyCode = input("Please enter the three letter currency code: ");                
    userCurrencyCode = userCurrencyCode.upper();                
    if (userCurrencyCode in c.currencies):
        errored = True
        index = 0;
        while(errored):
            if (index != 0):
                latestDate = datetime.datetime.now() - datetime.timedelta(days=index)
            else:
                latestDate = datetime.datetime.now()
            try:
                convertedAmount = c.convert(amountToGain, 'GBP', userCurrencyCode, date = latestDate.strftime("%Y-%m-%d"));
                errored = False;
                return str(convertedAmount) + " In " + userCurrencyCode;
            except:
                errored = True
                index += 1;
        return "Could not find the date of the last currency conversion"                                         
    else:
        return "Invalid currency code"



    #! Wont work because can only make a api call per minute
    # get the latest weeks results, to find the date of the last value
    #latestDate = datetime.datetime.fromtimestamp(aggs[-1].timestamp/1000).strftime("%d/%m/%Y")
    #print(latestDate)
    #for a in CLIENT.list_aggs(ticker=ticker, multiplier=5, timespan="minute", from_=latestDate, to=latestDate, limit=50000):
    #    print(a)
    #userTicker = print("Enter the Stock name code:")
    #if (userTicker != ""):
    #    for a in CLIENT.list_aggs(ticker=ticker, multiplier=1, timespan="day", from_=preNow.strftime("%Y-%m-%d"), to=now.strftime("%Y-%m-%d"), limit=120):
    #        aggs.append(a)
    #print("Price at this moment: " + a[0])
    #main()

def buying():
    buyingWindow = QMainWindow();
    buyingWindow.setWindowTitle("Trade Calculator - Selling");
    aggs = []
    errored = True
    index = 0
    latestDate = datetime.datetime.now()
    notConfirmed = True
    stockToSell = "AAPL"

    while (notConfirmed):
        stockToSell = input("Enter the code for the stock you want to buy: ")
        if (stockToSell != ""):
            confirmationDecision = input("Are you sure you want to buy " + stockToSell + " stock? (Y/N) ")
            if (confirmationDecision == "Y"):
                notConfirmed = False

    ## Do a for each loop where we do a try catch around this for each loop, increasing the number of days that we are taking away from now until the for each succeeds
    while (errored):
        if index != 0:
            latestDate = datetime.datetime.now() - datetime.timedelta(days=index)
        try:
            print(latestDate.strftime("%Y-%m-%d"))
            for a in CLIENT.list_aggs(ticker=stockToSell, multiplier=10, timespan="minute", from_=latestDate.strftime("%Y-%m-%d"), to=latestDate.strftime("%Y-%m-%d"), limit=5000):
                print(a)
                print("Time: " + datetime.datetime.fromtimestamp(a.timestamp/1000).strftime("%d/%m/%Y %H:%M:%S"))
                aggs.append(a)
            errored = False
        except:
            errored = True
            index += 1
    print("Last Price: " + str(aggs[-1].high) + " - " + str(aggs[-1].low) + " GBP at " + datetime.datetime.fromtimestamp(aggs[-1].timestamp/1000).strftime("%d/%m/%Y %H:%M:%S"));
    difference = aggs[-1].high - aggs[-1].low
    buyValue = round(aggs[-1].low + (difference / 2), 2)
    confirmBuy = input("Do you want to buy? (Y/N) ")
    if (confirmBuy == 'Y'):
        typeOfPurchase = input("Would you like to buy using amount in GBP or Units? (AMOUNT/UNITS)").upper();
        if (typeOfPurchase == "AMOUNT"):
            amountToPurchase = input("How much would you like to spend in GBP? ");
            print("Amount to Purchase: " + amountToPurchase);
            print("Buy Value: " + str(round((float(buyValue)), 2)));
            numberOfUnits = float(amountToPurchase) / round((float(buyValue)), 2);
            print("Total of " + str(round(numberOfUnits, 0))  + " Units")
        elif (typeOfPurchase == "UNITS"):
            amountToPurchase = input("How many Units would you like to buy? ");
            numberInPounds = float(amountToPurchase) * round(float(buyValue), 2);
            print("Total of " + str(numberInPounds) + "(GBP) spent");
        else:
            print("Defaulted to Amount: ");
            amountToPurchase = input("How much would you like to spend in GBP? ");
            numberOfUnits = float(amountToPurchase) / round(float(buyValue));
            print("Total of " + str(round(numberOfUnits, 0)) + " Units")
    main()
    

def main():
    #Handle GUI
    menuWindow = QMainWindow();
    menuWindow.setWindowTitle("Trade Calculator");
    topLayout = QHBoxLayout();
    centerLayout = QVBoxLayout();
    
    #GUI Menu title
    title = QLabel('TRADE CALCULATOR');
    title.setFont(QFont("Futura", 80, 15));
    title.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignBottom);
    
    #GUI Menu Buttons
    trendsBtn = QPushButton(text='Trends');
    trendsBtn.setFont(QFont("Futura", 25, 15));
    trendsBtn.setFixedSize(500, 80);
    sellingBtn = QPushButton(text='Sell');
    sellingBtn.setFont(QFont("Futura", 25, 15));
    sellingBtn.setFixedSize(500, 80);
    buyingBtn = QPushButton(text='Buy');
    buyingBtn .setFont(QFont("Futura", 25, 15));
    buyingBtn.setFixedSize(500, 80);
    exitBtn = QPushButton(text='Exit');
    exitBtn.setFont(QFont("Futura", 10, 5));
    exitBtn.setFixedSize(100, 50);
    
    #Add buttons and title to layouts/window
    topLayout.addWidget(title);
    topLayout.addWidget(exitBtn);
    centerLayout.addWidget(trendsBtn);
    centerLayout.addWidget(sellingBtn);
    centerLayout.addWidget(buyingBtn);
    topLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter);
    centerLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter);
    topWidget = QWidget();
    topWidget.setLayout(topLayout);
    menuWindow.setMenuWidget(topWidget);
    centerWidget = QWidget();
    centerWidget.setLayout(centerLayout);
    menuWindow.setCentralWidget(centerWidget)
    menuWindow.resize(1000, 500);
    
    #Button click functions
    def trendsBtnClicked():
        print("Trends Clicked");
        menuWindow.close();
        confirmDates();
        
    def sellingBtnClicked():
        print("Selling Clicked");
        menuWindow.close();
        selling();
        
    def buyingBtnClicked():
        print("Buying Clicked");
        menuWindow.close();
        buying();
        
    def exitBtnClicked():
        print("Exit Clicked");
        APP.quit();
        exit();
        
    
    #Calls for when buttons are clicked
    trendsBtn.clicked.connect(trendsBtnClicked);
    sellingBtn.clicked.connect(sellingBtnClicked);
    buyingBtn.clicked.connect(buyingBtnClicked);
    exitBtn.clicked.connect(exitBtnClicked);
    
    #Execute application
    menuWindow.show();
    APP.exec();
    
    #Command line Interface
    # print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    # print("|-------------------------------------------------  TRADE CALCULATOR  -------------------------------------------------|")
    # print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n\n")
    # print("1: Show Trends")
    # print("2: Selling")
    # print("3: Buying")
    # print("4: Exit")
    # choice = input("\nEnter the number option depending on what action you want to carry out: ")
    # match choice:
    #     case "1":
    #         confirmDates()
    #     case "2":
    #         selling()
    #     case "3":
    #         buying()
    #     case "4":
    #         exit()

main()
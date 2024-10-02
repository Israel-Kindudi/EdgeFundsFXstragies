import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from countries import unique_countries

# List of major forex countries we are interested in
countries = unique_countries #["united-states", "euro-area", "japan", "united-kingdom", "australia", "canada", "switzerland"]

# Base URL for TradingEconomics
base_url = "https://tradingeconomics.com/{country}/indicators"

# Set headers to simulate a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.google.com/',
    'DNT': '1',  # Do Not Track Request Header
}
def fetch_data():
    # List to store all country data
    all_data = []

    # Loop through each country
    for country in countries:
        # Dynamically build the URL for each country
        url = base_url.format(country=country)
        
        # Make a GET request to the page with headers
        response = requests.get(url, headers=headers)
        
        # Pause between requests to avoid overloading the server
        time.sleep(2)
        
        # Check if the request was successful
        if response.status_code == 200:
            print(f"Fetching data for {country}...")
            
            # Parse the page content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all table rows in the indicators table
            rows = soup.find_all('tr')
            
            # Extract the relevant data (indicator, last, previous, highest, lowest, date)
            for row in rows:
                cols = row.find_all('td')
                if len(cols) > 1:  # Skip rows without data
                    indicator = cols[0].text.strip()
                    last = cols[1].text.strip()
                    previous = cols[2].text.strip() if len(cols) > 2 else ''
                    highest = cols[3].text.strip() if len(cols) > 3 else ''
                    lowest = cols[4].text.strip() if len(cols) > 4 else ''
                    date = cols[5].text.strip() if len(cols) > 5 else ''
                    
                    # Append the data to the list
                    all_data.append([country, indicator, last, previous, highest, lowest, date])
        else:
            print(f"Failed to retrieve data for {country}")

    # Create a DataFrame from the collected data
    df = pd.DataFrame(all_data, columns=["Country", "Indicator", "Last", "Previous", "Highest", "Lowest", "Date"])

    # Save the data to a CSV file
    df.to_csv('forex_indicators.csv', index=False)

    print("Data scraping complete. Data saved to 'forex_indicators.csv'.")
def financial_differential():
    country1 = input("enter the first country")
    country2 = input("enter counrty 2")
    # Read the CSV data
    df = pd.read_csv('forex_indicators.csv')

    def calculate_differential(df, country1, country2, indicator):
        """
        Compare the 'Last' values of a given indicator between two countries,
        print the two countries' values, and assess whether it is a bullish or bearish signal.
        
        Args:
        - df: DataFrame containing the data
        - country1: The first country for comparison
        - country2: The second country for comparison
        - indicator: The financial indicator to compare
        
        Returns:
        - Tuple (differential value, bullish/bearish signal)
        """
        
        # Get the 'Last' values for the given indicator
        c1_value = df[(df['Country'] == country1) & (df['Indicator'] == indicator)]['Last'].values[0]
        c2_value = df[(df['Country'] == country2) & (df['Indicator'] == indicator)]['Last'].values[0]
        
        # Calculate the differential
        differential = float(c1_value) - float(c2_value)
        
        # Print the values for both countries
        print(f"{indicator} for {country1}: {c1_value}, {indicator} for {country2}: {c2_value}")
        
        # Initialize signal variable (to prevent UnboundLocalError)
        signal = None
        
        # Determine if it's a bullish or bearish signal based on the indicator type
        if indicator in ['GDP Growth Rate', 'Interest Rate', 'Balance of Trade','Unemployment Rate']:  # Higher is better
            if differential > 0:
                signal = f"Bullish signal for {country1}."
            else:
                signal = f"Bearish signal for {country1}."
        elif indicator == 'Inflation Rate':  # Ideal inflation is around 2%
            ideal_inflation = 2.0
            
            # Calculate the absolute difference from the ideal inflation rate
            c1_inflation_diff = abs(float(c1_value) - ideal_inflation)
            c2_inflation_diff = abs(float(c2_value) - ideal_inflation)
            
            # Compare which country is closer to the ideal inflation
            if c1_inflation_diff < c2_inflation_diff:
                signal = f"Bullish signal for {country1}."
            else:
                signal = f"Bearish signal for {country1}."
        elif indicator == 'Unemployment Rate':  # Lower is better
            if differential > 0:  # If country1 has a higher unemployment rate, it's bearish
                signal = f"Bearish signal for {country1}."
            else:  # If country1 has a lower unemployment rate, it's bullish
                signal = f"Bullish signal for {country1}."

        
        # Catch any unhandled indicators (just in case)
        if signal is None:
            signal = "Unknown indicator type. Unable to determine signal."
        
        # Return the differential and the signal
        return differential, signal
            
   # Indicators to compare (including Trade Balance and Unemployment Rate)
    indicators = ['GDP Growth Rate', 'Interest Rate', 'Inflation Rate', 'Balance of Trade','Unemployment Rate']

    # Compare the financial differentials for all indicators
    for indicator in indicators:
        diff, signal = calculate_differential(df, country1, country2, indicator)
        print(f"{indicator} Differential ({country1} vs {country2}): {diff:.2f} -> {signal}\n")
def listen_for_input():
    choice = input("Enter your choice: ")
    return choice
while True:
    print("fetch data : 1")
    print("financial differentials : 2")
    print("quit : q")
    
    # Collect the user's choice once
    choice = listen_for_input()
    
    # Check the input once, based on the collected choice
    if choice == "1":
        fetch_data()
    elif choice == "2":
        financial_differential()
    elif choice == "q":
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.")

# Original data (including continents, countries, and some duplicates)
data = [
    "United States", "Euro Area", "China", "Japan", "Germany", "United Kingdom", "France", "India", "Italy", 
    "Brazil", "Canada", "South Korea", "Russia", "Spain", "Australia", "Mexico", "Indonesia", "Turkey", 
    "Netherlands", "Switzerland", "Saudi Arabia", "Argentina", "South Africa", "Singapore", "America", 
    "Antigua and Barbuda", "Argentina", "Aruba", "Bahamas", "Barbados", "Belize", "Bermuda", "Bolivia", 
    "Brazil", "Canada", "Cayman Islands", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominica", 
    "Dominican Republic", "Ecuador", "El Salvador", "Grenada", "Guatemala", "Guyana", "Haiti", "Honduras", 
    "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "Suriname", 
    "Trinidad and Tobago", "United States", "Uruguay", "Venezuela", "Europe", "Albania", "Andorra", 
    "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus", 
    "Czech Republic", "Denmark", "Estonia", "Euro area", "Faroe Islands", "Finland", "France", 
    "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Isle of Man", "Italy", "Kosovo", "Latvia", 
    "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", 
    "North Macedonia", "Norway", "Poland", "Portugal", "Romania", "Russia", "Serbia", "Slovakia", 
    "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine", "United Kingdom", "Africa", 
    "Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Cape Verde", 
    "Central African Republic", "Chad", "Comoros", "Congo", "Djibouti", "Egypt", "Equatorial Guinea", 
    "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea Bissau", "Ivory Coast", 
    "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", 
    "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Republic of the Congo", "Rwanda", 
    "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", 
    "South Sudan", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe", 
    "Asia", "Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Brunei", 
    "Cambodia", "China", "East Timor", "Georgia", "Hong Kong", "India", "Indonesia", "Iran", "Iraq", 
    "Israel", "Japan", "Jordan", "Kazakhstan", "Kuwait", "Kyrgyzstan", "Laos", "Lebanon", "Macao", 
    "Malaysia", "Maldives", "Mongolia", "Myanmar", "Nepal", "North Korea", "Oman", "Palestine", 
    "Pakistan", "Philippines", "Qatar", "Saudi Arabia", "Singapore", "South Korea", "Sri Lanka", "Syria", 
    "Taiwan", "Tajikistan", "Thailand", "Turkmenistan", "United Arab Emirates", "Uzbekistan", "Vietnam", 
    "Yemen", "Australia", "Australia", "Fiji", "Kiribati", "New Caledonia", "New Zealand", "Papua New Guinea", 
    "Samoa", "Solomon Islands", "Tonga", "Vanuatu"
]

# List of continent names to remove, except "Australia"
continents = ["Africa", "Asia", "Europe", "Euro Area", "America", "Euro area"]

# Remove continents and duplicates, but keep "Australia" as a country
unique_countries = list(set([country for country in data if country not in continents]))

# Sort the list alphabetically
unique_countries.sort()

# Resulting list of unique countries
print(unique_countries)

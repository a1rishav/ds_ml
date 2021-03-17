# EDA

## Uses of visualization

### Numerical values
- Histogram or seaborn's distplot
- Box plot for outliers
- Scatter plot to identify trend bw numerical variables
- Scatter plot to identify natural clusters in data
- Correlation heatmap to for relation bw all features
- All correlations, use for smaller no. of columns --> pair plot
- Line chart for trends, x axis will have a continues variable

### Categorical values
- Bar chart
- Pie chart - df['Column'].value_counts().plot.pie()

## Data sourcing
- Data sourcing
- Data cleaning
- Univariate analysis
- Bivariate analysis
- Derived metrics

### Examples

#### Private Data
- HR analytics
    - which people would leave company
    - which people are right for hiring
- Telecom
    - which people would leave network
    - create right packs
- Banks
    - Identifying loan and loan amount
    - Loan packages
- Retail
    - Product stocking
    - What products sell together
    - If a newly introduced product is not badly affecting other products
- Media
    - Advertising
    - Data journalism
    
#### Public Data

- References
    - https://github.com/awesomedata/awesome-public-datasets
    - https://data.gov.in/
    - https://data.gov/
    - https://data.gov.uk
    - https://censusindia.gov.in/ --> very powerful
    - https://github.com/datameet
    
## Data Cleaning
- Fixing rows and columns
  - Fixing rows
      - Delete incorrect rows --> unnecessary header rows, footer rows
      - Delete summary rows --> Total, subtotal rows
      - Delete extra rows --> column number indicator rows, blannk rows
  - Fixing columns
      - Merge columns for creating unique identifiers if needed: E.g. Merge State, City into Full address
      - Split columns for more data: Split address to get State and City to analyse each separately
      - Add column names: Add column names if missing
      - Rename columns consistently: Abbreviations, encoded columns
      - Delete columns: Delete unnecessary columns
      - Align misaligned columns: Dataset may have shifted columns
- Fix missing values
  - Set values as missing values: Identify values that indicate missing data, and yet are not recognised by the software as such, e.g treat blank strings, "NA", "XX", "999", etc. as missing.
  - Adding is good, exaggerating is bad: **You should try to get information from reliable external sources as much as possible, but if you can’t, then it is better to keep missing values as such rather than exaggerating the existing rows/columns.**
  - Delete rows, columns: Rows could be deleted if the number of missing values are significant in number, as this would not impact the analysis. Columns could be removed if the missing values are quite significant in number.
  - Fill partial missing values using business judgement: Missing time zone, century, etc. These values are easily identifiable.
  - https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html
- Standarise values
  - Numeric
    - Standardise units: Ensure all observations under a variable have a common and consistent unit, e.g. convert lbs to kgs, miles/hr to km/hr, etc.
    - Scale values if required:  Make sure the observations under a variable have a common scale
    - Standardise precision for better presentation of data, e.g. 4.5312341 kgs to 4.53 kgs.
    - Remove outliers: Remove high and low values that would disproportionately affect the results of your analysis.
  - Categorical
    - Standardise units: Ensure all observations under a variable have a common and consistent unit, e.g. convert lbs to kgs, miles/hr to km/hr, etc.
    - Scale values if required:  Make sure the observations under a variable have a common scale
    - Standardise precision for better presentation of data, e.g. 4.5312341 kgs to 4.53 kgs.
    - Remove outliers: Remove high and low values that would disproportionately affect the results of your analysis.
- Fix invalid values
  - Encode unicode properly: In case the data is being read as junk characters, try to change encoding, E.g. CP1252 instead of UTF-8.
  - Convert incorrect data types: Correct the incorrect data types to the correct data types for ease of analysis. E.g. if numeric values are stored as strings, it would not be possible to calculate metrics such as mean, median, etc. Some of the common data type corrections are — string to number: "12,300" to “12300”; string to date: "2013-Aug" to “2013/08”; number to string: “PIN Code 110001” to "110001"; etc.
  - Correct values that go beyond range: If some of the values are beyond logical range, e.g. temperature less than -273° C (0° K), you would need to correct them as required. A close look would help you check if there is scope for correction, or if the value needs to be removed.
  - Correct values not in the list: Remove values that don’t belong to a list. E.g. In a data set containing blood groups of individuals, strings “E” or “F” are invalid values and can be removed.
  - Correct wrong structure: Values that don’t follow a defined structure can be removed. E.g. In a data set containing pin codes of Indian cities, a pin code of 12 digits would be an invalid value and needs to be removed. Similarly, a phone number of 12 digits would be an invalid value.
  - Validate internal rules: If there are internal rules such as a date of a product’s delivery must definitely be after the date of the order, they should be correct and consistent.
- Filtering data 
  - Deduplicate data: Remove identical rows, remove rows where some columns are identical
  - Filter rows: Filter by segment, filter by date period to get only the rows relevant to the analysis
  - Filter columns: Pick columns relevant to the analysis
  - Aggregate data: Group by required keys, aggregate the rest

## Univariate Analysis

### Extract metadata
- Overview
  - Description of data, what is the data about
  - Source
  - Format, can be files, can be database
  - Count of rows
  - Sampling method if available,eg : all customers who bought more items bw 2001 and 2020
- Column Info
  - Name
  - type
  - description
  - missing values count
  - unique items or unique items count
  - column type : ordered categorical, unordered categorical, numerical
- Analysing unordered categorical variable
  - Column current_working_location has name of states
    - find value_counts
  - Barchart showing frequency count
  - Add rank (sorting and assigning a number) and plotting rank vs frequency plot using
    - If the range of values is too high, use log scale, a straight line in log scale is **powerlaw distribution**  
- Analysing ordered categorical variable
  - variables 
    - low, medium, high
    - electricity units consumption
    - marks of a student
  - plot a histogram
    - spike in between are anamolies
  - Analysing quantative variables
    - median is a better measure of group's representativeness
    - 

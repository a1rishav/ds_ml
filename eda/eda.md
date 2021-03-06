# EDA

## Purpose
- what independent variables are affecting target variable
- among indepeendent variables which ones are co-orelated

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

## Relationship
  - identify categorical and numerical
  - numerical and numerical --> categorical
  - numerical and categorical --> barplot, boxplot
  - categorical and categorical

## Univariate, Segmented Univariate, Bivariate Analysis

- Extract metadata
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
    - median is a better measure of group's representativeness as mean will be affected by outlier
    - mode is used in categorical data to get the most frequent one
    - 25th, 75th percentile, interquartile values are much better than standard deviation since standard deviation is affected by outliers
    - to know the spread, use 75th - 25th percentile
    - practical use case : on a sachine's cricket score dataset, group sachin's score in ranges 1-10, 11-20, ..., sachin scored max bw 1 to 10
  - Segmented Univariate Analysis
    -  any categorical data can serve as the basis of segmentation, but you’ll need to use your best business judgement to choose the right data to analyse
    - Process
      - Take raw data
      - Group by dimensions
      - Summarise using a relevant metric such as mean, median, etc.
      - Compare the aggregated metric across groups/categories
      - “Don’t blindly believe in the averages of the buckets — you need to observe the distribution of each bucket closely and ask yourself if the difference in means is significant enough to draw a conclusion. If the difference in means is small, you may not be able to draw inferences. In such cases, a technique called hypothesis testing is used to ascertain whether the difference in means is significant or due to randomness
  - Bivariate Analysis on Continuous Variables
      - correlation is a number between -1 and 1 which quantifies the extent to which two variables ‘correlate’ with each other.
        - If one increases as the other increases, the correlation is positive
        - If one decreases as the other increases, the correlation is negative
        - If one stays constant as the other varies, the correlation is zero
      - Correlation practical use cases
        - Resturants can group items andprepare combos based on coorealtion of sales
        - Resturant sales data, it was found that 1L bottle sales was negatively coorelated with sales of other items, so size was reduced to 500 ml
      - bivariate analysis is basically grouping on 2 categorical columns and aggregating a numeric column
  - Derived Metrics
    Steven’s typology classifies variables into four types — nominal, ordinal, interval and ratio
    - Type-driven metrics
      - Nominal - Categorical variables, where the categories differ only by their names; there is no order among categories, e.g. colour (red, blue, green)
      - Ordinal - Categories follow a certain order, but the mathematical difference between categories is not meaningful, e.g. education level (primary school, high school, college)
      - Interval - Categories follow a certain order, and the mathematical difference between categories is meaningful but division or multiplication is not, e.g. temperature in degrees celsius, dates (the difference between two dates is the number of days between them, but 25th May / 5th June is meaningless) 
      - Ratio - Apart from the mathematical difference, the ratio (division/multiplication) is possible, e.g. sales in dollars ($100 is twice $50), marks of students (50 is half of 100),
      
      - Examples :
        - review : sentiment, length of review
        - date : month, day, year, day of week
        - location : district, state, country, east, west, timezone, urban, rural 
      
      - Numerical : mean, median, percntile of a column can be a new column
    - Business-driven metrics : requires domain knowledge
      - Examples
        - Student marks : pass / fail, CGPA cutoff
        - Banking : number of checques in a month, card sold == target, 
    - Data-driven metrics
      - data-driven metrics can be created based on the variables present in the existing data set
      - if you have two variables in your data set such as "weight" and "height" which shows a high correlation. So, instead of analysing "weight" and "height" variables separately, you can think of deriving a new metric "Body Mass Index (BMI)
  
## Workflow
  - Summary stats
    - df.describe 
    - df.describe include 0 for categorical
  - handling missing value
    - find percentage of missing values of each column
    - understand from bussiness why a column is missing
    - impute if necessary
    - if target is missing ignore the rows 
  - derive varibales --> how can I make use of the information
  - any anomalies check with business
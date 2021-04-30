## Seaborn

### About
- visulaization library
- built on top of matplotlib and closely integrated with pandas

### Functionalities
- analysing univariate and bivariate analysis
- automatic estimation and plotting of linear regression models
- better views by changing style and colour
- we can create seaborn plots and also use functions of matplotlib like adding a titile

### Visualizations
- distplot
    - can be used instead of histogram
    - also provides probability density curve
    - https://seaborn.pydata.org/generated/seaborn.distplot.html
    ```buildoutcfg
    ax = sns.distplot(x)
    ```
- countplot
    - histogram for catergorical values
    - https://seaborn.pydata.org/generated/seaborn.countplot.html
    ```buildoutcfg
     sns.countplot(x="class", data=titanic)
     sns.countplot(x='purpose', hue='loan_status', data=df)
    ```
  
- jointplot
  - relationship bw 2 numerical features
  - scatterplot with distribution for numerical features
  - https://seaborn.pydata.org/generated/seaborn.jointplot.html
  ```buildoutcfg
   sns.jointplot(df.Size, df.Rating)
  ```
- pairplot
  - Pair wise scatter plot bw all features, so 4 features there will be 4 * 4 plots
  - should be used for less numerical features
  - ```buildoutcfg
     sns.pairplot(df[['Reviews', 'Size', 'Price', 'Rating']])
    ```
  - https://seaborn.pydata.org/generated/seaborn.pairplot.html

- barplot
  - Can be used to show relationship between categorical and numerical features
  - https://seaborn.pydata.org/generated/seaborn.barplot.html?highlight=barplot#seaborn.barplot  
  - ```
    sns.barplot(data=df, x='Content Rating', y='Rating')
    ```

- boxplot
  - Can be used to show relationship between categorical and numerical features
  - identify outliers
  - https://seaborn.pydata.org/generated/seaborn.boxplot.html
  - ```
     sns.boxplot(x=df['Content Rating'], y=df.Rating)
     sns.boxplot(y='loan_amnt', x='loan_status', data=df)
    ```
- heatmap
  - visualize coorelation
  - ```
    sns.heatmap(data=df.corr(), cmap = "Greens", annot=True)
    ```
  - https://seaborn.pydata.org/generated/seaborn.heatmap.html?highlight=heatmap#seaborn.heatmap

- style
    - available styles --> https://seaborn.pydata.org/generated/seaborn.countplot.html
    ```
        plt.style.available
        plt.style.use("ggplot")  
    ```
  
- Reference : https://towardsdatascience.com/a-complete-guide-to-plotting-categorical-variables-with-seaborn-bfe54db66bec
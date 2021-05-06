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
  - when target variable is categorical and we want to see it's relationship with categorical variable
    ```buildoutcfg
    feature = 'grade'
    
    def view_relationship_bw_categorical_variables(plot_df, feature, sort_by="feature"):
        # get counts of defaults and total
    
        filtered_df = plot_df.loc[plot_df.loan_status == 'Charged Off'][[feature, "loan_status"]].copy()
    
        filtered_df = filtered_df[feature].value_counts().to_frame()
        filtered_df['total_count'] = df[feature].value_counts()
        filtered_df.rename({feature: 'default_count'}, axis=1, inplace=True)
    
        # calulate percentage of deaulters in each bin
    
    
        filtered_df['default_percentage'] = filtered_df.apply(lambda row :
                                                              round(row['default_count'] /
                                                                    row['total_count'] * 100, 2), axis=1)
        filtered_df[feature] = filtered_df.index
    
        # # plot bins and default percentage
        if sort_by == 'feature':
            filtered_df = filtered_df.sort_values(by=feature)
        else:
            filtered_df = filtered_df.sort_values(by='default_percentage')
        sns.barplot(data=filtered_df, x=feature, y='default_percentage')
        return filtered_df
        
    view_relationship_bw_categorical_variables(df, feature)
    ```
  - when target variable is categorical and we want to see it's relationship with numerical variable
    ```buildoutcfg

    def view_categorical_and_numerical_relationship(plot_df, feature, bins):
        feature_column = getattr(plot_df, feature)
        plot_df['{}_bins'.format(feature)] = pd.cut(feature_column, bins=bins)
    
        # create another binned dti dataframe for loan_status == 'Charged Off'
    
        filtered_df = plot_df.loc[plot_df.loan_status == 'Charged Off'].copy()
        binned_col_name = '{}_bins'.format(feature)
        filtered_df[binned_col_name] = pd.cut(filtered_df[feature], bins=bins)
    
        # get count of defaulters and non defaulters in each bin
    
        count_df = plot_df[binned_col_name].value_counts().to_frame()
        filtered_df = filtered_df[binned_col_name].value_counts().to_frame()
    
        # calulate percentage of deaulters in each bin
    
        filtered_df['total_count'] = getattr(count_df, binned_col_name)
        filtered_df.rename({binned_col_name: 'default_count'}, axis=1, inplace=True)
    
        filtered_df['default_percentage'] = filtered_df.apply(lambda row :
                                                              round(row['default_count'] /
                                                                    row['total_count'] * 100, 2), axis=1)
        filtered_df[feature] = filtered_df.index
        filtered_df[feature] = filtered_df[feature].apply(lambda value : str(value).replace("]", "").replace("(", "").replace(",", " -"))
        filtered_df.reset_index(drop=True, inplace=True)
    
    #     plot bins and default percentage
        sns.barplot(data=filtered_df, x=feature, y='default_percentage')
        return filtered_df
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
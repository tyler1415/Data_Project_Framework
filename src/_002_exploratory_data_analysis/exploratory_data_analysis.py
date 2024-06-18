import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class exploratory_data_analysis:
    def __init__(self, df):

        self.df = df

    def summary_results(self):
        """Print summary statistics of the DataFrame."""
        print("Summary Statistics:")
        print(self.df.describe(include='all'))

    def missing_values(self):
        """Print the count of missing values in each column."""
        print("Missing Values:")
        print(self.df.isnull().sum())

    def plot_distributions(self):
        """Plot the distribution of each numeric column."""
        numeric_columns = self.df.select_dtypes(include=['number']).columns
        self.df[numeric_columns].hist(bins=15, figsize=(15, 10))
        plt.suptitle('Distribution of Numeric Columns')
        plt.show()

    def correlation_matrix(self):
        """Print and plot the correlation matrix of numeric columns in the DataFrame."""
        numeric_df = self.df.select_dtypes(include=['number'])
        corr_matrix = numeric_df.corr()
        print("Correlation Matrix:")
        print(corr_matrix)
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
        plt.title('Correlation Matrix')
        plt.show()
        
    def value_counts(self, column):
        """Print the value counts of a specific column."""
        if column in self.df.columns:
            print(f"Value Counts for {column}:")
            print(self.df[column].value_counts())
        else:
            print(f"Column {column} does not exist in the DataFrame.")

    def pairplot(self):
        """Plot pairwise relationships in the dataset."""
        sns.pairplot(self.df)
        plt.show()

    def plot_missing_values_heatmap(self):
        """Plot a heatmap of missing values."""
        plt.figure(figsize=(10, 6))
        sns.heatmap(self.df.isnull(), cbar=False, cmap='viridis')
        plt.title('Heatmap of Missing Values')
        plt.show()
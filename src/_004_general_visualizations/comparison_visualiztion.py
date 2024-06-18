import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class ComparisonVisualization:
    def __init__(self, df):
        self.df = df

    def box_plot(self):
        # Example: Box plot comparison of numeric columns
        numeric_columns = self.df.select_dtypes(include=['number']).columns
        for col in numeric_columns:
            plt.figure(figsize=(8, 6))
            sns.boxplot(x=self.df[col])
            plt.title(f'Comparison of {col}')
            plt.xlabel(col)
            plt.tight_layout()
            plt.show()

    def bar_plot(self, categorical_column):
        """Plot bar plots of means of numeric columns across different categories."""
        numeric_columns = self.df.select_dtypes(include=['number']).columns
        for num_col in numeric_columns:
            plt.figure(figsize=(10, 6))
            sns.barplot(x=categorical_column, y=num_col, data=self.df, ci=None)
            plt.title(f'Mean {num_col} by {categorical_column}')
            plt.xlabel(categorical_column)
            plt.ylabel(f'Mean {num_col}')
            plt.tight_layout()
            plt.show()

    def line_plot(self, x_column, y_column):
        """Plot a line graph of numeric variable over a continuous variable."""
        plt.figure(figsize=(10, 6))
        sns.lineplot(x=x_column, y=y_column, data=self.df)
        plt.title(f'Line Graph of {y_column} over {x_column}')
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.tight_layout()
        plt.show()
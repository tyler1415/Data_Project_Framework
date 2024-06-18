import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DistributionVisualization:
    def __init__(self, df):
        self.df = df

    def histogram(self):
        # Example: Histograms for distribution of numeric columns
        numeric_columns = self.df.select_dtypes(include=['number']).columns
        for col in numeric_columns:
            plt.figure(figsize=(8, 6))
            sns.histplot(self.df[col], kde=True)
            plt.title(f'Distribution of {col}')
            plt.xlabel(col)
            plt.ylabel('Frequency')
            plt.tight_layout()
            plt.show()
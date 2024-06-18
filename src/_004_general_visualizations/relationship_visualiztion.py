import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class RelationshipVisualization:
    def __init__(self, df):
        self.df = df

    def pair_plot(self):
        # Example: Pairplot for relationships between variables
        plt.figure(figsize=(12, 10))
        sns.pairplot(self.df)
        plt.tight_layout()
        plt.show()

    def scatter_plot_matrix(self):
        """Plot a scatter plot matrix of numeric columns."""
        numeric_columns = self.df.select_dtypes(include=['number']).columns
        sns.pairplot(self.df[numeric_columns])
        plt.title('Scatter Plot Matrix')
        plt.tight_layout()
        plt.show()
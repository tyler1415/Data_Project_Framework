import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class CompositionVisualization:
    def __init__(self, df):
        self.df = df

    def pie_chart(self):
        # Example: Pie chart for composition of categorical data
        categorical_columns = self.df.select_dtypes(include=['object', 'category']).columns
        for col in categorical_columns:
            plt.figure(figsize=(8, 6))
            self.df[col].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
            plt.title(f'Composition of {col}')
            plt.ylabel('')
            plt.tight_layout()
            plt.show()


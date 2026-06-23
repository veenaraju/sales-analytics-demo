import pandas as pd


def load_data(file_path):
    """Load sales data from CSV file."""
    return pd.read_csv(file_path)


def total_sales(df):
    """Calculate total sales amount (quantity * price)."""
    df['total'] = df['quantity'] * df['price']
    return df['total'].sum()


def average_sales(df):
    """Calculate average sales amount per transaction."""
    df['total'] = df['quantity'] * df['price']
    return df['total'].mean()


def sales_by_category(df):
    """Calculate total sales grouped by category."""
    df['total'] = df['quantity'] * df['price']
    return df.groupby('category')['total'].sum().to_dict()


if __name__ == "__main__":
    # Example usage
    df = load_data(r'D:\Python_Projects\windsurf\SalesAnalyticsDemo\data\sales.csv')
    print(f"Total Sales modified: ${total_sales(df):.2f}")
    print(f"Average Sales modified twice: ${average_sales(df):.2f}")
    print(f"Sales by Category modified twice: {sales_by_category(df)}")

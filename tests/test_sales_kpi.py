import pytest
import pandas as pd
import sys
import os

# Add the src directory to the path so we can import the module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from sales_kpi import total_sales, average_sales, sales_by_category


@pytest.fixture
def sample_df():
    """Create a sample DataFrame for testing."""
    data = {
        'date': ['2024-01-01', '2024-01-02', '2024-01-03'],
        'product': ['Laptop', 'Mouse', 'Desk Chair'],
        'category': ['Electronics', 'Electronics', 'Furniture'],
        'quantity': [2, 5, 3],
        'price': [1200, 25, 150]
    }
    return pd.DataFrame(data)


def test_total_sales(sample_df):
    """Test total_sales function."""
    result = total_sales(sample_df)
    expected = (2 * 1200) + (5 * 25) + (3 * 150)  # 2400 + 125 + 450 = 2975
    assert result == expected


def test_average_sales(sample_df):
    """Test average_sales function."""
    result = average_sales(sample_df)
    expected = ((2 * 1200) + (5 * 25) + (3 * 150)) / 3  # 2975 / 3 = 991.67
    assert round(result, 2) == round(expected, 2)


def test_sales_by_category(sample_df):
    """Test sales_by_category function."""
    result = sales_by_category(sample_df)
    expected = {
        'Electronics': (2 * 1200) + (5 * 25),  # 2400 + 125 = 2525
        'Furniture': (3 * 150)  # 450
    }
    assert result == expected


def test_sales_by_category_types(sample_df):
    """Test that sales_by_category returns a dictionary."""
    result = sales_by_category(sample_df)
    assert isinstance(result, dict)
    assert len(result) == 2

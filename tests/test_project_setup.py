"""Tests for initial project setup and sample CSV datasets.

These tests verify package importability, existence of sample data files,
and correctness of CSV column headers for DataPulse Day 1.
"""

import csv
from pathlib import Path


# Helper function to read the header row from a CSV file.
def get_csv_headers(file_path: Path) -> list[str]:
    """Read and return the column headers of a CSV file.

    Parameters:
        file_path (Path): Path to the target CSV file.

    Returns:
        list[str]: A list of header column names from the first row.
    """
    with file_path.open(mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        return next(reader)


# Tests that the datapulse package can be imported successfully.
def test_datapulse_package_import() -> None:
    """Verify that the datapulse package can be imported and has a valid version."""
    import datapulse

    assert hasattr(datapulse, "__version__")
    assert isinstance(datapulse.__version__, str)
    assert len(datapulse.__version__) > 0


# Tests that all required sample CSV files exist in the repository.
def test_sample_csv_files_exist() -> None:
    """Verify that sample files for sales, validation, and inventory exist on disk."""
    base_dir = Path(__file__).resolve().parent.parent / "sample_data"

    sales_file = base_dir / "sales" / "sales_sample.csv"
    validation_file = base_dir / "validation" / "validation_sample.csv"
    inventory_file = base_dir / "inventory" / "inventory_sample.csv"

    assert sales_file.is_file(), f"Expected file not found: {sales_file}"
    assert validation_file.is_file(), f"Expected file not found: {validation_file}"
    assert inventory_file.is_file(), f"Expected file not found: {inventory_file}"


# Tests that the sales sample CSV file has the required columns.
def test_sales_csv_columns() -> None:
    """Verify that sales_sample.csv contains all expected column headers."""
    base_dir = Path(__file__).resolve().parent.parent / "sample_data"
    sales_file = base_dir / "sales" / "sales_sample.csv"

    expected_columns = [
        "order_id",
        "order_date",
        "product_id",
        "product_name",
        "quantity",
        "unit_price",
    ]

    actual_columns = get_csv_headers(sales_file)
    assert actual_columns == expected_columns


# Tests that the validation sample CSV file has the required columns.
def test_validation_csv_columns() -> None:
    """Verify that validation_sample.csv contains all expected column headers."""
    base_dir = Path(__file__).resolve().parent.parent / "sample_data"
    validation_file = base_dir / "validation" / "validation_sample.csv"

    expected_columns = [
        "order_id",
        "product_name",
        "quantity",
        "unit_price",
    ]

    actual_columns = get_csv_headers(validation_file)
    assert actual_columns == expected_columns


# Tests that the inventory sample CSV file has the required columns.
def test_inventory_csv_columns() -> None:
    """Verify that inventory_sample.csv contains all expected column headers."""
    base_dir = Path(__file__).resolve().parent.parent / "sample_data"
    inventory_file = base_dir / "inventory" / "inventory_sample.csv"

    expected_columns = [
        "product_id",
        "product_name",
        "stock_quantity",
        "reorder_level",
    ]

    actual_columns = get_csv_headers(inventory_file)
    assert actual_columns == expected_columns

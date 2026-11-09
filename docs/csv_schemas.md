# CSV Schema Definitions

This document defines the schema specifications and sample data rules for CSV datasets processed by **DataPulse – Serverless Data Processing Platform**.

---

## 1. Sales Analysis Schema

- **Target File:** `sample_data/sales/sales_sample.csv`
- **Purpose:** Ingest daily or transactional sales records to compute business metrics such as total orders, total units sold, gross revenue, and distinct products sold.

### Columns Specification

| Column | Data Type | Constraint | Description |
|---|---|---|---|
| `order_id` | String | Required, Unique | Unique identifier for the customer order. |
| `order_date` | Date | Required (YYYY-MM-DD) | Date when the order was placed. |
| `product_id` | String | Required | Unique product SKU or identifier. |
| `product_name` | String | Required | Human-readable name of the product. |
| `quantity` | Integer | Required, Positive (`> 0`) | Number of units purchased in the order. |
| `unit_price` | Decimal | Required, Non-negative (`>= 0.0`) | Selling price per individual unit. |

### Sample Data Table

| order_id | order_date | product_id | product_name | quantity | unit_price |
|---|---|---|---|---:|---:|
| 1001 | 2026-01-10 | PROD-001 | Laptop | 2 | 150000 |
| 1002 | 2026-01-11 | PROD-002 | Mouse | 5 | 2500 |
| 1003 | 2026-01-12 | PROD-001 | Laptop | 1 | 150000 |
| 1004 | 2026-01-13 | PROD-003 | Keyboard | 3 | 5000 |
| 1005 | 2026-01-14 | PROD-002 | Mouse | 2 | 2500 |

### Expected Sample Calculations

- **Total Orders:** 5
- **Total Units Sold:** 13 (2 + 5 + 1 + 3 + 2)
- **Unique Products:** 3 (`Laptop`, `Mouse`, `Keyboard`)
- **Sample Total Revenue:** 482,500 (calculated as $(2 \times 150000) + (5 \times 2500) + (1 \times 150000) + (3 \times 5000) + (2 \times 2500)$; baseline subtotal across initial 4 orders equals 477,500).

---

## 2. Data Validation Schema

- **Target File:** `sample_data/validation/validation_sample.csv`
- **Purpose:** Test the data validation processor with records that simulate real-world data corruption and edge cases.

### Columns Specification

| Column | Data Type | Constraint | Description |
|---|---|---|---|
| `order_id` | String | Required, Unique | Identifier of the order. |
| `product_name` | String | Required | Name of the product ordered. |
| `quantity` | Integer | Required, Positive (`> 0`) | Quantity ordered. |
| `unit_price` | Decimal | Required, Non-negative (`>= 0.0`) | Unit price. |

### Sample Data Table and Validation Cases

| order_id | product_name | quantity | unit_price | Validation Case | Expected Outcome |
|---|---|---:|---:|---|---|
| `ORD-1001` | Laptop | 1 | 150000 | Baseline valid record | Valid |
| `ORD-1002` | Mouse | *[missing]* | 2500 | Missing quantity field | Invalid (missing value) |
| `ORD-1003` | Keyboard | -2 | 5000 | Negative quantity | Invalid (must be > 0) |
| `ORD-1001` | Monitor | 1 | 45000 | Duplicate order ID (`ORD-1001`) | Invalid (duplicate primary key) |
| `ORD-1005` | Headphones | 3 | -1200 | Negative unit price | Invalid (must be >= 0.0) |

---

## 3. Inventory Analysis Schema

- **Target File:** `sample_data/inventory/inventory_sample.csv`
- **Purpose:** Evaluate inventory levels against predetermined reorder thresholds to identify items that require restocking.

### Columns Specification

| Column | Data Type | Constraint | Description |
|---|---|---|---|
| `product_id` | String | Required, Unique | Unique product identification code. |
| `product_name` | String | Required | Name of the inventory item. |
| `stock_quantity` | Integer | Required, Non-negative (`>= 0`) | Units currently available in warehouse. |
| `reorder_level` | Integer | Required, Non-negative (`>= 0`) | Minimum safety stock before reordering. |

### Sample Data Table

| product_id | product_name | stock_quantity | reorder_level | Status / Restock Required |
|---|---|---:|---:|---|
| `INV-001` | Laptop Stand | 45 | 20 | Healthy (stock >= reorder level) |
| `INV-002` | Mechanical Keyboard | 8 | 15 | **Needs Restock** (stock < reorder level) |
| `INV-003` | Wireless Mouse | 5 | 25 | **Needs Restock** (stock < reorder level) |
| `INV-004` | USB-C Hub | 60 | 30 | Healthy (stock >= reorder level) |
| `INV-005` | HDMI Cable | 12 | 20 | **Needs Restock** (stock < reorder level) |
| `INV-006` | Monitor Arm | 30 | 10 | Healthy (stock >= reorder level) |

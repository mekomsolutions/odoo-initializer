### Model `stock_location`

The `stock_location` subfolder allows to import Price Lists provided as CSV files. See the example below:

| id | name | discount_policy | sequence | item_ids/applied_on | item_ids/base | item_ids/compute_price | item_ids/min_quantity | item_ids/percent_price | item_ids/product_id/id | item_ids/date_start | item_ids/date_end |
| -
| pricelist.X | Summer Discount 2019 | Discount included in the price | 16 | Global | Public Price | Percentage (discount) | 1 | 20 |  | 2019-06-21 | 2019-09-23 |


See the test resources for further examples:
- [odoo_csv/stock_location/stock.location.csv](../odoo_initializer/tests/resources/odoo_csv/stock_location/stock.location.csv)

### Model `units_of_measure`

The `units_of_measure` subfolder allows to import Units of Measure provided as CSV files. See the example below:


id | name | category_id/id | factor | uom_type | rounding
| - | - | - | - | - | - |
product.product_uom_dozen | Dozen(s) | product.product_uom_categ_unit | 0.0833333333333 | Bigger than the reference Unit of Measure | 0.01
product.product_uom_litre | Liter(s) | product.product_uom_categ_vol | 1.0 | Reference Unit of Measure for this category | 0.01

See the test resources for further examples:
- [odoo_csv/units_of_measure/product.uom.csv](../odoo_initializer/tests/resources/odoo_csv/units_of_measure/product.uom.csv)

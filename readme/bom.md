### Model `bill_of_material`

The `bill_of_material` subfolder allows to import stock warehouses provided as CSV files. See the example below:

| id | bom_line_ids/product_id/id | bom_line_ids/product_qty | product_tmpl_id/id | product_qty |
| - | - | - | - | - | 
| init.fded4b3a-9674-4cdb-9ba2-a5ec922b61f7 | init.4392860e-a2bc-4e00-87af-8003f5fcd47e | 3 | init.1a3d9c2d-7067-4d68-8f5c-70c4afea89d1_product_template | 10 |


See the test resources for further examples:
- [odoo_csv/bills_of_material/bom.csv](../odoo_initializer/tests/resources/odoo_csv/bills_of_material/bom.csv)

### Model `product`

The `product` subfolder allows to import products provided as CSV files. See the example below:

| id | product_variant_ids/id | lst_price | price |
| - | - | - | - |
| init.testProduct | init.testProductVariant | 10 | 15|

See the test resources for further examples:
- [odoo_csv/product/product.template.csv](../odoo_initializer/tests/resources/odoo_csv/product/product.template.csv)


:exclamation:
**Note**: Product vs Product Variant
The product domain is represented by product.template model. It can be used as a template for its variations, called product variants (product.product).

To define a product variant please use Product Variant domain instead.

This domain is the place where to create the mappings between the product and its variants as shown above in the example.
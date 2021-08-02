### Model `drug`

The `drug` subfolder allows you to import Odoo products provided as CSV files.
It is designed specifically load OpenMRS Initializer drug type of files, ie, of a format compatible with [OpenMRS Module Initializer](https://github.com/mekomsolutions/openmrs-module-initializer/) concepts files.

The drug loader will apply a specific mapping to translate the OpenMRS Initializer file headers and into Odoo compatible headers such as:

[drug_loader.py#L6-L11](https://github.com/mekomsolutions/odoo-initializer/blob/ce149ea01c58c1101ee43f20d5dbcbad26a332af/odoo_initializer/models/drug_loader.py#L6-L11)
```
field_mapping = {
    "product_variant_ids/id": "odoo_variant_id",
    "id": "odoo_id"
}
```
Note: `drug` loader work in conjunction with `drug_variant` loader by providing a mapping to the defined products variants in `drug_variant`, see [here](drug_variant.md)
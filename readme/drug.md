### Model `drug`

The `drug` subfolder allows you to import Odoo products provided as CSV files.
It is designed specifically load OpenMRS Initializer drug type of files, ie, of a format compatible with [OpenMRS Module Initializer](https://github.com/mekomsolutions/openmrs-module-initializer/) concepts files.
See an example file: [OpenMRS Drugs.csv](https://github.com/mekomsolutions/openmrs-module-initializer/blob/master/readme/drugs.md)

The drug loader has been designed to allow OpenMRS and Odoo to share a common set of metadata and avoid maintaining 2 files.

So the Odoo drug loader allows you to provide to import products (drugs) in Odoo and provide a base price directly on the OpenMRS file.

The drug loader will apply a specific mapping to translate the OpenMRS Initializer file headers and into Odoo compatible headers such as:

[drug_loader.py#L6-L11](https://github.com/mekomsolutions/odoo-initializer/blob/ce149ea01c58c1101ee43f20d5dbcbad26a332af/odoo_initializer/models/drug_loader.py#L6-L11)
```
field_mapping = {
    "id": "Uuid",
    "name": "Name",
    "drug": "Concept Drug",
    "lst_price": "odoo_price",
    "categ_id/id": "odoo_category",
}
```

See the example below:

| Uuid | 	Name |	Concept Drug |	odoo_price | odoo_category |
| - | - | - | - | - |
| 1 | Paracetamol 500mg | paracetamol | 120 | product.product_category_all |
| 2 | Panadol | paracetamol | 200 | product.product_category_all |
| 3 | Metacin 1g | paracetamol | 300 | product.product_category_all |


See the test resources for further examples:
- [openmrs_csv/drugs/drugs.csv](../odoo_initializer/tests/resources/openmrs_csv/drugs/drugs.csv)

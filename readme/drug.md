### Model `drug`

The `drug` subfolder allows you to import Odoo **product variants** provided as CSV files.
It is designed specifically load OpenMRS Initializer drug type of files, ie, of a format compatible with [OpenMRS Module Initializer](https://github.com/mekomsolutions/openmrs-module-initializer/) concepts files.
See an example file: [OpenMRS Drugs.csv](https://github.com/mekomsolutions/openmrs-module-initializer/blob/master/readme/drugs.md)

The drug loader has been designed to allow OpenMRS and Odoo to share a common set of metadata and avoid maintaining multiple files.

Thus the Odoo drug loader allows you to provide product fields (such as cost, price, category...) directly on the OpenMRS file.

The drug loader will apply a specific mapping to translate the OpenMRS Initializer file headers and into Odoo compatible headers such as:

[drug_loader.py#L6-L11](../odoo_initializer/models/drug_loader.py#L6-L18)
```
field_mapping = {
    "uuid": "Uuid",
    "name": "Name",
    "lst_price": "odoo_price",
    "categ_id/id": "odoo_category",
    "type":"odoo_type",
    "id": "odoo_id",
    "uom_id/id": "odoo_uom",
    "standard_price": "odoo_cost"
}
```

See the example below:

| Uuid | Name |	Concept Drug |	odoo_price | odoo_category | odoo_id | odoo_type | odoo_uom | odoo_cost
| - | - | - | - | - | - | - | - | - |
| 1 | Paracetamol 500mg | paracetamol | 120 | product.product_category_all | paracetamol_500mg | Stockable Product | product.product_uom_qt | 80 |
| 2 | Panadol | paracetamol | 200 | product.product_category_all | Panadol | Stockable Product | product.product_uom_qt | 150 |
| 3 | Metacin 1g | paracetamol | 300 | product.product_category_all | Metacin_1g | Stockable Product | product.product_uom_qt | 200 |

`Note` :
- All fields in the example are mandatory, if a field is missing the file import will be skipped


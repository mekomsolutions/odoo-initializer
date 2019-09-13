### Model `concept`

The `concept` subfolder allows you to import Odoo products provided as CSV files.
It is designed specifically to load OpenMRS Initializer concepts type of files, ie, of a format compatible with [OpenMRS Module Initializer](https://github.com/mekomsolutions/openmrs-module-initializer/) concepts files.

The order loader has been designed to allow OpenMRS and Odoo to share a common set of metadata and avoid maintaining 2 files.

So the Odoo order loader allows you to provide to import products (concepts) in Odoo and provide a base price directly on the OpenMRS file.

The drug loader will apply a specific mapping to translate the OpenMRS Initializer file headers into Odoo compatible headers.

```
field_mapping = {
    "lst_price": "odoo_price",
    "product_variant_ids/categ_id/id": "odoo_category",
    "type": "odoo_type",
    "name": "Short name:en",
    "product_variant_ids/uuid": "Uuid",
    "id": "odoo_id",
    "description": "Data class",
    }
```

See the example below:

| Uuid | 	Short name:en |	Data class |	odoo_price | odoo_category | odoo_id | odoo_type |
| - | - | - | - | - | - | - |
| 1 | XR 2 View Abdomen | Radiology | 2000 | bahmni_product.categ_services_radiology | hsc_XR 2 View Abdomen | service |

`Note` :
- All fields in the example are mandatory, if a field is missing the file import will be skipped


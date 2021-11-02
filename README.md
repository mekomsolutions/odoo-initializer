<img src="readme/crudem-hsc-logo.png" alt="hsc-logo" width="400"/>

------

# Odoo Initializer Add-on

### Introduction
This add-on aims at providing a configuration layer to let implementers start an Odoo server with a given set of pre-loaded settings and metadata, that is versioned controlled.

Settings and metadata will be loaded onto the Odoo server based on what is provided in the data files.

Those data files are mostly in CSV and XML formats, depending of the model that is loaded.

They are processed when the add-on is installed.

### Supported models:

See below the list of supported models:
- [Currency (CSV)](./readme/currency.md)
- [Country (CSV)](./readme/country.md)
- [System Parameter (CSV)](./readme/system_parameter.md)
- [Company Property (CSV)](./readme/company_property.md)
- [Drug (CSV)](./readme/drug.md)
- [Fiscal Position (CSV)](./readme/fiscal_position.md)
- [Journal (CSV)](./readme/journal.md)
- [Payment (CSV)](./readme/payment_term.md)
- [Price List (CSV)](./readme/price_list.md)
- [Stock (CSV)](./readme/stock_location.md)
- [Company (CSV)](./readme/company.md)
- [Partner (CSV)](./readme/partner.md)
- [Units of Measure](./readme/uom.md)
- [Shop (CSV)](./readme/sale_shop.md) (Bahmni specific)
- [Product Variant (CSV)](./readme/product_variant.md)
- [Product (CSV)](./readme/product.md)
- [Product Category (CSV)](./readme/product_category.md)
- [Order Type (CSV)](./readme/order_type.md) (Bahmni specific)
- [Shop Mapping (CSV)](./readme/shop_mapping.md) (Bahmni specific)
- [Default Value (CSV)](./readme/default_value.md)
- [Decimal Precision (CSV)](./readme/decimal_precision.md)
- [Language (XML)](./readme/language.md)
- [NEW: Additional models can now be added via configuration file!](###-support-additional-models-through-configuration-file)


### Support additional models through configuration file:

Adding support to more models is possible by providing them as models in the configuration file (see example [here](./odoo_initializer/tests/resources/config/inializer_config.json)) and set the file path in odoo.conf as following

```
initializer_config_file_path = /mnt/odoo_config/initializer_config.json
```
### Specific model behavior parameters:

Below is the list of supported optional parameters, that can change behavior when handling model files:

#### field mapping:
Map field name in Odoo model with column name in CSV file, see example [here](./odoo_initializer/models/orders_loader.py#L6-L14)

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
Field mapping is a JSON object where keys are Odoo field names (eg: "lst_price") and values are CSV column names (eg: "odoo_price")
In that case, it allows Odoo initializer to process Concept files from OpenMRS Initializer compatible files.

#### filters:
Filter out rows where value of selected column does not match the specified options, see example [here](./odoo_initializer/models/orders_loader.py#L16)
```
filters = {
        "Data class": ["LabTest",
                       "Radiology"]
    }
```
From the example above, only rows where `Data Class` value is "LabTest" or "Radiology" will be loaded.

#### rules
Apply a defined function on each row of a CSV file by taking a field name as a parameter, see example [here](./odoo_initializer/models/product_loader.py#L8-L10)

available rules:
- NO_UPDATE: do not update the specified field if the record exists.
- EXTERNAL_TO_INTERNAL_ID: substitute external id with internal id

```
field_rules = {
        "lst_price": "NO_UPDATE"
    }
```
If record exists we update it without "lst_price".

Note: [here](./odoo_initializer/models/currency_loader.py#L4) is a default domain implementation example
```
class CurrencyLoader(BaseLoader):
    model_name = "res.currency"
    folder = "currency"
```

A default loader is a class that inherits [BaseLoader]((./odoo_initializer/models/base_loader.py#) where `folder` is the configuration subfolder where all files to be loaded are placed, and `model_name` is the Odoo database model where all records in files should be saved.

----
## Build, Test and Deploy
Requires [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/install/) to be installed.

### Run add-on tests

Project tests should be run using the following Gradle command:
```
./gradlew clean test
```

Once the tests have run, you may want to run `./gradlew cleanDocker` to make sure all the resources are destroyed (containers, volumes, folders)

### Install locally

Install the archive locally:
```
./gradlew clean install
```

### Deploy on repository

2 was to set the credentials:
- export username/password as environment variables:
```
# Prompt for Nexus username and password
read -p "Nexus username: " user; export NEXUS_USER=$user; read -sp "Nexus password: " password; export NEXUS_PASSWORD=$password; echo ""
```
```
./gradlew publish -Puser=${NEXUS_USER} -Ppassword=${NEXUS_PASSWORD}
```

- read from the `~/.m2/settings.xml` file:
```
export NEXUS_REPO_ID="mks-nexus"
```
```
./gradlew publish -PrepoId=${NEXUS_REPO_ID}
```

(Note that, if set, the `-Puser` and `-Ppassword` will take precedence over the settings read in the `~/.m2/settings.xml`)

By default the repo URL will be Mekom Nexus repository, but you can provide your own artifact repository URL by adding:
```
-Purl="https://my-nexus/url"
```

### Additional info
- To run Odoo tests and process the CSV files:
```
./gradlew clean test
```

- To process CSV files and keep Odoo server running:
```
./gradlew clean run
```

Note: You can always run both tasks by using 
```
./gradlew clean test run
```

The Odoo server will be accessible at http://localhost:8069

- If you want to force remove all the containers created in the tests, run the following:
```
./gradlew cleanDocker
```

- The addon will expect some properties to be provided in the odoo.conf file. Those are:
-- `initializer_checksums_path`: where to save checksums of processed files (to avoid re-processing old files upon restart)
-- `initializer_data_files_paths`: comma separated list of where to find the Odoo configuration files.

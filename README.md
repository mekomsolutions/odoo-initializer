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
- [Company Property (CSV)](./readme/company_property.md)
- [Drug (CSV)](./readme/drug.md)
- [Fiscal Position (CSV)](./readme/fiscal_position.md)
- [Journal (CSV)](./readme/journal.md)
- [Payment (CSV)](./readme/payment_term.md)
- [Price List (CSV)](./readme/price_list.md)
- [Stock (CSV)](./readme/stock_location.md)
- [Company (CSV)](./readme/company.md)
- [Partner (CSV)](./readme/partner.md)
- [Shop (CSV)](./readme/sale_shop.md) (Bahmni specific)

----
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
- The `test` Gradle task will in fact run 2 substasks: **runUnitTests** and **processCSVs**.
You can run those 2 tasks independently if you which.
```
./gradlew clean runUnitTests
```
```
./gradlew clean processCSVs
```

- If you are willing to leave the Odoo server running after running the tests, use:
```
./gradlew clean test run
```
The Odoo server will be accessible at http://localhost:8069

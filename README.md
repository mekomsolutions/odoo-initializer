# Odoo Initializer Add-on

### Run tests

Project tests should be run using the following Gradle command:
```
./gradlew clean test
```

Once the tests have run, you may want to run `./gradlew clean` again to make sure all the resources are destroyed (containers, volumes, folders)

### Run the tests and let the Odoo server running
If you are willing to leave the server running after the tests are run, use:
```
./gradlew clean test run
```
The Odoo server will be accessible at http://localhost:8069

### Additional info
The `test` Gradle task will in fact run 2 substasks: **runUnitTests** and **processCSVs**
You can run those 2 tasks independently if you which only run tests partially
```
./gradlew clean runUnitTests
```
```
./gradlew clean processCSVs
```

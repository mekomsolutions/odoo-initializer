### Model `fiscal_position`

The `fiscal_position` subfolder allows to import Fiscal Position provided as CSV files. See the example below:

| id | active | company_id/id | account_ids/account_src_id/id | account_ids/account_dest_id/id | account_ids/create_date | country_id/id | country_group_id/id | auto_apply | state_ids/id | name | vat_required | zip_from | zip_to |
| -
| \init.account_fiscal_position_1 | True |  |  |  |  |  | base.europe | True |  | European Companies | True | 0 | 0 |


See the test resources for further examples:
- [odoo_csv/fiscal_position/account.fiscal.position.csv](../odoo_initializer/tests/resources/odoo_csv/fiscal_position/account.fiscal.position.csv)

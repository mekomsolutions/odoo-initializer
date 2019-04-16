### Model `journal`

The `journal` subfolder allows to import Journals provided as CSV files. See the example below:

| id | name | bank_acc_number | type_control_ids/id | account_control_ids/id | update_posted | bank_id/id | bank_account_id/id | company_id/id | currency_id/id | inbound_payment_method_ids/id | outbound_payment_method_ids/id | code | type |
| -
| \init.account_journal_debt | Debt |  |  |  | False |  |  | base.main_company |  | account.account_payment_method_manual_in | account.account_payment_method_manual_out, account_check_printing.account_payment_method_check | DEBT | Bank |


See the test resources for further examples:
- [odoo_csv/journal/account.journal.csv](../odoo_initializer/tests/resources/odoo_csv/journal/account.journal.csv)

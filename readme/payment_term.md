### Model `payment_term`

The `payment_term` subfolder allows to import Payment Terms provided as CSV files. See the example below:

| id | company_id/id | name | line_ids/days | line_ids/value_amount | note | line_ids/option | line_ids/value
| -
| account.account_payment_term_90days | base.main_company | 90 Days | 90 | 0 | Payment term: 90 Days | Day(s) after the invoice date | Balance


See the test resources for further examples:
- [odoo_csv/payment_term/account.payment.term.csv](../odoo_initializer/tests/resources/odoo_csv/payment_term/account.payment.term.csv)

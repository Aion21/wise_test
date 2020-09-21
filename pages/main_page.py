from selene import be, query, have
from selene.support.shared import browser

from entities.customer import Customer
from utils.properties import url


class MainPage:

    def __init__(self):
        self.result_table_css = 'table.w3-table-all'
        self.result_table_rows_css = '.w3-table-all tbody tr'
        self.result_table_rows_data_css = 'td'
        self.result_message = 'div#divResultSQL div'

    def get_result_table(self):
        browser.element(self.result_table_css).should(be.existing)
        return browser.all(self.result_table_rows_css)

    @staticmethod
    def go_to_main_page():
        browser.open(url)

    @staticmethod
    def set_and_run_sql(sql):
        browser.driver.execute_script(f'window.editor.setValue("{sql}")')
        browser.driver.execute_script('w3schoolsSQLSubmit()')

    def make_customers_list(self):
        result_table = self.get_result_table()
        customers_list = []

        for row in result_table:
            customer_data = []
            for data in row.all(self.result_table_rows_data_css):
                customer_data.append(data.get(query.text))
            if customer_data:
                customers_list.append(customer_data)

        return [Customer(customer_data) for customer_data in customers_list]

    def made_changes_one_row_check(self):
        browser.element(self.result_message).should(
            have.text('You have made changes to the database. Rows affected: 1'))

    def insert_customer(self, customer):
        sql = f"INSERT INTO Customers (CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country) " \
              f"VALUES ('{customer.customer_ID}','{customer.customer_name}','{customer.contact_name}'," \
              f"'{customer.address}','{customer.city}','{customer.postal_code}','{customer.country}')"

        self.set_and_run_sql(sql)
        self.made_changes_one_row_check()

    def update_customer(self, customer):
        sql = f"UPDATE Customers SET CustomerName = '{customer.customer_name}', ContactName = '{customer.contact_name}'," \
              f" Address = '{customer.address}', City = '{customer.city}', PostalCode = '{customer.postal_code}', " \
              f"Country = '{customer.country}' WHERE CustomerID = '{customer.customer_ID}'"

        self.set_and_run_sql(sql)
        self.made_changes_one_row_check()

    def delete_customer(self, customer):
        sql = f"DELETE FROM Customers WHERE CustomerID = '{customer.customer_ID}'"
        self.set_and_run_sql(sql)
        self.made_changes_one_row_check()

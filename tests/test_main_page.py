import time

import pytest

from entities.customer import Customer
from pages.main_page import MainPage
from utils.sql_statements import city_london, all_customers
from utils.utils import get_random_string, random_picker


def test_1_task(setup_browser):
    MainPage().go_to_main_page()
    MainPage().set_and_run_sql(all_customers)
    customers_list = MainPage().make_customers_list()
    assert any(customer for customer in customers_list if
               customer.contact_name == 'Giovanni Rovelli' and customer.address == 'Via Ludovico il Moro 22')


def test_2_task(setup_browser):
    MainPage().go_to_main_page()
    MainPage().set_and_run_sql(city_london)
    customers_list = MainPage().make_customers_list()
    assert len(customers_list) == 6


def test_3_task(setup_browser):
    MainPage().go_to_main_page()
    customer = Customer(['99', 'Detective agency', 'Sherlock Holmes', 'Baker st. 221', 'London', 'NW1', 'UK'])
    MainPage().insert_customer(customer)
    MainPage().set_and_run_sql(all_customers)
    customers_list = MainPage().make_customers_list()
    assert customer in customers_list


def test_4_task(setup_browser):
    MainPage().go_to_main_page()
    MainPage().set_and_run_sql(all_customers)
    customers_list = MainPage().make_customers_list()
    customer = random_picker(customers_list)
    customer.customer_name = get_random_string(7)
    customer.contact_name = get_random_string(4)
    customer.address = get_random_string(7)
    customer.city = get_random_string(6)
    customer.postal_code = get_random_string(4)
    customer.country = get_random_string(3)
    MainPage().update_customer(customer)
    MainPage().set_and_run_sql(all_customers)
    customers_list = MainPage().make_customers_list()
    assert customer in customers_list


def test_5_task(setup_browser):
    MainPage().go_to_main_page()
    MainPage().set_and_run_sql(all_customers)
    customers_list = MainPage().make_customers_list()
    customer = random_picker(customers_list)
    MainPage().delete_customer(customer)
    MainPage().set_and_run_sql(all_customers)
    customers_list = MainPage().make_customers_list()
    assert customer not in customers_list

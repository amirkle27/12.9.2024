from fileinput import close

from numpy.ma.extras import average

import sqlite_lib

#2
#a
def count_customers ():
    sqlite_lib.connect('ecomm.db')
    customers_number = sqlite_lib.run_query_select("SELECT COUNT ('Customer ID')"
                                                   "FROM 'E-commerce Customer Behavior - Sheet1'")
    sqlite_lib.close()
    return customers_number [0][0]


if __name__ == "__main__":
    print(count_customers())

#b
def average_customer_age ():
    sqlite_lib.connect('ecomm.db')
    average_age = sqlite_lib.run_query_select("SELECT AVG(Age)"
                                              "FROM 'E-commerce Customer Behavior - Sheet1'")
    sqlite_lib.close()
    return average_age[0][0]

if __name__ == "__main__":
    print(average_customer_age())

#c
def counting_men_women ():
    sqlite_lib.connect('ecomm.db')
    counting_men = sqlite_lib.run_query_select("SELECT COUNT (*)"
                                               "FROM 'E-commerce Customer Behavior - Sheet1'"
                                               "WHERE Gender = 'Male'")

    counting_women = sqlite_lib.run_query_select("SELECT COUNT (*)"
                                                 "FROM 'E-commerce Customer Behavior - Sheet1'"
                                                 "WHERE GENDER = 'Female'")

    answer = (f"Number of Male Customers: {counting_men[0][0]}\nNumber of Female Customers: {counting_women[0][0]}")
    sqlite_lib.close()
    return answer

if __name__ == "__main__":
    print(counting_men_women())

#d
def average_purchases ():
    sqlite_lib.connect('ecomm.db')
    men_purchase_average = sqlite_lib.run_query_select('SELECT AVG("Items Purchased")'
                                                       'FROM "E-commerce Customer Behavior - Sheet1"'
                                                       'WHERE Gender = "Male"')

    women_purchase_average = sqlite_lib.run_query_select('SELECT AVG("Items Purchased")'
                                                         'FROM "E-commerce Customer Behavior - Sheet1"'
                                                         'WHERE Gender = "Female"')

    answer = (f"Average Purchases made by Male Customers: {men_purchase_average[0][0]}\nAverage Purchases made by Female Customers: {women_purchase_average[0][0]}")
    sqlite_lib.close()
    return answer

if __name__ == "__main__":
    print(average_purchases())

#e
def membership_types ():
    sqlite_lib.connect('ecomm.db')
    memberships = sqlite_lib.run_query_select('SELECT COUNT (DISTINCT "Membership Type")'
                                              'FROM "E-commerce Customer Behavior - Sheet1"')
    sqlite_lib.close()
    return memberships [0][0]

if __name__ == "__main__":
    print(membership_types())

#f
def counting_members_by_membership_kinds ():
    sqlite_lib.connect('ecomm.db')
    count = sqlite_lib.run_query_select('SELECT "Membership Type", COUNT ("Customer ID")'
                                        'FROM "E-commerce Customer Behavior - Sheet1"'
                                        'GROUP BY "Membership Type"')
    sqlite_lib.close()
    return count

if __name__ == "__main__":
    result = counting_members_by_membership_kinds()
    for membership_type, customer_count in result:
        print(f"{membership_type:6}: {customer_count} customers")

#g
def counting_ny_customets ():
    sqlite_lib.connect('ecomm.db')
    counting = sqlite_lib.run_query_select('SELECT "City", COUNT ("Customer ID")'
                                           ' FROM "E-commerce Customer Behavior - Sheet1"'
                                           ' Where City = "New York"')
    sqlite_lib.close()
    return counting

if __name__ == "__main__":
    for city, customers in counting_ny_customets():
        print(f"{city} - {customers}")

#h
def counting_customers_by_city ():
    sqlite_lib.connect('ecomm.db')
    count = sqlite_lib.run_query_select('SELECT "City", COUNT("Customer ID")'
                                        'FROM "E-commerce Customer Behavior - Sheet1"'
                                        'GROUP BY "City"'
                                        'ORDER BY "Customer ID" ' )
    sqlite_lib.close()
    return count

if __name__ == "__main__":
    for city, customers in counting_customers_by_city():
        print(f"{city:<15}: {customers}")

#i
def total_spend_men_women ():
    sqlite_lib.connect('ecomm.db')
    count = sqlite_lib.run_query_select('SELECT "Gender", SUM("TOTAL SPEND")'
                                        'FROM "E-commerce Customer Behavior - Sheet1"'
                                        'GROUP BY "Gender"')
    sqlite_lib.close()
    return count

if __name__ == "__main__":
    for gender, total  in total_spend_men_women():
        print(f"{gender:<6}: {total}")

#j
def most_least_products ():
    sqlite_lib.connect('ecomm.db')
    count_max = sqlite_lib.run_query_select(
        'SELECT "Customer ID", "Items Purchased" '
        'FROM "E-commerce Customer Behavior - Sheet1" '
        'WHERE "Items Purchased" = (SELECT MAX("Items Purchased")'
        'FROM "E-commerce Customer Behavior - Sheet1")'
    )

    count_min = sqlite_lib.run_query_select(
        'SELECT "Customer ID", "Items Purchased" '
        'FROM "E-commerce Customer Behavior - Sheet1" '
        'WHERE "Items Purchased" = (SELECT MIN("Items Purchased") '
        'FROM "E-commerce Customer Behavior - Sheet1")'
    )

    sqlite_lib.close()

    count_max_output = [info for info in count_max]
    count_min_output = [info for info in count_min]
    return count_max_output, count_min_output

if __name__ == "__main__":
    max_results, min_results = most_least_products()

    for customer, items in max_results:
        print(f"Customer no. {customer} bought the largest number of products - {items}")
    for customer, items in min_results:
        print(f"Customer no. {customer} bought the smallest number of products - {items}")



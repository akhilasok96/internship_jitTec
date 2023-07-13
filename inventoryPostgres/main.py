import psycopg2
import random

class Inventory:
    def add_product(self):
        product_id = random.randrange(100,500)
        product_name = input("Enter product name: ")
        category_id = int(input("Enter the category id: "))
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))

        conn = psycopg2.connect(
            database="company",
            user="postgres",
            password="postgres",
            host="127.0.0.1",
            port="5432",
        )

        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO inventory (product_id, product_name, category, quantity, price) VALUES ({product_id},'{product_name}', {category_id}, {quantity}, {price})"
        )
        conn.commit()
        conn.close()
        print("Product added successfully.")

    def update_inventory(self):
        product_name = input("Enter product name: ")
        new_quantity = int(input("Enter new quantity: "))

        conn = psycopg2.connect(
            database="company",
            user="postgres",
            password="postgres",
            host="127.0.0.1",
            port="5432",
        )
        cursor = conn.cursor()
        cursor.execute(
            f"UPDATE inventory SET quantity = {new_quantity} WHERE product_name = '{product_name}'"
        )
        conn.commit()
        conn.close()
        print("Inventory updated successfully.")

    def display_product_details(self):
        product_name = input("Enter product name: ")

        conn = psycopg2.connect(
            database="company",
            user="postgres",
            password="postgres",
            host="127.0.0.1",
            port="5432",
        )
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM inventory WHERE product_name = '{product_name}'"
        )
        product = cursor.fetchone()
        conn.close()

        if product:
            print("Product ID:", product[0])
            print("Product Name:", product[1])
            print("Category ID:", product[2])
            print("Quantity:", product[3])
            print("Price:", product[4])
        else:
            print("Product not found.")


class Sales:
    def print_sales_report(self):
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")

        conn = psycopg2.connect(
            database="company",
            user="postgres",
            password="postgres",
            host="127.0.0.1",
            port="5432",
        )
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT s.sales_id, s.product_id, s.customer_id, s.quantity, i.product_name, (s.quantity * i.price) as 'Total Sales' FROM sales s inner join inventory i on s.product_id = i.product_id WHERE s.date BETWEEN {start_date} AND {end_date}"
        )
        sales = cursor.fetchall()
        conn.close()

        if sales:
            print("Sales Report:")
            for sale in sales:
                print("Sale ID:", sale[0])
                print("Product ID:", sale[1])
                print("Customer ID:", sale[2])
                print("Quantity:", sale[3])
                print("Total Price:", sale[4])
                print("Date:", sale[5])
        else:
            print("No sales found between the given dates.")

    def insert_sale(self):
        sales_id = random.randrange(1000,1800)
        product_id = int(input("Enter product ID: "))
        customer_id = int(input("Enter customer ID: "))
        quantity = int(input("Enter quantity: "))
        date = input("Enter product ID: ")

        conn = psycopg2.connect(
            database="company",
            user="postgres",
            password="postgres",
            host="127.0.0.1",
            port="5432",
        )
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO sales VALUES({sales_id},{product_id}, {customer_id}, {quantity}, '{date}')"
        )
        conn.commit()

        cursor.execute(f"SELECT quantity from inventory where product_id={product_id}")
        quant = cursor.fetchone()
        remQ = quant[0][0] - quantity
        cursor.execute(f"UPDATE inventory SET quantity={remQ} where product_id = {product_id}")
        conn.close()
        print("Sale inserted successfully.")


class Customers:
    def __init__(self):
        self.conn = psycopg2.connect(
            database="company",
            user="postgres",
            password="postgres",
            host="127.0.0.1",
            port="5432",
        )
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def get_customer_details(self, customer_id):
        self.cursor.execute(f"SELECT * FROM customers")
        customer = self.cursor.fetchone()

        if customer:
            print("Customer ID:", customer[0])
            print("Customer Name:", customer[1])
            print("Email:", customer[2])
        else:
            print("Customer not found.")


def main():
    inventory = Inventory()
    sales = Sales()
    customers = Customers()

    while True:
        print("------ MENU ------")
        print("1. Add Product to Inventory")
        print("2. Update Inventory")
        print("3. Print Sales Report")
        print("4. Insert Sale")
        print("5. Display Product Details")
        print("6. Display Customer Details")
        print("7. Exit")
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                inventory.add_product()
            case 2:
                inventory.update_inventory()
            case 3:
                sales.print_sales_report()
            case 4:
                sales.insert_sale()
            case 5:
                inventory.display_product_details()
            case 6:
                customer_id = int(input("Enter customer ID: "))
                customers.get_customer_details(customer_id)
            case 7:
                break

main()

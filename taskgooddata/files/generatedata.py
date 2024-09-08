import random
import string
import names
import csv
import datetime

class GenerateData:
    def __init__(self):
        self.customers = []
        self.products = []
        self.sales = []
        # self.header_written = False  # Flag to track header writing

    def generate_random_name(self):
        first_name = names.get_first_name()
        last_name = names.get_last_name()
        return first_name + " " + last_name

    def generate_random_email(self, name):
        first_name, last_name = name.split()
        domain = random.choice(["kozel.com", "pilsner.org", "gambrinus.net", "staropramen.cz"])
        email = first_name[0] + last_name + "@" + domain
        return email

    def generate_random_age(self):
        return random.randint(15, 70)

    def generate_random_gender(self):
        return random.choice(["Male", "Female"])

    # def generate_random_product_name(self):
    #     product_type = random.choice(["Laptop", "Cellphone", "TV", "Tablet", "Smartwatch", "Headphone", "Console"])
    #     brand = random.choice(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"])
    #     return product_type + " " + brand

    def generate_random_product_name(self):
        product_type = random.choice(["Laptop", "Cellphone", "TV", "Tablet", "Smartwatch", "Headphone", "Console"])
        brand = random.choice(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"])
        # Add a counter for unique product names within a category
        product_name_counter = 1
        for product in self.products:
            if product[1].startswith(product_type + " " + brand):
                product_name_counter += 1
        return product_type + " " + brand + " " + str(product_name_counter)


    def generate_random_price(self, product_type):
        if product_type == "Laptop":
            return round(random.uniform(700, 2000), 1)
        elif product_type == "Cellphone":
            return round(random.uniform(400, 1000), 1)
        elif product_type == "TV":
            return round(random.uniform(500, 2500), 1)
        elif product_type == "Tablet":
            return round(random.uniform(300, 1500), 1)
        elif product_type == "Smartwatch":
            return round(random.uniform(200, 500), 1)
        elif product_type == "Headphone":
            return round(random.uniform(50, 200), 1)
        else:
            return round(random.uniform(300, 1000), 1)

    def create_customer_data(self, num_customers):
        for i in range(1, num_customers + 1):
            name = self.generate_random_name()
            age = self.generate_random_age()
            gender = self.generate_random_gender()
            email = self.generate_random_email(name)
            self.customers.append((i, name, age, gender, email))

    def create_product_data(self, num_products):
        for i in range(1, num_products + 1):
            product_name = self.generate_random_product_name()
            price = self.generate_random_price(product_name.split()[0])
            stock_quantity = random.randint(0, 100)
            self.products.append((i, product_name, price, stock_quantity))

    def create_sales_data(self, num_sales):
        for i in range(1, num_sales + 1):
            customer_id = random.randint(1, len(self.customers))
            product_id = random.randint(1, len(self.products))
            sale_date = datetime.datetime(2023, 9, 1) + datetime.timedelta(days=random.randint(0, 365))
            quantity = random.randint(1, 5)
            product = next(p for p in self.products if p[0] == product_id)
            total_amount = round(product[2] * quantity, 2)
            paid_method = random.choice(["cash", "debit", "credit"])
            self.sales.append((i, customer_id, product_id, sale_date.strftime("%Y-%m-%d"), quantity, total_amount, paid_method))


        # Function to save data to CSV
    def save_to_csv(self, filename, data, header):
        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)  # Write the header row
            for row in data:
                writer.writerow(row)

if __name__ == "__main__":
    data_generator = GenerateData()
    data_generator.create_customer_data(100)
    data_generator.create_product_data(50)
    data_generator.create_sales_data(1000)

    data_generator.save_to_csv("CustomerData.csv", data_generator.customers, 
                               ["CustomerID", "CustomerName", "Age", "Gender", "Email"])
    data_generator.save_to_csv("ProductData.csv", data_generator.products, 
                               ["ProductID", "ProductName", "Price", "StockQuantity"])
    data_generator.save_to_csv("SalesData.csv", data_generator.sales, 
                               ["SaleID", "CustomerID", "ProductID", "SaleDate", "Quantity", "TotalAmount", "PaymentMethod"])

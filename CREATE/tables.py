from base import Database

def  city():
    query = f'''
    CREATE TABLE city(city_id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    last_update TIMESTAMP DEFAULT NOW());'''

    Database.connect("localhost", "pharmacy", "postgres", "azizullo", query)

def address():
    query = """
CREATE TABLE Address (
    address_id SERIAL PRIMARY KEY,
    street VARCHAR(50) NOT NULL,
    city_id INT REFERENCES City(city_id),
    last_update TIMESTAMP DEFAULT NOW());"""
    Database.connect("localhost", "pharmacy", "postgres", "azizullo", query)
    return "Successful"

def manufacturer ():
    query = """
CREATE TABLE Manufacturer (
    manufacturer_id SERIAL PRIMARY KEY,
    manufacturer_name VARCHAR(50) NOT NULL);"""
    Database.connect("localhost", "pharmacy", "postgres", "azizullo", query)
    return "Successful"

def product ():
    query = """
    CREATE TABLE Product (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    manufacturer_id INT REFERENCES Manufacturer(manufacturer_id) ON DELETE CASCADE);"""
    Database.connect("localhost", "pharmacy", "postgres", "azizullo", query)
    return "Successful"

-- Create Pharmacy table
CREATE TABLE Pharmacy (
    pharmacy_id SERIAL PRIMARY KEY,
    pharmacy_name VARCHAR(255) NOT NULL,
    address_id INT REFERENCES Address(address_id) ON DELETE CASCADE
);

-- Create Staff table
CREATE TABLE Staff (
    staff_id SERIAL PRIMARY KEY,
    staff_name VARCHAR(255) NOT NULL,
    address_id INT REFERENCES Address(address_id) ON DELETE CASCADE
);

-- Create Payment Type table
CREATE TABLE Payment_Type (
    payment_type_id SERIAL PRIMARY KEY,
    payment_type_name VARCHAR(255) NOT NULL
);

-- Create Payment table
CREATE TABLE Payment (
    payment_id SERIAL PRIMARY KEY,
    pharmacy_id INT REFERENCES Pharmacy(pharmacy_id) ON DELETE CASCADE,
    staff_id INT REFERENCES Staff(staff_id) ON DELETE CASCADE,
    payment_type_id INT REFERENCES Payment_Type(payment_type_id) ON DELETE CASCADE
);

-- Create Pharmacy_Product table
CREATE TABLE Pharmacy_Product (
    pharmacy_id INT REFERENCES Pharmacy(pharmacy_id) ON DELETE CASCADE,
    product_id INT REFERENCES Product(product_id) ON DELETE CASCADE,
    PRIMARY KEY (pharmacy_id, product_id)
);



if __name__ == "__main__":
    city()

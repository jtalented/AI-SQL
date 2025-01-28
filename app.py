import sqlite3
import openai

# Initialize OpenAI API
openai.api_key = "************************"

# initialize the database if it doesn't exist
def initialize_database():
    conn = sqlite3.connect("restaurant_management.db")
    cursor = conn.cursor()
    # Create tables
    cursor.executescript("""
CREATE TABLE Restaurants (
    RestaurantID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Location TEXT,
    CuisineType TEXT
);

                         


CREATE TABLE Menus (
    MenuID INTEGER PRIMARY KEY,
    RestaurantID INTEGER,
    MenuName TEXT NOT NULL,
    FOREIGN KEY (RestaurantID) REFERENCES Restaurants(RestaurantID)
);

                         
CREATE TABLE Dishes (
    DishID INTEGER PRIMARY KEY,
    MenuID INTEGER,
    DishName TEXT NOT NULL,
    Price REAL NOT NULL,
    FOREIGN KEY (MenuID) REFERENCES Menus(MenuID)
);

                         

CREATE TABLE Customers (
    CustomerID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    PhoneNumber TEXT
);

                         

CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY,
    CustomerID INTEGER,
    OrderDate TEXT NOT NULL,
    TotalAmount REAL NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

                         


CREATE TABLE OrderItems (
    OrderItemID INTEGER PRIMARY KEY,
    OrderID INTEGER,
    DishID INTEGER,
    Quantity INTEGER NOT NULL,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (DishID) REFERENCES Dishes(DishID)
);
""")
    



    conn.commit()
    return conn

# User input
def generate_sql_from_prompt(prompt, schema_description):
    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",

        messages=[
            {"role": "system", "content": f"Schema: {schema_description}"},
            {"role": "user", "content": prompt}
        ]

    )

    return response['choices'][0]['message']['content']

# results
def execute_query(conn, sql):
    cursor = conn.cursor()
    #try
    try:
        cursor.execute(sql)
        if cursor.description:
            rows = cursor.fetchall()
            return rows
        else:
            conn.commit()
            return "Query executed successfully."
    except Exception as e:
        return f"Error: {str(e)}"




# Main App
def main():
    conn = initialize_database()
    schema_description = """
    Restaurants(RestaurantID, Name, Location, CuisineType),
    Menus(MenuID, RestaurantID, MenuName),
    Dishes(DishID, MenuID, DishName, Price),
    Customers(CustomerID, Name, PhoneNumber),
    Orders(OrderID, CustomerID, OrderDate, TotalAmount),
    OrderItems(OrderItemID, OrderID, DishID, Quantity)
    """


    #

    print("Welcome to the Restaurant Management System!")

    #while loop fo the users input
    while True:
        prompt = input("Ask your question (type 'exit' to quit): ")
        if prompt.lower() == 'exit':
            break
        sql_query = generate_sql_from_prompt(prompt, schema_description)
        print(f"Generated SQL: {sql_query}")
        result = execute_query(conn, sql_query)
        print(f"Result: {result}")


    conn.close()

if __name__ == "__main__":
    main()

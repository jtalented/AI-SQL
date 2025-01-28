-- Insert Restaurants
INSERT INTO Restaurants (RestaurantID, Name, Location, CuisineType) VALUES
(1, 'The Gourmet Spot', 'Downtown', 'Italian'),
(2, 'Burger Haven', 'Midtown', 'American'),
(3, 'Sushi Paradise', 'Uptown', 'Japanese');





-- Insert Menus
INSERT INTO Menus (MenuID, RestaurantID, MenuName) VALUES
(1, 1, 'Lunch Menu'),
(2, 1, 'Dinner Menu'),
(3, 2, 'All Day Menu'),
(4, 3, 'Specialty Menu');



-- Insert Dishes
INSERT INTO Dishes (DishID, MenuID, DishName, Price) VALUES
(1, 1, 'Pasta Carbonara', 12.99),
(2, 1, 'Caprese Salad', 8.99),
(3, 2, 'Grilled Salmon', 19.99),
(4, 2, 'Steak Frites', 22.99),
(5, 3, 'Cheeseburger', 9.99),
(6, 3, 'Fries', 3.99),
(7, 4, 'Sushi Platter', 24.99),
(8, 4, 'Tempura Shrimp', 14.99);



-- Insert Customers
INSERT INTO Customers (CustomerID, Name, PhoneNumber) VALUES
(1, 'Alice Johnson', '555-1234'),
(2, 'Bob Smith', '555-5678'),
(3, 'Charlie Brown', '555-8765'),
(4, 'David Lee', '555-4321');



-- Insert orders
INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount) VALUES
(1, 1, '2025-01-15', 38.98),
(2, 2, '2025-01-16', 29.99),
(3, 3, '2025-01-17', 47.98),
(4, 4, '2025-01-18', 39.98);



-- Insert OrderItems
INSERT INTO OrderItems (OrderItemID, OrderID, DishID, Quantity) VALUES
(1, 1, 1, 2),
(2, 1, 2, 1),
(3, 2, 3, 1),
(4, 2, 5, 1),
(5, 3, 6, 1),
(6, 3, 7, 2),
(7, 4, 8, 2);

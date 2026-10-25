# ByteBites models
#
# Customer  - A campus user with a name and a purchase history (list of past
#             Orders). A customer is verified once they have at least one order.
# FoodItem  - A single item for sale, with a name, price, category (plain
#             string, e.g. "Drinks"), and popularity rating.
# Menu      - The full collection of FoodItems; supports adding items and
#             filtering them by category.
# Order     - One transaction grouping the FoodItems a customer picked; starts
#             empty and computes its total cost on demand (not stored).

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


class FoodItem:
    """A single item for sale on the ByteBites menu."""

    def __init__(self, name: str, price: float, category: str, popularity_rating: float) -> None:
        """Create a food item with its name, price, category, and popularity rating (0.0-5.0)."""
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    """The full collection of food items ByteBites sells."""

    def __init__(self) -> None:
        """Create an empty menu."""
        self.items: list[FoodItem] = []

    def add_item(self, item: FoodItem) -> None:
        """Add a food item to the menu."""
        pass

    def filter_by_category(self, category: str) -> list[FoodItem]:
        """Return the menu items whose category exactly matches the given string."""
        pass


class Order:
    """A single transaction grouping the food items a customer picked."""

    def __init__(self) -> None:
        """Create an empty order."""
        self.items: list[FoodItem] = []

    def add_item(self, item: FoodItem) -> None:
        """Add a food item to the order."""
        pass

    def compute_total(self) -> float:
        """Return the sum of item prices, computed each call; 0.0 if the order is empty."""
        pass


class Customer:
    """A campus user who places orders."""

    def __init__(self, name: str) -> None:
        """Create a customer with a name and an empty purchase history."""
        self.name = name
        self.purchase_history: list[Order] = []

    def add_purchase(self, order: Order) -> None:
        """Record a completed order in the customer's purchase history."""
        pass

    def is_verified(self) -> bool:
        """Return True if the customer has at least one past order."""
        pass

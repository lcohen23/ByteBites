# Tests for the ByteBites models.
from models import Customer, FoodItem, Menu, Order


def make_menu() -> Menu:
    """Build a small sample menu used by several tests."""
    menu = Menu()
    menu.add_item(FoodItem("Spicy Burger", 8.50, "Food", 4.5))
    menu.add_item(FoodItem("Large Soda", 2.00, "Drinks", 4.0))
    menu.add_item(FoodItem("Chocolate Cake", 4.25, "Desserts", 4.8))
    menu.add_item(FoodItem("Iced Tea", 1.75, "Drinks", 3.2))
    return menu


# Order totals

def test_calculate_total_with_multiple_items():
    """A $10 burger plus a $5 soda totals $15."""
    order = Order()
    order.add_item(FoodItem("Burger", 10.00, "Food", 4.0))
    order.add_item(FoodItem("Soda", 5.00, "Drinks", 3.5))
    assert order.compute_total() == 15.00


def test_order_total_is_zero_when_empty():
    """An order with no items totals 0.0 instead of crashing."""
    assert Order().compute_total() == 0.0


def test_order_total_counts_duplicate_items():
    """Adding the same $2 soda twice totals $4."""
    soda = FoodItem("Soda", 2.00, "Drinks", 3.5)
    order = Order()
    order.add_item(soda)
    order.add_item(soda)
    assert order.compute_total() == 4.00


def test_order_total_updates_after_adding_item():
    """The total reflects items added after an earlier total was computed."""
    order = Order()
    order.add_item(FoodItem("Burger", 10.00, "Food", 4.0))
    assert order.compute_total() == 10.00
    order.add_item(FoodItem("Soda", 5.00, "Drinks", 3.5))
    assert order.compute_total() == 15.00


# Category filtering

def test_filter_by_category_returns_only_matching_items():
    """Filtering "Drinks" returns only the drink items."""
    drinks = make_menu().filter_by_category("Drinks")
    assert [item.name for item in drinks] == ["Large Soda", "Iced Tea"]


def test_filter_by_category_with_no_matches_returns_empty_list():
    """Filtering a category with no items returns an empty list."""
    assert make_menu().filter_by_category("Pizza") == []


def test_filter_by_category_is_case_sensitive():
    """Filtering "drinks" does not match items in "Drinks"."""
    assert make_menu().filter_by_category("drinks") == []


def test_filter_on_empty_menu_returns_empty_list():
    """Filtering an empty menu returns an empty list."""
    assert Menu().filter_by_category("Drinks") == []


# Sorting

def test_sort_by_popularity_highest_first():
    """Sorted items run from highest to lowest popularity rating."""
    sorted_items = make_menu().sort_by_popularity()
    ratings = [item.popularity_rating for item in sorted_items]
    assert ratings == [4.8, 4.5, 4.0, 3.2]


def test_sort_by_popularity_does_not_change_menu_order():
    """Sorting leaves the menu's own item order unchanged."""
    menu = make_menu()
    menu.sort_by_popularity()
    assert [item.name for item in menu.items] == [
        "Spicy Burger", "Large Soda", "Chocolate Cake", "Iced Tea"
    ]


def test_sort_empty_menu_returns_empty_list():
    """Sorting an empty menu returns an empty list."""
    assert Menu().sort_by_popularity() == []


# Customer verification

def test_new_customer_is_not_verified():
    """A customer with no purchases is not verified."""
    assert not Customer("Ana").is_verified()


def test_customer_is_verified_after_purchase():
    """A customer is verified after one recorded purchase."""
    order = Order()
    order.add_item(FoodItem("Large Soda", 2.00, "Drinks", 4.0))
    customer = Customer("Ana")
    customer.add_purchase(order)
    assert customer.is_verified()

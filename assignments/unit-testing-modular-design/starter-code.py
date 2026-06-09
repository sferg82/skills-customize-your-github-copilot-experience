from typing import Dict, List


def calculate_total(items: List[Dict[str, float]]) -> float:
    """Return the total price for a list of items.

    Each item should contain 'name', 'price', and 'quantity'.
    """
    raise NotImplementedError


def apply_discount(total: float, discount_percent: float) -> float:
    """Return the total after applying a discount percentage."""
    raise NotImplementedError


def format_receipt(customer_name: str, items: List[Dict[str, float]], discount_percent: float = 0) -> str:
    """Return a formatted receipt string for the order."""
    raise NotImplementedError


if __name__ == "__main__":
    sample_items = [
        {"name": "Notebook", "price": 3.50, "quantity": 2},
        {"name": "Pen", "price": 1.20, "quantity": 3},
    ]

    print(format_receipt("Alex", sample_items, discount_percent=10))

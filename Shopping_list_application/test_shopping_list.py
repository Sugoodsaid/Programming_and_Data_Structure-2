# test_functions.py
import unittest
import json
import os
from functions import ShoppingList

class TestShoppingList(unittest.TestCase):

    def setUp(self):
        """Create a ShoppingList instance for testing."""
        self.shopping_list = ShoppingList()

    def test_add_item(self):
        """Test adding an item to the shopping list."""
        self.shopping_list.add_item("Apples")
        self.assertIn("Apples", self.shopping_list.items)

    def test_delete_item(self):
        """Test deleting an item from the shopping list."""
        self.shopping_list.add_item("Bananas")
        self.shopping_list.delete_item("Bananas")
        self.assertNotIn("Bananas", self.shopping_list.items)

    def test_modify_item(self):
        """Test modifying an existing item in the shopping list."""
        self.shopping_list.add_item("Oranges")
        self.shopping_list.modify_item("Oranges", "Grapes")
        self.assertIn("Grapes", self.shopping_list.items)
        self.assertNotIn("Oranges", self.shopping_list.items)

    def test_display_items_empty(self):
        """Test displaying items when the list is empty."""
        # Here we would typically mock messagebox to test this
        # But for simplicity, we will just check the items list
        self.assertEqual(self.shopping_list.items, [])

    def test_save_to_file(self):
        """Test saving the shopping list to a file."""
        self.shopping_list.add_item("Milk")
        self.shopping_list.save_to_file("test_list.json")
        with open("test_list.json", 'r') as f:
            items = json.load(f)
            self.assertIn("Milk", items)

    def test_load_from_file(self):
        """Test loading the shopping list from a file."""
        with open("test_list.json", 'w') as f:
            json.dump(["Eggs", "Bread"], f)
        
        self.shopping_list.load_from_file("test_list.json")
        self.assertIn("Eggs", self.shopping_list.items)
        self.assertIn("Bread", self.shopping_list.items)

    def tearDown(self):
        """Clean up any files created during testing."""
        if os.path.exists("test_list.json"):
            os.remove("test_list.json")

if __name__ == '__main__':
    unittest.main()

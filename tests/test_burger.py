from unittest.mock import Mock
from praktikum.burger import Burger
from data import Data
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        bun = Bun(Data.BLACK_BUN, Data.BLACK_BUN_PRICE)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 100
        mock_ingredient.get_name.return_value = 'cutlet'
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0].get_name() == 'cutlet'
        assert burger.ingredients[0].get_price() == 100
        assert burger.ingredients[0].get_type() == INGREDIENT_TYPE_FILLING

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_get_price(self):
        burger = Burger()
        data = Database()
        burger.set_buns(data.available_buns()[0])
        burger.add_ingredient(data.available_ingredients()[0])
        burger.add_ingredient(data.available_ingredients()[1])
        burger.add_ingredient(data.available_ingredients()[2])
        assert burger.get_price() == 800

    def test_get_receipt(self):
        burger = Burger()
        data = Database()
        burger.set_buns(data.available_buns()[2])
        burger.add_ingredient(data.available_ingredients()[0])
        burger.add_ingredient(data.available_ingredients()[1])
        burger.add_ingredient(data.available_ingredients()[2])
        expected_receipt = '''(==== red bun ====)\n= sauce hot sauce =\n= sauce sour cream =\n= sauce chili sauce =\n(==== red bun ====)\n\nPrice: 1200'''
        assert burger.get_receipt() == expected_receipt

    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient_one = Mock()
        mock_ingredient_one.get_price.return_value = 100
        mock_ingredient_one.get_name.return_value = 'cutlet'
        mock_ingredient_one.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient_two = Mock()
        mock_ingredient_two.get_price.return_value = 300
        mock_ingredient_two.get_name.return_value = 'sausage'
        mock_ingredient_two.get_type.return_value = INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient_one)
        burger.add_ingredient(mock_ingredient_two)
        burger.move_ingredient(0, 1)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_ingredient_two
        assert burger.ingredients[1] == mock_ingredient_one
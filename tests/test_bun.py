from unittest.mock import Mock
from praktikum.burger import Burger
from data import Data
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING


class TestBurger:

    # Тестирование метода set_buns
    def test_set_buns(self):
        # Создаем объект бургера и булки
        burger = Burger()
        bun = Bun(Data.BLACK_BUN, Data.BLACK_BUN_PRICE)

        # Устанавливаем булку для бургера
        burger.set_buns(bun)

        # Проверяем, что булка установлена корректно
        assert burger.bun == bun

    # Тестирование метода add_ingredient
    def test_add_ingredient(self):
        # Создаем объект бургера и мок-ингредиент
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 100
        mock_ingredient.get_name.return_value = 'cutlet'
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING

        # Добавляем ингредиент в бургер
        burger.add_ingredient(mock_ingredient)

        # Проверяем, что ингредиент добавлен корректно
        assert burger.ingredients[0].get_name() == 'cutlet'
        assert burger.ingredients[0].get_price() == 100
        assert burger.ingredients[0].get_type() == INGREDIENT_TYPE_FILLING

    # Тестирование метода remove_ingredient
    def test_remove_ingredient(self):
        # Создаем объект бургера и мок-ингредиент
        burger = Burger()
        mock_ingredient = Mock()

        # Добавляем и удаляем ингредиент
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        # Проверяем, что ингредиент удален
        assert len(burger.ingredients) == 0

    # Тестирование метода get_price
    def test_get_price(self):
        # Создаем объект бургера и базы данных
        burger = Burger()
        data = Database()

        # Устанавливаем булку и добавляем ингредиенты
        burger.set_buns(data.available_buns()[0])
        burger.add_ingredient(data.available_ingredients()[0])
        burger.add_ingredient(data.available_ingredients()[1])
        burger.add_ingredient(data.available_ingredients()[2])

        # Проверяем общую стоимость бургера
        assert burger.get_price() == 800

    # Тестирование метода get_receipt
    def test_get_receipt(self):
        # Создаем объект бургера и базы данных
        burger = Burger()
        data = Database()

        # Устанавливаем булку и добавляем ингредиенты
        burger.set_buns(data.available_buns()[2])
        burger.add_ingredient(data.available_ingredients()[0])
        burger.add_ingredient(data.available_ingredients()[1])
        burger.add_ingredient(data.available_ingredients()[2])

        # Ожидаемый результат чека
        expected_receipt = '''(==== red bun ====)\n= sauce hot sauce =\n= sauce sour cream =\n= sauce chili sauce =\n(==== red bun ====)\n\nPrice: 1200'''

        # Проверяем, что чек сформирован корректно
        assert burger.get_receipt() == expected_receipt

    # Тестирование метода move_ingredient
    def test_move_ingredient(self):
        # Создаем объект бургера и два мок-ингредиента
        burger = Burger()
        mock_ingredient_one = Mock()
        mock_ingredient_one.get_price.return_value = 100
        mock_ingredient_one.get_name.return_value = 'cutlet'
        mock_ingredient_one.get_type.return_value = INGREDIENT_TYPE_FILLING

        mock_ingredient_two = Mock()
        mock_ingredient_two.get_price.return_value = 300
        mock_ingredient_two.get_name.return_value = 'sausage'
        mock_ingredient_two.get_type.return_value = INGREDIENT_TYPE_FILLING

        # Добавляем ингредиенты и перемещаем их
        burger.add_ingredient(mock_ingredient_one)
        burger.add_ingredient(mock_ingredient_two)
        burger.move_ingredient(0, 1)

        # Проверяем, что ингредиенты перемещены корректно
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_ingredient_two
        assert burger.ingredients[1] == mock_ingredient_one
from shopping_cart import ShoppingCart
import pytest

@pytest.fixture
def cart():
    return ShoppingCart(5)

def test_add_item(cart):
    cart.add('apple')
    
    assert cart.size() == 1
    
    
def test_get_item(cart):
    cart.add('apple')
    
    assert 'apple' in cart.get_items()
    
    
def test_over_max_quantity(cart):
    fruits = ['apple', 'orange', 'grapes', 'mango', 'peach']
    for i in range(len(fruits)):
        cart.add(fruits[i])
            
    with pytest.raises(OverflowError):
        cart.add('melon')
        
        
def test_get_total_price(cart):
    cart.add('apple')
    cart.add('melon')
    
    prices = {
        'apple': 4,
        'melon': 7
    }
    
    assert cart.get_total_price(prices) == 11
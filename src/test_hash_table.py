from hash_table import HashTable

def test_equals_returns_true_for_equal_hash_tables():
    hash_table_1 = HashTable()
    hash_table_1.set("a", 10)
    hash_table_1.set("b", 15)

    hash_table_2 = HashTable()
    hash_table_2.set("a", 10)
    hash_table_2.set("b", 15)
    
    assert hash_table_1 == hash_table_2


def test_equals_returns_false_for_not_equal_hash_tables():
    hash_table_1 = HashTable()
    hash_table_1.set("a", 10)
    hash_table_1.set("b", 15)

    hash_table_2 = HashTable()
    hash_table_2.set("a", 10)
    hash_table_2.set("b", 16)
    
    assert hash_table_1 != hash_table_2

def test_set_sets_value_to_hash_table():
    # arrange
    hash_table = HashTable()

    # act
    hash_table.set("a", 10)

    # assert
    hash_table.get("a") == 10

def test_get_gets_value_from_hash_table_by_key():
    # arrange
    hash_table = HashTable()
    hash_table.set("a", 10)
    hash_table.set("b", 15)
    hash_table.set("c", 16)

    # act
    # assert
    hash_table.get("c") == 15
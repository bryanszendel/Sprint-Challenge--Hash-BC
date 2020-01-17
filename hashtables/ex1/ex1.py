#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    if length == 2:
        if weights[0] + weights[1] == limit:
            return [1,0]
        else:
            return None

    for i in range(len(weights)):
        hash_table_insert(ht, weights[i], i)
    
    indices = []
    for weight in weights:
        difference = limit - weight
        index = hash_table_retrieve(ht, difference)
        if index is not None:
            indices.append(index)

    if indices != []:
        return indices
    else:
        return None

# get_indices_of_item_weights(weights=[ 4, 6, 10, 15, 16 ], length=5, limit=21)

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

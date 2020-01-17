#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        

def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = []
    count = 0

    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # city = hash_table_retrieve(hashtable, "FLG")
    # print(city)
    city = hash_table_retrieve(hashtable, "NONE")
    while city != "NONE":
        route.insert(count, city)
        count += 1
        new_city = hash_table_retrieve(hashtable, city)
        city = new_city
    print(route)
    return route

# these_tickets = [
#   Ticket(source="PIT", destination="ORD" ),
#   Ticket(source="XNA", destination="CID" ),
#   Ticket(source="SFO", destination="BHM" ),
#   Ticket(source="FLG", destination="XNA" ),
#   Ticket(source="NONE", destination="LAX"),
#   Ticket(source="LAX", destination="SFO" ),
#   Ticket(source="CID", destination="SLC" ),
#   Ticket(source="ORD", destination="NONE"),
#   Ticket(source="SLC", destination="PIT" ),
#   Ticket(source="BHM", destination="FLG" )
# ]
# reconstruct_trip(these_tickets, 10)
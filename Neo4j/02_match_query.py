# https://neo4j.com/docs/api/python-driver/current/

from neo4j.v1 import GraphDatabase

# Open Neo4j project > on any existing graph, click on Start then Manage button > on Details tab, notice the Bolt port.
uri = "bolt://localhost:11005"
driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))


# Prints the friends of the Person node with the provided name
def print_friends_of(tx, name):
    for record in tx.run("MATCH (a:Person)-[:KNOWS]->(f) "
                         "WHERE a.name = {name} "
                         "RETURN f.name", name=name):
        print(record["f.name"])


# Prints all the friends of Person node named Alice
with driver.session() as session:
    session.read_transaction(print_friends_of, "Alice")

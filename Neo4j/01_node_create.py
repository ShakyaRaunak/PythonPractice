# https://neo4j.com/docs/api/python-driver/current/

# Neo4j Bolt Driver
from neo4j.v1 import GraphDatabase

# Open Neo4j project > on any existing graph, click on Start then Manage button > on Details tab, notice the Bolt port.
uri = "bolt://localhost:11005"
driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))


# Create a new Person node with the provided name
def create_person(tx, name):
    return tx.run("CREATE (a:Person {name:$name}) "
                  "RETURN id(a)", name=name).single().value()


# Create a new Person node named Alice
with driver.session() as session:
    node_id = session.write_transaction(create_person, "Alice")

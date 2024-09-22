import py2neo


graph = py2neo.Graph("bolt://localhost:7687", auth=("neo4j", "pumspums"))

batch_size = 200
total_rows = 1048558  

for start in range(0, total_rows, batch_size):
    query = f"""
    LOAD CSV WITH HEADERS FROM 'file:///psam_ca2.csv' AS row
    WITH row
    SKIP {start} LIMIT {batch_size}
    MATCH (p:Person {{id: toInteger(row.id)}})
    MATCH (s:Sex {{id: toInteger(row.sex_id)}})
    MERGE (p)-[:HAS_SEX]->(s);
    """
    try:
        graph.run(query)
        print(f"Batch {start // batch_size + 1} successfully processed")
    except Exception as e:
        print(f"Error in batch {start // batch_size + 1}: {str(e)}")

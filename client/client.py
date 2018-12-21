import requests

query = """
{
    allCategories{
        name
    }
}
"""
req = requests.post("http://127.0.0.1:8000/graphql", json={'query':query})

if req.status_code == 200:
    print(req.json())
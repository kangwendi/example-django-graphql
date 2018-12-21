require('isomorphic-fetch');

fetch("http://127.0.0.1:8000/graphql",{
    method:'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query: '{ allCategories { name } }' }),
})

.then(res=>res.json())
.then(res=>console.log(res.data));
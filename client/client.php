<?php

//GRAPHQL request
$query = <<<'JSON'
query{
   allCategories {
       name
       ingredients{
           name
       }
   }
}
JSON;
$variables = '';

$json = json_encode(['query' => $query]);

$chObj = curl_init();
curl_setopt($chObj, CURLOPT_URL, "http://127.0.0.1:8000/graphql");
// curl_setopt($chObj, CURLOPT_RETURNTRANSFER, true);    
curl_setopt($chObj, CURLOPT_CUSTOMREQUEST, 'POST');
curl_setopt($chObj, CURLOPT_HEADER, true);
// curl_setopt($chObj, CURLOPT_VERBOSE, true);
curl_setopt($chObj, CURLOPT_POSTFIELDS, $json);
curl_setopt($chObj, CURLOPT_HTTPHEADER,
     array(
            'User-Agent: PHP Script',
            'Content-Type: application/json;charset=utf-8',
            // 'Authorization: bearer '.GITHUB_TOKEN 
        )
    ); 

$response = curl_exec($chObj);
// var_dump($response);
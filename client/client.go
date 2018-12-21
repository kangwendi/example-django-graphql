package main

import (
	"context"
	"fmt"
	"log"

	"github.com/machinebox/graphql"
)

func main() {
	//client
	client := graphql.NewClient("http://127.0.0.1:8000/graphql")
	// defer client.Close()

	//make request to graphql endpoint
	req := graphql.NewRequest(`
		query{
			allCategories {
				name
			}
		}
	`)

	//get result
	var respData map[string]interface{}
	ctx := context.Background()

	if err := client.Run(ctx, req, &respData); err != nil {
		log.Fatal(err)
	}

	fmt.Println(respData)

	// for _, value := range respData {
	// 	fmt.Println(value[0])
	// }
}

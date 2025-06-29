package main

import "fmt"

func main() {

	y := 100

	if y := 20; y > 15 {
		fmt.Println("y is greater than 15")

		fmt.Println("Scope inside is: ", y)
	}

	fmt.Println("Scope outside is: ", y)

}

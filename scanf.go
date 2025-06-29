//Using fmt.Scanf

package main

import "fmt"

func main() {

	var name string
	var age int

	fmt.Print("Ente your name and age: ")
	fmt.Scanf("%s %d", &name, &age)

	fmt.Println("Name:", name)
	fmt.Println("Age:", age)
}

package main

import (
	"fmt"
	"strconv"
)

func main() {
	fmt.Println("Enter the modulus number: ")
	var modulus int
	fmt.Scanln(&modulus)

	fmt.Println("Enter your element value: ")
	var element int
	fmt.Scanln(&element)

	index := 0
	var ai_set []int

	for index < modulus {
		ai_set = append(ai_set, index)
		index += 1
	}

	for number := range ai_set {
		ai := number + element
		if ai%modulus == 0 {
			fmt.Print("Additivie inverse of " + strconv.Itoa(element) + " is " + strconv.Itoa(number))
		}
	}

}

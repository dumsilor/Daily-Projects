package main

import (
	"fmt"
)

func main() {
	fmt.Print("Enther your first number: ")
	var num_a int
	fmt.Scanln(&num_a)

	fmt.Print("Enter your second Number: ")
	var num_b int
	fmt.Scanln(&num_b)

	var reminder int
	var quotient int
	val_a := num_a
	val_b := num_b

	fmt.Print(`
------------------------------------------------
|     q     |     a     |     b     |     r    |
------------------------------------------------
	`)
	for num_b != 0 {
		quotient = num_a / num_b
		reminder = num_a % num_b
		fmt.Printf(`
|     %d     |     %d     |     %d     |     %d    |
----------------------------------------------------
		`, quotient, num_a, num_b, reminder)
		num_a = num_b
		num_b = reminder
	}

	fmt.Printf(`
|     %d     |     %d     |     %d     |     %d    |
----------------------------------------------------
    `, quotient, num_a, num_b, reminder)

	fmt.Printf("gcd(%d,%d)=%d", val_a, val_b, num_a)
}

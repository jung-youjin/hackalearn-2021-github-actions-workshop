package main

import (
	"fmt"
	"os"
)

func main() {
	leader := os.Getenv("INPUT_LEADER")
	member := os.Getenv("INPUT_MEMBER")

	fmt.Println("Hello " + member)
	fmt.Println("Hello " + leader)
}
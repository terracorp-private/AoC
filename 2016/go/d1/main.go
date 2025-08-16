package main

import (
	"fmt"
	"os"
	"strings"

	"gonum.org/v1/gonum/mat"
)

func fileReader(input string) []string {
	fileContent, err := os.ReadFile(input)
	if err != nil {
		fmt.Print(err)
	}
	fileContentStr := string(fileContent)
	fileContentArray := strings.Split((fileContentStr), `, `)
	return fileContentArray
}

func instrunctDecode(instructions []string) {

	rotations := []*mat.Dense{}

	// Initialize matrices for right and left rotation
	rotR := mat.NewDense(2, 2, []float64{
		0, -1,
		1, 0,
	})

	rotL := mat.NewDense(2, 2, []float64{
		0, 1,
		-1, 0,
	})

	// TODO Rotation & Translation Struct

	for _, instruction := range instructions {
		rotationInstruction := instruction[0]
		// rotationInstruction := string(instruction[0])
		translationInstruction := instruction[1:]

		if rotationInstruction == 76 {
			rotations = append(rotations, rotR)
			// fmt.Printf("Type of rotR is: %T\n", rotR)
		} else {
			rotations = append(rotations, rotL)
		}

		fmt.Println(rotationInstruction, translationInstruction)
		fmt.Printf("%v\n", *rotations[0])
	}
}


func rotator() {
	// Take the matrix product of a and b and place the result in c.
	// var c mat.Dense
	// c.Mul(a, b)

	// // Print the result using the formatter.
	// fc := mat.Formatted(&c, mat.Prefix("    "), mat.Squeeze())
	// fmt.Printf("c = %v\n", fc)
}

func main() {

	fl := "./data/input.txt"
	instructionsArray := fileReader(fl)
	instrunctDecode(instructionsArray)

}

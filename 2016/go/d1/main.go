package main

import (
	"fmt"
	"gonum.org/v1/gonum/mat"
	"os"
	"strconv"
	"strings"
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

	const left int = 76
	const right int = 82

	// Initial orientation
	orientation := mat.NewDense(2, 1, []float64{
		0,
		1,
	})

	coordinates := mat.NewDense(2, 1, []float64{
		0,
		0,
	})

	finalCoordinate := mat.NewDense(2, 1, []float64{
		0,
		0,
	})

	// Initialize matrices for right and left rotation
	rotL := mat.NewDense(2, 2, []float64{
		0, -1,
		1, 0,
	})

	rotR := mat.NewDense(2, 2, []float64{
		0, 1,
		-1, 0,
	})

	// Orientaiton after rotation
	for _, instruction := range instructions {
		rotationInstruction := int(instruction[0])
		translationInstruction := strings.TrimSpace("\n" + instruction[1:] + "\n")
		translation, err := strconv.Atoi(translationInstruction)
		if err != nil {
			panic(err)
		}

		if rotationInstruction == right {
			orientation.Mul(rotR, orientation)
			coordinates.Scale(float64(translation), orientation)
		} else if rotationInstruction == left {
			orientation.Mul(rotL, orientation)
			coordinates.Scale(float64(translation), orientation)
		} else {
			fmt.Print("Error in the matrix!")
		}

		finalCoordinate.Add(finalCoordinate, coordinates)
	}
	// Print the result using the formatter.
	fc := mat.Formatted(finalCoordinate, mat.Prefix("    "), mat.Squeeze())
	fmt.Printf("CoordinateInits = %v\n", fc)
}

func main() {

	fl := "./data/input.txt"
	instructionsArray := fileReader(fl)
	instrunctDecode(instructionsArray)

}

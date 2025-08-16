package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {

	var pathToFile string = os.Args[1]
	file, err := os.Open(pathToFile)

	if err != nil {
		panic(err)
	}

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		items := strings.Split(line, ",")
		fmt.Printf("%s\n", items)
	}

}

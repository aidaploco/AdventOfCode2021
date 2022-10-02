package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var LanternFishSchool map[int]int

var SpawnTimers = []int{0, 1, 2, 3, 4, 5, 6, 7, 8}

const MinnowSpawnTimer int = 8
const AdultSpawnTimer int = 6

func readInputFile() {
	fileName := "day6"
	if len(os.Args) > 1 {
		fileName = os.Args[1]
	}
	fmt.Println("Opening ", fileName)
	file, err := os.Open(fileName)
	if err != nil {
		fmt.Println("ERROR")
		fmt.Println(err)
		panic(err)
	}

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		// This loops over the input file per line
		text := scanner.Text()

		// intValue, _ := strconv.Atoi(text)
		for _, data := range strings.Split(strings.TrimSpace(text), ",") {
			startTimer, _ := strconv.Atoi(data)
			LanternFishSchool[startTimer]++
		}
	}
	return

}

func runSimulation(numberOfDays int) (finalCount int) {
	for dayCount := 1; dayCount <= numberOfDays; dayCount++ {
		fmt.Printf("\nDay %d: ", dayCount)
		// Each da
		spawnReset := LanternFishSchool[0]
		for _, timer := range SpawnTimers {
			switch timer {
			case MinnowSpawnTimer:
				LanternFishSchool[timer] = spawnReset
				break
			case AdultSpawnTimer:
				LanternFishSchool[timer] = LanternFishSchool[timer+1] + spawnReset
			default:
				LanternFishSchool[timer] = LanternFishSchool[timer+1]
			}
			fmt.Printf(" %d-%d fish,", timer, LanternFishSchool[timer])
		}
	}
	for _, value := range LanternFishSchool {
		finalCount += value
	}
	return
}

func intializeFishMap() {
	LanternFishSchool = make(map[int]int, 9)
	for _, val := range SpawnTimers {
		LanternFishSchool[val] = 0
	}
}

func main() {
	intializeFishMap()
	readInputFile()
	finalCount := runSimulation(256)
	fmt.Printf("\nFinal count: %d\n", finalCount)
}

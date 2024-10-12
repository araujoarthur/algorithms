package main

import "fmt"

func main() {
	var temp []int = []int{1, 2, 5, 10, 3, 4, 6}
	BubbleSort(temp)
	fmt.Println(temp)
}

func BubbleSort(numbers []int) {
	swapped := true
	for swapped {
		swapped = false
		for i := 0; i <= len(numbers)-2; i++ {
			if numbers[i] > numbers[i+1] {
				Swap(numbers, i)
				swapped = true
			}
		}

	}
}

func Swap(slc []int, idx int) {
	var tmp = slc[idx]
	slc[idx] = slc[idx+1]
	slc[idx+1] = tmp
}

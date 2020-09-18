package main

import "fmt"
import "math"

type Shape interface {
	area() float64
	perimeter() float64
}

type Square struct {
	a float64	
}

type Circle struct {
	r float64	
}

// A struct has to implement both methods of the Shape interface
func (s Square) area() float64 {
	return s.a * s.a	
}

func (s Square) perimeter() float64 {
	return 4 * s.a
}

func (c Circle) area() float64 {
	return c.r * c.r * math.Pi
}

func (c Circle) perimeter() float64 {
	return 2 * math.Pi * c.r
}

func main() {
	fmt.Println("Hello, 世界")
	
	s := Square{a: 5}
	c := Circle{r: 4}
	
	shapes := []Shape{s, c}
	
	for _, s := range shapes {
		fmt.Println("Perimeter:", s.perimeter())
		fmt.Println("Area:", s.area())
	}
}

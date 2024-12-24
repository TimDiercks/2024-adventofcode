package main

import (
	"day23/utils"
	"fmt"
	"strings"
)

const TEST = false

func main() {
	inputFile := "input.txt"
	if TEST {
		inputFile = "test_input.txt"
	}

	connections, err := utils.GetInput(inputFile)
	if err != nil {
		return
	}

	graph := make(utils.Graph)

	for _, connection := range connections {
		for i, connectionNodeA := range connection {
			nodeA := utils.GetNodeOrNew(&graph, connectionNodeA)
			for j, connectionNodeB := range connection {
				if i == j {
					continue
				}
				nodeB := utils.GetNodeOrNew(&graph, connectionNodeB)

				if _, exists := nodeA.Neighbors[nodeB.Value]; exists {
					continue
				}

				nodeA.Neighbors[nodeB.Value] = nodeB
				nodeB.Neighbors[nodeA.Value] = nodeA
			}
		}
	}

	cliques := utils.Find3erCliques(&graph)

	cliquesWithT := 0
	for _, clique := range cliques {
		for _, node := range clique {
			if strings.HasPrefix(node.Value, "t") {
				cliquesWithT += 1
				break
			}
		}
	}

	fmt.Printf("Connection with t: %d\n", cliquesWithT)

	maxCliqueKey, _ := utils.FindMaxClique(&graph, cliques)

	fmt.Printf("Password: %s\n", maxCliqueKey)
}

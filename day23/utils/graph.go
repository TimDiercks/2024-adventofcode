package utils

import (
	"fmt"
	"slices"
	"strings"
)

type Node struct {
	Value     string
	Neighbors map[string]*Node
}

type Graph = map[string]*Node

func GetNodeOrNew(graph *Graph, nodeName string) *Node {
	if node, seen := (*graph)[nodeName]; seen {
		return node
	}

	newNode := &Node{
		Value:     nodeName,
		Neighbors: make(map[string]*Node),
	}
	(*graph)[nodeName] = newNode
	return newNode
}

func Find3erCliques(graph *Graph) map[string][]*Node {
	cliques := make(map[string][]*Node)
	for nodeValue, node := range *graph {
		for _, neighbor := range node.Neighbors {
			for _, neighbor2 := range neighbor.Neighbors {
				if _, hasNeighbor := neighbor2.Neighbors[nodeValue]; !hasNeighbor {
					continue
				}
				nodeNameList := []string{node.Value, neighbor.Value, neighbor2.Value}
				slices.Sort(nodeNameList)
				cliqueString := strings.ReplaceAll(strings.ReplaceAll(strings.ReplaceAll(fmt.Sprint(nodeNameList), " ", ""), "[", ""), "]", "")
				cliques[cliqueString] = []*Node{node, neighbor, neighbor2}
			}
		}
	}

	return cliques
}

func FindMaxClique(graph *Graph, cliques map[string][]*Node) (string, []*Node) {

	for _, node := range *graph {
		for cliqueKey, clique := range cliques {
			isInClique := true
			for _, cliqueNode := range clique {
				if _, exists := node.Neighbors[cliqueNode.Value]; !exists {
					isInClique = false
					break
				}
			}
			if !isInClique {
				continue
			}
			nodeNameList := make([]string, 0)
			clique = append(clique, node)
			for _, cliqueNode := range clique {
				nodeNameList = append(nodeNameList, cliqueNode.Value)
			}
			slices.Sort(nodeNameList)

			cliqueString := strings.ReplaceAll(strings.ReplaceAll(strings.ReplaceAll(fmt.Sprint(nodeNameList), " ", ","), "[", ""), "]", "")
			cliques[cliqueString] = clique
			delete(cliques, cliqueKey)
		}
	}

	maxClique := []*Node{}
	maxCliqueString := ""
	for cliqueKey, clique := range cliques {
		if len(cliqueKey) > len(maxCliqueString) {
			maxClique = clique
			maxCliqueString = cliqueKey
		}
	}

	return maxCliqueString, maxClique
}

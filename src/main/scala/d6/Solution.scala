package d6

import scala.collection.mutable.ListBuffer
import scala.io.Source

object Solution extends Solver with App {
  println("P1: " + solveP1)
  println("P2: " + solveP2)
}

class Node (var parent: String, var children: ListBuffer[String]) {}

trait Solver {
  def checksum(iter: Iterator[String]): Int = {
    var graph = Map[String, ListBuffer[String]]()
    iter.map(x => x.split(')')).foreach(edge => {
      if (graph.contains(edge(0))) graph(edge(0)).append(edge(1))
      else graph += (edge(0) -> ListBuffer(edge(1)))
    })
    traverse(graph, "COM", 0)
  }

  def traverse(graph: Map[String, ListBuffer[String]], node: String, depth: Int): Int = {
    var subsum = 0
    if (graph.contains(node))
      graph(node).foreach(subsum += traverse(graph, _, depth + 1))
    subsum + depth
  }

  def distance(iter: Iterator[String]): Int = {
    var graph = Map("COM" -> new Node("", ListBuffer()))
    iter.map(x => x.split(')')).foreach(edge => {
      var parent = edge(0)
      var child = edge(1)
      if (!graph.contains(parent))
        graph += (parent -> new Node("", ListBuffer()))
      graph(parent).children += child
      if (!graph.contains(child)) {
        graph += (child -> new Node(parent, ListBuffer()))
      }
      else {
        graph(child).parent = parent
      }
    })
    var parent = graph("YOU").parent
    var ancestorsYOU = ListBuffer[String]()
    while (parent != "") {
      ancestorsYOU.prepend(parent)
      parent = graph(parent).parent
    }
    parent = graph("SAN").parent
    var ancestorsSAN = ListBuffer[String]()
    while (parent != "") {
      ancestorsSAN.prepend(parent)
      parent = graph(parent).parent
    }
    ancestorsSAN.length + ancestorsYOU.length - 2 * ancestorsYOU.intersect(ancestorsSAN).length
  }

  def solveP1: String = {
    checksum(Source.fromResource("d6/input").getLines()).toString
  }

  def solveP2: String = {
    distance(Source.fromResource("d6/input").getLines()).toString
  }
}

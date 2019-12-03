package d1

import scala.io.Source

object Solution extends Solver with App {
  println("P1: " + solveP1.toString)
  println("P2: " + solveP2.toString)
}

trait Solver {
  def fuel(x: Int): Int = {
    (x / 3) - 2
  }

  def totalFuel(x: Int): Int = {
    var currentNotCountedFuel = fuel(x)
    var total = currentNotCountedFuel
    while (fuel(currentNotCountedFuel) > 0) {
      currentNotCountedFuel = fuel(currentNotCountedFuel)
      total += currentNotCountedFuel
    }
    total
  }

  def solveP1: Int = {
    Source.fromResource("d1/input").getLines.map(x => x.toInt).map(fuel).sum
  }

  def solveP2: Int = {
    Source.fromResource("d1/input").getLines.map(x => x.toInt).map(totalFuel).sum
  }
}

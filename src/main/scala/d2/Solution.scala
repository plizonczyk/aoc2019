package d2

import scala.io.Source

object Solution extends Solver with App {
  println("P1: " + solveP1)
  println("P2: " + solveP2)
}

trait Solver {
  def opcodeSolver(opcodes: Array[Int]): Array[Int] = {
    var arr = opcodes.clone()
    var i = 0
    while (arr(i) != 99) {
      arr(i) match {
        case 1 => arr(arr(i+3)) = arr(arr(i+1)) + arr(arr(i+2))
        case 2 => arr(arr(i+3)) = arr(arr(i+1)) * arr(arr(i+2))
      }
      i += 4
    }
    arr
  }

  def solveP1: String = {
    var to_transform = Source.fromResource("d2/input").mkString.split(',').map(x => x.toInt)
    to_transform(1) = 12
    to_transform(2) = 2

    opcodeSolver(to_transform)(0).toString
  }

  def solveP2: String = {
    var to_transform = Source.fromResource("d2/input").mkString.split(',').map(x => x.toInt)
    val offset = opcodeSolver(to_transform)(0)

    to_transform(1) = 1
    val first = opcodeSolver(to_transform)(0)

    to_transform(1) = 2
    val second = opcodeSolver(to_transform)(0)

    val magic_number = 19690720
    val diff = second - first
    val noun = (magic_number - offset) / diff
    val verb = magic_number - offset - noun * diff
    (100 * noun + verb).toString
  }
}

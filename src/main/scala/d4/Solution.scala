package d4

import scala.io.Source

object Solution extends Solver with App {
  println("P1: " + solveP1)
  println("P2: " + solveP2)
}

trait Solver {
  def meetsCriteria(num: Int): Boolean = {
    val digits = num.toString.toCharArray.map(_.toInt)
    val nondecreasing = digits.sliding(2).map(x => x(0) <= x(1)).reduceLeft(_ && _)
    val doubleDigit = digits.sliding(2).exists(x => x(0) == x(1))
    nondecreasing && doubleDigit
  }

  def meetsCriteriaP2(num: Int): Boolean = {
    val digits = num.toString.toCharArray.map(_.toInt)
    val nondecreasing = digits.sliding(2).map(x => x(0) <= x(1)).reduceLeft(_ && _)
    val doubleDigits = digits.sliding(2).filter(x => x(0) == x(1)).map(x => x(0)).toArray.
      groupBy(identity).mapValues(_.length).values.exists(_ == 1)
    nondecreasing && doubleDigits
  }

  def solveP1: String = {
    (152085 to 670283).map(meetsCriteria).count(_ == true).toString
  }

  def solveP2: String = {
    (152085 to 670283).map(meetsCriteriaP2).count(_ == true).toString
  }
}

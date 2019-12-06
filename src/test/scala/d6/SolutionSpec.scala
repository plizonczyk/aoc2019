package d6

import org.scalatest._

class SolutionSpec extends FlatSpec with Matchers {
  "Checksum" should "test properly" in {
    Solution.checksum("COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L".lines) shouldEqual 42
  }

  "Distance" should "test properly" in {
    Solution.distance("COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L\nK)YOU\nI)SAN".lines) shouldEqual 4
  }
}

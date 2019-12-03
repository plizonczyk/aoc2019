package d1

import org.scalatest._

class SolutionSpec extends FlatSpec with Matchers {
  "The Solution object" should "calculate fuel properly" in {
    Solution.fuel(12) shouldEqual 2
    Solution.fuel(14) shouldEqual 2
    Solution.fuel(1969) shouldEqual 654
    Solution.fuel(100756) shouldEqual 33583
  }
  "The Solution object" should "calculate total fuel properly" in {
    Solution.totalFuel(14) shouldEqual 2
    Solution.totalFuel(1969) shouldEqual 966
    Solution.totalFuel(100756) shouldEqual 50346
  }
}

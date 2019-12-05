package d4

import org.scalatest._

class SolutionSpec extends FlatSpec with Matchers {
  "MeetsCriteria" should "test properly" in {
    Solution.meetsCriteria(111111) shouldEqual true
    Solution.meetsCriteria(223450) shouldEqual false
    Solution.meetsCriteria(123789) shouldEqual false
  }

  "MeetsCriteriaP2" should "test properly" in {
    Solution.meetsCriteriaP2(112233) shouldEqual true
    Solution.meetsCriteriaP2(123444) shouldEqual false
    Solution.meetsCriteriaP2(111122) shouldEqual true
  }
}

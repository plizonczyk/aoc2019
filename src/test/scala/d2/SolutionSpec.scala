package d2

import org.scalatest._

class SolutionSpec extends FlatSpec with Matchers {
  "The Solution object" should "return rewritten opcodes list" in {
    Solution.opcodeSolver("1,0,0,0,99".split(',').map(x => x.toInt)).mkString(",") shouldEqual "2,0,0,0,99"
    Solution.opcodeSolver("2,3,0,3,99".split(',').map(x => x.toInt)).mkString(",") shouldEqual "2,3,0,6,99"
    Solution.opcodeSolver("2,4,4,5,99,0".split(',').map(x => x.toInt)).mkString(",") shouldEqual "2,4,4,5,99,9801"
    Solution.opcodeSolver("1,1,1,4,99,5,6,0,99".split(',').map(x => x.toInt)).mkString(",") shouldEqual "30,1,1,4,2,5,6,0,99"
  }
}

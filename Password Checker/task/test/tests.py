from hstest import CheckResult, StageTest, dynamic_test, TestedProgram
import hashlib


class StageTest3(StageTest):

    @dynamic_test
    def initial_prompt_test(self):
        main = TestedProgram()
        output = main.start().lower().strip()
        if "enter your password" not in output:
            return CheckResult.wrong("Your program should ask for the user's password.")
        return CheckResult.correct()

    valid_pwds = ["mypassword123", "youcantguessme", "abcdefgh", "validpwd"]

    @dynamic_test(data=valid_pwds)
    def hash_output_test(self, x):
        main = TestedProgram()
        main.start().lower()
        output = main.execute(x).lower().strip()

        expected_hash = hashlib.sha1(x.encode()).hexdigest()

        if expected_hash not in output:
            return CheckResult.wrong("The program should output the hashed password. " +
                                     "Expected: \"" + expected_hash + "\". Got: " + output)
        return CheckResult.correct()


if __name__ == '__main__':
    StageTest3().run_tests()

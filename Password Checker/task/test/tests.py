from hstest import CheckResult, StageTest, dynamic_test, TestedProgram


class StageTest1(StageTest):
    @dynamic_test
    def initial_prompt_test(self):
        main = TestedProgram()
        output = main.start().lower().strip()
        if "enter your password" not in output:
            return CheckResult.wrong("Your program should ask for the user's password.")
        return CheckResult.correct()

    pwds = ["mypassword123", "youcantguessme", "123456", "qwerty", "qwertz"]

    @dynamic_test(data=pwds)
    def input_test(self, x):
        main = TestedProgram()
        output = main.start().lower()
        output2 = main.execute(x)

        if x not in output2:
            return CheckResult.wrong("Your program should display the entered password, " +
                                     "which is: \"" + x + "\". Meanwhile, your output is: " + output2)

        return CheckResult.correct()


if __name__ == '__main__':
    StageTest1().run_tests()

from hstest import CheckResult, StageTest, dynamic_test, TestedProgram


class StageTest2(StageTest):
    @dynamic_test
    def initial_prompt_test(self):
        main = TestedProgram()
        output = main.start().lower().strip()
        if "enter your password" not in output:
            return CheckResult.wrong("Your program should ask for the user's password.")
        return CheckResult.correct()

    valid_pwds = ["mypassword123", "youcantguessme", "abcdefgh", "validpwd"]
    short_pwds = ["123456", "qwerty", "qwertz", "notlong", "short"]

    @dynamic_test(data=valid_pwds)
    def display_pwd_test(self, x):
        main = TestedProgram()
        main.start().lower()
        output2 = main.execute(x)

        if x not in output2:
            return CheckResult.wrong("Your program should display the entered password, " +
                                     "which is: \"" + x + "\". Meanwhile, your output is: " + output2)

        return CheckResult.correct()

    @dynamic_test(data=short_pwds)
    def short_pwd_length_check(self, x):
        main = TestedProgram()
        main.start().lower()
        output = main.execute(x)

        if ("short" not in output) and ("8" not in output):
            return CheckResult.wrong("The program did not warn about a short password.")

        return CheckResult.correct()

    @dynamic_test(data=valid_pwds)
    def valid_pwd_length_check(self, x):
        main = TestedProgram()
        main.start().lower()
        output = main.execute(x)

        if x not in output:
            return CheckResult.wrong("The program did not confirm the valid password.")

        return CheckResult.correct()

    @dynamic_test(data=short_pwds)
    def prompt_again_check(self, x):
        main = TestedProgram()
        main.start().lower()
        output = main.execute(x) #short password is passed
        if "password" not in output:
            return CheckResult.wrong("The program did not ask for the password again " +
                                     "after a short one.")
        elif main.is_finished():
            return CheckResult.wrong("The program finished without asking for a password again " +
                                     "after a short one.")
        return CheckResult.correct()


if __name__ == '__main__':
    StageTest2().run_tests()
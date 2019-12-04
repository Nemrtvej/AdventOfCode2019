class Checker:

    def check_first_version(self, password: str) -> bool:
        if not self._assert_not_decreasing(password):
            return False
        if not self._assert_successing_numbers(password):
            return False

        return True

    def check_second_version(self, password: str) -> bool:
        if not self._assert_not_decreasing(password):
            return False
        if not self._assert_only_two_successing_numbers(password):
            return False

        return True

    def _assert_only_two_successing_numbers(self, password: str):
        subgroups = []
        pointer = 0

        previous_letter = password[0]
        subgroups.append([previous_letter])

        for i in range(1, len(password)):
            current_letter = password[i]
            if current_letter == subgroups[pointer][0]:
                subgroups[pointer].append(current_letter)
            else:
                subgroups.append([current_letter])
                pointer += 1

        for subgroup in subgroups:
            if len(subgroup) == 2:
                return True
        return False

    def _assert_successing_numbers(self, password: str):
        previous_letter = password[0]
        for i in range(1, len(password)):
            current_letter = password[i]
            if previous_letter == current_letter:
                return True
            previous_letter = current_letter

        return False

    def _assert_not_decreasing(self, password):
        previous_letter = password[0]
        for i in range(1, len(password)):
            current_letter = password[i]
            if previous_letter > current_letter:
                return False
            previous_letter = current_letter

        return True


def main_part_1():
    passwords = range(165432, 707913)
    possibilities = 0
    checker = Checker()
    for password in passwords:
        if checker.check_first_version(str(password)):
            possibilities += 1

    print('Number of possibilities: %s' % possibilities)

def main_part_2():
    passwords = range(165432, 707913)
    possibilities = 0
    checker = Checker()
    for password in passwords:
        if checker.check_second_version(str(password)):
            possibilities += 1

    print('Number of possibilities: %s' % possibilities)


if __name__ == '__main__':
    main_part_1()
    main_part_2()
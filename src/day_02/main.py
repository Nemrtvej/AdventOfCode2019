from typing import List, Tuple


class Memory:

    def __init__(self, contents: List[int]):
        self._contents = contents
        self._pointer = 0

    def serialize(self) -> str:
        return ','.join(map(str, self._contents))

    def is_finished(self) -> bool:
        return self._pointer > len(self._contents)

    def get_opcode(self) -> int:
        value = self._contents[self._pointer]
        self._pointer += 4
        return value

    def set_value(self, value, address) -> None:
        self._contents[address] = value

    def get_operands(self) -> Tuple[int, int, int]:
        first_address = self._contents[self._pointer - 3]
        second_address = self._contents[self._pointer - 2]
        target_address = self._contents[self._pointer - 1]

        return self._contents[first_address], self._contents[second_address], target_address

    def get_result(self) -> int:
        return self._contents[0]

    def clone(self) -> "Memory":
        return Memory(self._contents.copy())

    def __repr__(self) -> str:
        return self.serialize()

class Engine:

    def run(self, memory: Memory):
        while not memory.is_finished():
            opcode = memory.get_opcode()
            if opcode == 99:
                return
            elif opcode == 1:
                first_operand, second_operand, target = memory.get_operands()
                memory.set_value(first_operand + second_operand, target)
            elif opcode == 2:
                first_operand, second_operand, target = memory.get_operands()
                memory.set_value(first_operand * second_operand, target)
            else:
                raise ValueError('Unknown opcode: %s' % opcode)

        raise ValueError('Memory did not contain HALT code')



def process_input(input_str: str) -> Memory:
    memory = Memory(list(map(int, input_str.split(','))))
    engine = Engine()
    engine.run(memory)
    return memory


def main_part_1():
    input_str = '1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,6,23,2,13,23,27,1,27,13,31,1,9,31,35,1,35,9,39,' \
                '1,39,5,43,2,6,43,47,1,47,6,51,2,51,9,55,2,55,13,59,1,59,6,63,1,10,63,67,2,67,9,71,2,6,71,75,1,' \
                '75,5,79,2,79,10,83,1,5,83,87,2,9,87,91,1,5,91,95,2,13,95,99,1,99,10,103,1,103,2,107,1,107,6,0,' \
                '99,2,14,0,0'
    print(process_input(input_str).get_result())

def main_part_2():
    default_input = '1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,6,23,2,13,23,27,1,27,13,31,1,9,31,35,1,35,9,39,' \
                    '1,39,5,43,2,6,43,47,1,47,6,51,2,51,9,55,2,55,13,59,1,59,6,63,1,10,63,67,2,67,9,71,2,6,71,75,1,' \
                    '75,5,79,2,79,10,83,1,5,83,87,2,9,87,91,1,5,91,95,2,13,95,99,1,99,10,103,1,103,2,107,1,107,6,0,' \
                    '99,2,14,0,0'
    default_memory = Memory(list(map(int, default_input.split(','))))
    engine = Engine()
    for noun in range(0, 100):
        for verb in range(0, 100):
            try:
                current_memory = default_memory.clone()
                current_memory.set_value(noun, 1)
                current_memory.set_value(verb, 2)

                required_result = 19690720
                engine.run(current_memory)
                if current_memory.get_result() == required_result:
                    print(noun * 100 + verb)
                    return
            except ValueError as e:
                print('Error: %s' % str(e))

if __name__ == '__main__':
    main_part_1()
    main_part_2()
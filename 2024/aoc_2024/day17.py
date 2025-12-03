from dataclasses import dataclass
from enum import Enum, auto
from concurrent.futures import ThreadPoolExecutor
from threading import Event
from typing import List


class Opcode(Enum):
    ADV = 0
    BXL = 1
    BST = 2
    JNZ = 3
    BXC = 4
    OUT = 5
    BDV = 6
    CDV = 7


@dataclass
class ThreeBitVM:
    reg_a: int
    program: List[int]
    reg_b: int = 0
    reg_c: int = 0
    pc: int = 0

    def __str__(self):
        return self._state()

    def _combo_operand_value(self, operand) -> int:
        match operand:
            case 0 | 1 | 2 | 3:
                return operand
            case 4:
                return self.reg_a
            case 5:
                return self.reg_b
            case 6:
                return self.reg_c
            case 7:
                raise "operand 7 is reserved!"
            case _:
                raise f"illegal operand: {operand}"

    def _state(self) -> str:
        return f"a={oct(self.reg_a)}\t{"\t" if self.reg_a < 0o777 else ""}b={oct(self.reg_b)}\t{"\t" if self.reg_b < 0o777 else ""}c={oct(self.reg_c)}\t{"\t" if self.reg_c < 0o777 else ""}pc={self.pc}"

    def _debug(self, opcode, operand) -> str:
        return f"opcode={Opcode(opcode)};operand={operand};value={self._combo_operand_value(operand)}"

    def execute(self) -> List[int]:
        output = []

        while self.pc < len(self.program):
            # print(f"before: {self._state()}")
            (opcode, operand) = self.program[self.pc : self.pc + 2]
            # print(f"operation: {self._debug(opcode, operand)}")

            match opcode:
                case 0:  # ADV
                    self.reg_a //= 2 ** self._combo_operand_value(operand)
                    self.pc += 2
                case 1:  # BXL
                    self.reg_b ^= operand
                    self.pc += 2
                case 2:  # BST
                    self.reg_b = self._combo_operand_value(operand) % 8
                    self.pc += 2
                case 3:  # JNZ
                    self.pc = operand if self.reg_a != 0 else self.pc + 2
                case 4:  # BXC
                    self.reg_b ^= self.reg_c  # operand ignored
                    self.pc += 2
                case 5:  # out
                    output.append(self._combo_operand_value(operand) % 8)
                    self.pc += 2
                case 6:  # bdv
                    self.reg_b = self.reg_a // 2 ** self._combo_operand_value(operand)
                    self.pc += 2
                case 7:  # cdv
                    self.reg_c = self.reg_a // 2 ** self._combo_operand_value(operand)
                    self.pc += 2
                case _:
                    raise f"illegal operand: {opcode}"

            print(self, end="")
            print(f"\toutput: {output}")
            # print()

        return output

    def execute_optimized(self) -> List[int]:
        output = []

        print(self, end="")
        print(f"\tout={output}")

        while self.reg_a != 0:
            self.reg_b = self.reg_a & 7
            print(self, end="")
            print(f"\tout={output}")
            self.reg_b ^= 1
            print(self, end="")
            print(f"\tout={output}")
            self.reg_c = self.reg_a >> self.reg_b
            print(self, end="")
            print(f"\tout={output}")
            self.reg_b ^= 5
            print(self, end="")
            print(f"\tout={output}")
            self.reg_a >>= 3
            print(self, end="")
            print(f"\tout={output}")
            self.reg_b ^= self.reg_c
            print(self, end="")
            print(f"\tout={output}")
            output.append(self.reg_b & 7)
            print(self, end="")
            print(f"\tout={output}")

        return output

    def execute_reverse_optimized(self) -> List[int]:
        pass


if __name__ == "__main__":
    program = [2, 4, 1, 1, 7, 5, 1, 5, 0, 3, 4, 3, 5, 5, 3, 0]

    # part 1
    print(
        ",".join(
            map(
                str,
                ThreeBitVM(
                    reg_a=56256477,
                    program=program,
                ).execute_optimized(),
            )
        )
    )

    # part 2
    # answer_found = Event()

    # def tester(init_a, program, expected_output):
    #     while (
    #         "".join(
    #             map(
    #                 str,
    #                 ThreeBitVM(
    #                     reg_a=init_a,
    #                     program=program,
    #                 ).execute_optimized(),
    #             )
    #         )
    #         != expected_output
    #     ):
    #         if answer_found.is_set():
    #             return

    #         init_a += 12

    #         if (init_a // 12) % 10_000 == 0:
    #             print(f"trying reg_a={init_a}")

    #     print(f"**SOLUTION** {init_a}")
    #     answer_found.set()

    # expected_output = "".join(map(str, program))

    # with ThreadPoolExecutor() as pool:
    #     for n in range(12):
    #         pool.submit(
    #             tester, init_a=n, program=program, expected_output=expected_output
    #         )

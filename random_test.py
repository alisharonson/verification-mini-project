import random
from cpu import SimpleCPU

def random_instruction():
    ops = ["ADD", "SUB"]
    regs = ["R0", "R1", "R2", "R3"]
    return f"{random.choice(ops)} {random.choice(regs)} {random.choice(regs)}"

def run_random_tests(num_tests=100):
    for _ in range(num_tests):
        cpu = SimpleCPU()

        for r in cpu.registers:
            cpu.registers[r] = random.randint(-10, 10)

        expected = cpu.registers.copy()

        instr = random_instruction()

        op, r1, r2 = instr.split()
        if op == "ADD":
            expected[r1] += expected[r2]
        elif op == "SUB":
            expected[r1] -= expected[r2]

        cpu.execute(instr)

        if cpu.registers != expected:
            print("Mismatch found!")
            print("Instruction:", instr)
            print("Expected:", expected)
            print("Got:", cpu.registers)
            return

    print("All random tests passed!")

if __name__ == "__main__":
    run_random_tests()

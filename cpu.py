class SimpleCPU:
    def __init__(self):
        self.registers = {
            "R0": 0,
            "R1": 0,
            "R2": 0,
            "R3": 0
        }

    def execute(self, instruction):
        parts = instruction.split()

        if parts[0] == "ADD":
            r1, r2 = parts[1], parts[2]
            self.registers[r1] += self.registers[r2]

        elif parts[0] == "SUB":
            r1, r2 = parts[1], parts[2]
            self.registers[r1] -= self.registers[r2]

        elif parts[0] == "MOV":
            r, val = parts[1], int(parts[2])
            self.registers[r] = val

        else:
            raise ValueError(f"Unknown instruction: {instruction}")

    def run(self, program):
        for instr in program:
            self.execute(instr)

    def dump(self):
        return self.registers

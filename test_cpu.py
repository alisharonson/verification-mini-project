from cpu import SimpleCPU

def test_add():
    cpu = SimpleCPU()
    cpu.run([
        "MOV R1 5",
        "MOV R2 3",
        "ADD R1 R2"
    ])
    assert cpu.registers["R1"] == 8

def test_sub():
    cpu = SimpleCPU()
    cpu.run([
        "MOV R1 10",
        "MOV R2 4",
        "SUB R1 R2"
    ])
    assert cpu.registers["R1"] == 6

def test_sequence():
    cpu = SimpleCPU()
    cpu.run([
        "MOV R1 2",
        "MOV R2 3",
        "ADD R1 R2",
        "SUB R1 R2"
    ])
    assert cpu.registers["R1"] == 2

if __name__ == "__main__":
    test_add()
    test_sub()
    test_sequence()
    print("All tests passed!")

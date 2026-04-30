## Simple CPU Simulator with Verification

In this project, I tried to implement a minimal CPU simulator in Python, with verification tests and automated test generation. It has:
- 4-register CPU model (R0–R3)
- Basic instruction set: MOV, ADD, SUB
- Deterministic unit tests
- Randomized testing for bug detection

In building this, I wanted to explore hardware design verification concepts, such as instruction correctness and automated test generation.
### How to run:
Run tests: python test_cpu.py <br>
Run random verification: python random_test.py

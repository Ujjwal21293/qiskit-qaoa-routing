# Quantum Routing Optimization with QAOA (Qiskit)

This project uses a **real QAOA quantum circuit** to solve a **pathfinding problem** on a traffic network. It compares multiple route combinations and selects the **minimum-cost path** using **quantum optimization**.

## Features
- Quantum QAOA circuit (parameterized gates)
- QUBO conversion via Docplex
- Histogram of measured bitstrings
- Extendable graph (5 nodes)
- Option to run on IBM Quantum hardware

## Structure
- `src/`: Python files for QUBO modeling and circuit execution
- Graph JSON for traffic simulation

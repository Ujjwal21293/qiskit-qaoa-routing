from qiskit_optimization.translators import from_docplex_mp
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit_algorithms import QAOA
from qiskit.utils import QuantumInstance
from qiskit import Aer, IBMQ
from qiskit_algorithms.optimizers import COBYLA

def run_qaoa_qiskit(model, backend="qasm_simulator", shots=1024, reps=2, real_hw=False):
    qp = from_docplex_mp(model)

    if real_hw:
        IBMQ.load_account()
        provider = IBMQ.get_provider(hub='ibm-q')
        backend = provider.get_backend('ibmq_qasm_simulator')  # or 'ibmq_belem', etc.
    else:
        backend = Aer.get_backend(backend)

    qi = QuantumInstance(backend, shots=shots, seed_simulator=42)
    qaoa = QAOA(optimizer=COBYLA(), reps=reps, quantum_instance=qi)
    optimizer = MinimumEigenOptimizer(qaoa)

    result = optimizer.solve(qp)
    return result, qaoa

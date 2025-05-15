from docplex.mp.model import Model

def build_path_problem():
    mdl = Model("routing_qaoa")

    # Binary vars: x0 = AB, x1 = BC, x2 = CD, x3 = AD, x4 = BD
    x0 = mdl.binary_var(name='x0')
    x1 = mdl.binary_var(name='x1')
    x2 = mdl.binary_var(name='x2')
    x3 = mdl.binary_var(name='x3')
    x4 = mdl.binary_var(name='x4')

    # Minimize total cost
    mdl.minimize(x0*1 + x1*3 + x2*2 + x3*6 + x4*4)

    # Constraint: Choose exactly 3 edges to form path A -> D
    mdl.add_constraint(x0 + x1 + x2 + x3 + x4 == 3)

    return mdl

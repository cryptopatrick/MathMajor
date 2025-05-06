import sympy as sp

# Definiera variabel och ekvation
t = sp.Symbol('t')
x_t = 1 + 4*t
y_t = -1 - 2*t
z_t = 1 + 2*t

# Sätt in i nivåytans ekvation
eq = 2*x_t**2 + y_t**2 + z_t**2 - 4

# Lös för t
solutions = sp.solve(eq, t)

# Hitta den andra punkten P (den som inte är (1, -1, 1))
points = [(x_t.subs(t, sol), y_t.subs(t, sol), z_t.subs(t, sol)) for sol in solutions]
P = [p for p in points if p != (1, -1, 1)][0]

# Beräkna gradienten i P
x0, y0, z0 = P
grad_F_P = (4*x0, 2*y0, 2*z0)

# Ekvation för tangentplanet: F_x(x0) * (x - x0) + F_y(y0) * (y - y0) + F_z(z0) * (z - z0) = 0
x, y, z = sp.symbols('x y z')
tangent_plane_eq = grad_F_P[0] * (x - x0) + grad_F_P[1] * (y - y0) + grad_F_P[2] * (z - z0)

# Visa resultaten
P, tangent_plane_eq.simplify()


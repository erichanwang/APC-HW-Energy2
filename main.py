import mpmath as mp

# constants
m, k, A = 1, 1, 1

# integrand (thing inside integral)
f = lambda x: 1/mp.sqrt(A**4 - x**4)

# integrate from 0 to A
I = mp.quad(f, [0, A])

# period = 4 * sqrt(m/(2k)) * I
tau = 4*mp.sqrt(m/(2*k)) * I

#Period tau = 3.70814935365551
print(f"Period tau = {float(tau):.3f}")

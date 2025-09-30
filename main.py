import math
from scipy.integrate import quad

def period_quartic(m=1.0, Kspring=1.0, A=1.0):
    C = 4.0 * math.sqrt(m / (2.0 * Kspring))

    # inside the integral
    def integrand(dx):
        return 1.0 / math.sqrt(A**4 - dx**4)

    # integrate from 0 to A
    integral_value, error_estimate = quad(integrand, 0.0, A)

    # return period
    return C * integral_value

if __name__ == "__main__":
    period = period_quartic(m=1.0, Kspring=1.0, A=1.0)
    print(f"Period of oscillation (m=1, Kspring=1, A=1): {period:.3f}")

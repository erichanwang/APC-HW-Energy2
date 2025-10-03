(* Constants *)
m = 1;
k = 1;
A = 1;

(* Integrand *)
integrand[x_] := 1 / Sqrt[A^4 - x^4]

(* Compute the integral numerically *)
integral = NIntegrate[integrand[x], {x, 0, A}]

(* Period formula *)
tau = 4 * Sqrt[m / (2 * k)] * integral

(* Print the result *)
Print["Period tau = ", tau]

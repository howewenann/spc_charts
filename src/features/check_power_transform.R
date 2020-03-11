mu = 2
s2 = 2
lambda = 1/3


f <- function(x, lambda){
    return((1 / lambda) * (x^lambda - 1))
}

f1 <- function(x, lambda){
    return(x ^ (lambda - 1))
}


f11 <- function(x, lambda){
    return((lambda - 1) * x ^ (lambda - 2))
}

g <- function(x, lambda){
    return((1 / lambda) * ((x + 1) ^ lambda - 1))
}

g1 <- function(x, lambda){
    return((x + 1) ^ (lambda - 1))
}


g11 <- function(x, lambda){
    return((lambda - 1) * (x + 1) ^ (lambda - 2))
}



E_BC = f(mu, lambda) + f11(mu, lambda)/2 * s2
S_BC = sqrt((f1(mu, lambda))^2 * s2)

CI_BC = c(E_BC - 3*S_BC, E_BC + 3*S_BC)
CI_BC

E_YJ = g(mu, lambda) + g11(mu, lambda)/2 * s2
S_YJ = sqrt((g1(mu, lambda))^2 * s2)

CI_YJ = c(E_YJ - 3*S_YJ, E_YJ + 3*S_YJ)
CI_YJ


# Reverse transform
f_inv = function(x, lambda){
    return((lambda * x + 1)^(1/lambda))
}

g_inv = function(x, lambda){
    return((lambda * x + 1)^(1/lambda) - 1)
}


f_inv(CI_BC, lambda)
g_inv(CI_YJ, lambda)


# Check inverse functions
f(f_inv(CI_BC, lambda), lambda)
CI_BC

g(g_inv(CI_YJ, lambda), lambda)
CI_YJ


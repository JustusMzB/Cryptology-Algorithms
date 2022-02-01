def extended_euclidian(r0, r1, debug = False):
    if(r1 > r0):
        r0, r1 = r1, r0
    qminus1, qminus2 = 1, 0
    pminus1, pminus2 = 0, 1
    rminus1, rminus2 = r1, r0
    if debug:
        print(f'Extended Euklidian gcd. Start: r0 = {r0}, r1={r1}; p0 = {pminus2}, p1 = {pminus1}, q0 = {qminus2}, q1 = {qminus1}')
    i = 2
    while rminus1 != 0:
        d = rminus2 // rminus1
        if debug:
            print(f'\nStep {i}:')
            print(f'\tr{i-2} = r{i-1} * d{i} + r{i}')
        rminus1, rminus2  = rminus2 % rminus1, rminus1
        if debug:
            print(f'\t\t={rminus2} * {d} + {rminus1}')
            print(f'\tq{i} = q{i-2} -d{i} * q{i-1}')
            print(f'\t\t={qminus2} -{d} * {qminus1}')
        qminus1, qminus2 = qminus2 - qminus1*d, qminus1
        if debug:
            print(f'\t\t= {qminus1}')
            print(f'\tp{i} = p{i-2} -d{i} * p{i-1}')
            print(f'\t\t={pminus2} -{d} * {pminus1}')
        pminus1, pminus2 = pminus2 - pminus1*d, pminus1
        if debug:
            print(f'\t\t= {pminus1}')
        i += 1
    if debug:
        print(f'\nGCD = {rminus2} = {pminus2} * {r0} + {qminus2} * {r1}')
    return rminus2, pminus2, qminus2
def modulo_inverse(to_be_inversed:int, modul_number:int, debug:bool = False):
    gcd, potential_inverse, unnecessary = extended_euclidian(to_be_inversed, modul_number, debug=debug)
    if gcd != 1:
        raise ValueError(f'if {to_be_inversed} is supposed to have an inverse by multiplication with modulo {modul_number}, it must have no common divisor except 1. But it has common divisor {gcd}')
    return potential_inverse % modul_number
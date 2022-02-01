def binary_potencing(base:int, exponent:int, modul:int, debug:bool = False):
    """Simulates the binary potencing algorithm

    Args:
        base (int): base of the exponent operation
        exponent (int): exponent
        modul (int): modulo in which all calculations take place
        debug (bool, optional): If enabled, prints steps and intermediate results. Defaults to False.

    Returns:
        int: (base ** exponent) % modul
    """
    def next_factor(prev_factor, modul):
        return prev_factor**2 % modul
    def get_factors(start_factor, modul, amount):
        factors = [start_factor]
        curr_factor = start_factor
        for i in range(0, amount):
            curr_factor = next_factor(curr_factor, modul)
            factors.append(curr_factor)
        return factors

    def get_deltas(number):
        intermed_string = f'{number:b}'
        deltas = [i == '1' for i in intermed_string]
        deltas.reverse()
        return deltas

    string = f'Binary Potencing of {base} to the power of {exponent} to modulo {modul}\n'
    deltas = get_deltas(exponent)
    factors = get_factors(base, modul, len(deltas) + 1)
    string += f'exponent{exponent} = 0 '
    for i, val in enumerate(deltas):
        string += f' + {int(val)} * {2**i}'
    string += '\n'
    x = 1
    string += f'initial: x = 1, factor = {base}\n'
    for index, delta in enumerate(deltas):
        string += f'delta{index} = {int(delta)};\t'
        if delta:
            string += f'x <- {x} * {factors[index]} % {modul} = '
            x = x * factors[index] % modul
            string += f'{x};'
        else:
            string += f'x = {x}\t\t\t'
        string += f'\tfactor <- {factors[index]}² % {modul} = {factors[index+1]}; \n'
    string += f'result: {x}'
    if debug:
        print(string)
    return x
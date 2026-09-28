


def LFSR_step(P, state):
    """
    Input:
        P -- retroaction polynomial of the form 1 + \sum_{i=1}^\ell c_i X^i,
            represented as [c_1, ..., c_ell]
        state -- state at time t: s_n, ... s_{n+ell-1}
        
        Returns the state at time t+1 and the output at time t.
    """

    #TODO
    pass


def LFSR(P, state, N):

    pass
    #TODO


assert LFSR([0,0,1,1], [1,0,1,1], 15) == [1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0]


# helper function for question 6: convert integer to list of bits
def int_to_bits(i, width=8):
    return list([int(c) for c in '{:0{width}b}'.format(i, width=width)])
    
    



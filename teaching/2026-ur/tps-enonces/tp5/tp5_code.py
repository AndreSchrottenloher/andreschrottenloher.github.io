

def int_to_bits(i: int, width: int=8)-> list[int]:
    return list([int(c) for c in '{:0{width}b}'.format(i, width=width)])

def bits_to_int(l: list[int], rev: bool=False) -> int:
    out = 0
    for bit in (reversed(l) if rev else l):
        out = (out << 1) | bit
    return out

def LFSR_step(P: list[int], state: list[int]) -> tuple[int,list[int]]:
    """
    Input:
        P -- retroaction polynomial of the form 1 + \sum_{i=1}^\ell c_i X^i,
            represented as [c_1, ..., c_ell]
        state -- state at time t: s_n, ... s_{n+ell-1}
        
        Returns the state at time t+1 and the output at time t.
    """
    new_bit = 0
    for i in range(len(P)):
        new_bit ^= (P[i] * state[-i-1])
    return state[0], (state[1:] + [new_bit])


def LFSR(P: list[int], state: list[int], N: int) -> list[int]:
    tmp = state[:]
    out = []
    for i in range(N):
        bit, tmp = LFSR_step(P, tmp)
        out.append(bit)
    return out

#=======================================================
# 17-bit LFSR
P1 = [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
# 25-bit LFSR
P2 = [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,1]

#print( LFSR_period(P1, [1] + [0]*16), 2**17-1 )
#print( LFSR_period(P2, [1] + [0]*24), 2**25-1 ) # prend un peu de temps




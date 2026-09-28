# helper function: convert integer to list of bits

def int_to_bits(i, width=8):
    return list([int(c) for c in '{:0{width}b}'.format(i, width=width)])


def LFSR_step(P, state):
    new_bit = 0
    for i in range(len(P)):
        new_bit ^= (P[i] * state[-i-1])
    return state[0], (state[1:] + [new_bit])


def LFSR(P, state, N):
    if len(P) != len(state):
        raise ValueError("Wrong length")
    tmp = state[:]
    out = []
    for i in range(N):
        bit, tmp = LFSR_step(P, tmp)
        out.append(bit)
    return out


def bm( s ):
    # P and Q are represented as a list of coefficients
    P = [1] + [0]*len(s)
    Q = [1] + [0]*len(s)
    Lambda = 0
    m = -1
    dp = 1
    n = len(s)
    
    for t in range(n):
        d = s[t]
        for i in range(1, Lambda+1):
            d ^= P[i] * s[t-i]
        if d != 0:
            T = P[:]
            for i in range(len(P) - (t-m)):
                P[i + t-m] = P[i + t-m] ^ Q[i]
            if 2*Lambda <= t:
                Lambda = t + 1 - Lambda
                m = t
                Q = T
                dp = d
    return P

# -------------------------------------

P1 = [1,0,1,1,0,0,0,0,0,0,0,0,1]
P2 = [0,1,0,0,0,0,0,0,0,0,1]
P3 = [0,0,0,1,0,0,0,0,1]

def geffe(S1, S2, S3, N):
    
    #TODO
    pass

S1 = [1,0,1,0,1,0,1,0,1,0,1,0,1]
S2 = [1,0,1,0,1,0,1,0,1,0,1]
S3 = [1,0,1,0,1,0,1,0,1]

assert geffe(S1, S2, S3, 20) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1]


# -------------------------------------

challenge = [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1,
0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0,
0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0,
1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0,
0, 0, 0, 0, 0, 1, 0, 0, 1, 0]



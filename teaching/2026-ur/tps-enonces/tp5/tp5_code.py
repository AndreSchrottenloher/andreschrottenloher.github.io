import random
random.seed(0)

def int_to_bits(i: int, width: int=8)-> list[int]:
    return list([int(c) for c in '{:0{width}b}'.format(i, width=width)])

def bits_to_int(l: list[int], rev: bool=False) -> int:
    out = 0
    for bit in (reversed(l) if rev else l):
        out = (out << 1) | bit
    return out

def LFSR_step(P: list[int], state: list[int]) -> tuple[int,list[int]]:
    new_bit = 0
    for i in range(len(P)):
        new_bit ^= (P[i] * state[-i-1])
    return state[0], (state[1:] + [new_bit])


def LFSR_multiple_steps(P: list[int], state: list[int], N: int) -> list[int]:
    tmp = state[:]
    out = []
    for i in range(N):
        bit, tmp = LFSR_step(P, tmp)
        out.append(bit)
    return tmp, out

#=======================================================
# 17-bit LFSR
P1 = [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
# 25-bit LFSR
P2 = [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,1]


def css(s: list[int], N: int) -> list[int]:
    s1, s2 =  s[:16] + [1], s[16:] + [1]
    c = 0
    res = []
    for i in range(N):
        s1, bits1 = LFSR_multiple_steps(P1, s1, 8)
        s2, bits2 = LFSR_multiple_steps(P2, s2, 8)
        x = bits_to_int(bits1)
        y = bits_to_int(bits2)
        res.append( (x + y + c) % 256 )
        if x + y > 255:
            c = 1
        else:
            c = 0
    return res

assert css([1]*40,4) == [254, 255, 142, 185]
    

# ------------------ testing for question 2

def generate_s_x_z():
    # Generate a random key
    s = [random.randrange(2) for _ in range(40)]

    # Recompute the first sequence
    s1 = s[:16] + [1]
    x = []
    for i in range(3):
        s1, bits1 = LFSR_multiple_steps(P1, s1, 8)
        x.append( bits_to_int(bits1) )
    z = css(s,3)
    return s,x,z

def compute_initial_state_s2(x: list[int], z: list[int]) -> list[int]:
    """
    x: 3 bytes of output of the LFSR s1
    z: 3 bytes of output of CSS
    Output: the entire initial state s2.
    """
    x1,x2,x3 = tuple(x)
    z1,z2,z3 = tuple(z)

    y1 = (z1-x1) % 256
    c1 = ((x1 + y1) > 255)

    y2 = (z2 - x2 - c1) % 256
    c2 = ((x2 + y2) > 255)

    y3 = (z3 - x3 - c2) % 256
    return int_to_bits(y1) + int_to_bits(y2) + int_to_bits(y3)

# test your code:
s,x,z = generate_s_x_z()
assert compute_initial_state_s2(x,z) == s[16:]



def attack(z: list[int]) -> list[int]:
    """
    z: 5 bytes of the CSS output
    Return: the entire initial state s1.
    """
    #TODO    
    pass

# test your code:
#s = [random.randrange(2) for _ in range(40)]
#z = css(s, 5)
#assert attack(z) == s



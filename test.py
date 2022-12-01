# 2진수 문자열을 10진수로 변환
def Trans_int(Num_2):
    return int("0b"+Num_2, base=2)

# 2진수를 32비트로 확장시키는 함수


def Trans_len32(Num_2,b):
    a = int(b/4)
    return "".join(['0' for x in range(32*a-len(Num_2))])+Num_2

# 확장된 2진수에서 세트 비트와 블럭 비트를 반환하는 함수


def get_Set_Block(Num_2, s, b):
    if b == 1:
        Block_bit = '0'
    else:
        Block_bit = Num_2[-int(math.log2(b)):]
    Set_bit = Num_2[-int(math.log2(s)+math.log2(b)):-int(math.log2(b))]
    if Set_bit == '':
        Set_bit = '0'
    return Set_bit, Block_bit
s = 2
b = 2
b_yte = 2
cach = [[[0 for x in range(b_yte)] for x in range(s)] for x in range(b)]
print(cach)
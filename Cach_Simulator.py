import sys
import math
Total_Load = 0
Total_Store = 0
Load_hit = 0
Load_miss = 0
Store_hit = 0
Store_miss = 0
Total_cycle = 0


# 2진수 문자열을 10진수로 변환
def Trans_int(Num_2):
    return int("0b"+Num_2, base=2)

# 2진수를 32비트로 확장시키는 함수


def Trans_len32(Num_2):
    return "".join(['0' for x in range(32-len(Num_2))])+Num_2

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

# python Cach_Simulator.py 1 1 4 write-allocate write-through lru read01.trace


# [0] = set=1 , [1] = block = 1, [2] = bytes = 4bytes [3] = write-allocate
# [4] = write-through [5] = lru or fifo or random [6] = filename


# args = sys.argv[1:]

# s = int(args[0])
# b = int(args[1])
# size = int(args[2])
# allocate_type = args[3]
# write_type = args[4]
# Out_type = args[5]
# filename = args[6]

filename = "read01.trace"
f = open(filename, "r")
data = f.read().strip()
f.close()

s = 1
b = 1
size = 4

Length = int(math.log4(size))
byte_1 = 2**8

# data에는 리스트 자료형으로 파일 내용이 한줄 씩 들어있다.
# 만약 세트가 1, 블럭이 2, 바이트수가 4바이트 라면

# [세트수][블럭수] 인 2차원 리스트 생성, 0으로 초기화
cach = [[[0 for x in range(Length)] for x in range(s)] for x in range(b)]

# 데이터에는 trace 파일의 모든 줄정보
data = list(data.strip().split("\n"))

for i in data:
    c__ = i.split()
    # Load 인지 Store인지 판단 할 ls 변수
    Ls = c__[0]
    # 2진수가 들어있고 32비트로 확장되어 있는 Adress 변수(0b빠짐)
    Adress = bin(int(c__[1], 16))
    Adress = Trans_len32(Adress[2:])

    # load,store판단후 카운트를 올려줄 부분
    if Ls == "l":
        Total_Load += 1
    else:
        Total_Store += 1

    # set와 block 변수를 이용해 cache 에 맵핑하는 부분
    Set_Bit, Block_Bit = get_Set_Block(Adress, s, b)
    # Hit!
    b_1 = Trans_int(Set_Bit)
    b_2 = Trans_int(Block_Bit)
    if Adress in cach[b_1][b_2]:

        # cache에 자리가 있을때

        # cache에 자리가 없을때

        # Load
        if (Ls == 'l'):
            Load_hit += 1
        # Store
        else:
            Store_hit += 1

    # Miss
    else:
        # cache에 자리가 있을때

        # cache에 자리가 없을때

        # Load
        if (Ls == 'l'):
            Load_miss += 1
        # Store
        else:
            Store_miss += 1

        # Store 중 Miss 났을때 대처

        # Write Allocate 만 구현

        # cache에 바로 넣기만 구현...

        # 마지막 액세스 삭제, 선입 선출, 랜덤 삭제


# 총 출력할 부분
print(Trans_int("".join(['1' for x in range(32)])))
print(int("0xFFFFFFFF",base=16))
print(f"Total loads : {Total_Load}")
print(f"Total store : {Total_Store}")
print(f"Load hits : {Load_hit}")
print(f"Load misses : {Load_miss}")
print(f"Store hits : {Store_hit}")
print(f"Store misses : {Store_miss}")
print(f"Total cycles : {Total_cycle}")

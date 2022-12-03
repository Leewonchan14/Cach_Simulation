import sys
import math
import random
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
# ./csim 256 4 16 write-allocate write-back lru <sometracefile

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
# "C:/Users/twoone14/Desktop/컴구 과제/Cach_Simulation/read01.trace"
filename = 'gcc.trace'
f = open(filename, "r")
data = f.read().strip()
f.close()

s = 4
b = 4
size = 128
allocate_type = "write-allocate"
write_type = "write-through"
Out_type = "random"

Adress_Size = int(size/4)

# data에는 리스트 자료형으로 파일 내용이 한줄 씩 들어있다.
# 만약 세트가 1, 블럭이 2, 바이트수가 4바이트 라면

# [세트수][블럭수][빈리스트] 인 3차원 리스트 생성
cach = [[[] for x in range(b)] for x in range(s)]

# Dirty를 표시할 리스트...
Dirty = []
# fifo를 구현할 리스트...


# 데이터에는 trace 파일의 모든 줄정보
data = list(data.strip().split("\n"))

for i in data:
    c__ = i.split()
    # Load 인지 Store인지 판단 할 ls 변수
    Ls = c__[0]
    # 2진수가 들어있고 32비트로 확장되어 있는 Adress 변수(0b빠짐)
    Adress = bin(int(c__[1], 16))
    Adress = Trans_len32(Adress[2:])

    # set와 block 변수를 이용해 cache 에 맵핑하는 부분
    Set_Bit, Block_Bit = get_Set_Block(Adress, s, b)
    Set_Num = Trans_int(Set_Bit)
    Block_Num = Trans_int(Block_Bit)
    # Hit!
    if Adress in cach[Set_Num][Block_Num]:
        # Load수 올리고 끝
        if (Ls == 'l'):
            Load_hit += 1
            Total_Load += 1
        # Store
        else:
            Store_hit += 1
            Total_Store += 1
            # Store Hits 일때 wirte 타입이 through 라면 캐시와 메모리 동시저장 사이클 +101
            if write_type == "write-through":
                Total_cycle += 100
            # write 타입이 back이라면 일단 캐시저장후 쫒겨날때 메모리 저장 사이클 +100
            elif write_type == "write-back":
                # dirty 표시!!!
                Dirty.append(Adress)
                # 나중에 사이클 +100
        Total_cycle += 1
    # Miss
    else:
        # Load
        if (Ls == 'l'):
            Load_miss += 1
            Total_Load += 1
        # Store
        else:
            Store_miss += 1
            Total_Store += 1
            # Store miss 이면서 allocate type이 write 인 경우
            if allocate_type == "write-allocate":
                Total_cycle += 1
        
        Total_cycle += 100

        # allocate type이 write 인 경우 캐시를 이용해야하므로
        if allocate_type != "no-write-allocate":
            pass

            # cache에 자리가 있을때
            if Adress_Size > len(cach[Set_Num][Block_Num]):
                pass

            # cache에 자리가 없을때
            else:
                # lru 일때
                if Out_type == "lru":
                    pass
                # fifo 일때
                elif Out_type == "fifo":
                    pass
                elif Out_type == "random":
                    pass

            #캐시 저장
            cach[Set_Num][Block_Num].append(Adress)

        # allocate type이 no 인 경우
        elif write_type == "no-write-allocate":
            pass


# 총 출력할 부분
print(f"Total loads : {Total_Load}")
print(f"Total store : {Total_Store}")
print(f"Load hits : {Load_hit}")
print(f"Load misses : {Load_miss}")
print(f"Store hits : {Store_hit}")
print(f"Store misses : {Store_miss}")
print(f"Total cycles : {Total_cycle}")

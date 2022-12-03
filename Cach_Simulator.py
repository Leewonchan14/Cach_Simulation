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
filename = 'read01.trace'
f = open(filename, "r")
data = f.read().strip()
f.close()

s = 1
b = 1
size = 4
allocate_type = ""
write_type = "write-through"
Out_type = "random"

byte_1 = 2**8

# data에는 리스트 자료형으로 파일 내용이 한줄 씩 들어있다.
# 만약 세트가 1, 블럭이 2, 바이트수가 4바이트 라면

# [세트수][블럭수][바이트/4] 인 3차원 리스트 생성, 0으로 초기화
cach = [[[0 for x in range(int(size/4))] for x in range(s)] for x in range(b)]
isCache = [[[False for x in range(int(size/4))] for x in range(s)] for x in range(b)]
#Dirty를 표시할 리스트...
Dirty =[]

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
    Set_Num = Trans_int(Set_Bit)
    Block_Num = Trans_int(Block_Bit)
    if Adress in cach[Set_Num][Block_Num]:
    # Hit!
        # Load
        if (Ls == 'l'):
            Load_hit += 1
            Total_cycle += 1
        # Store
        else:
            Store_hit += 1
            #Store Hits 일때 wirte 타입이 through 라면 캐시와 메모리 동시저장 사이클 +101
            if write_type == "write-through":
                Total_cycle += 101
            #write 타입이 back이라면 일단 캐시저장후 쫒겨날때 메모리 저장 사이클 +100
            elif write_type == "write-back":
                #일단 사이클 +1
                Total_cycle += 1
                #dirty 표시!!!
                Dirty.append(Adress)
                #나중에 사이클 +100
    # Miss
    else:
        # Load
        if (Ls == 'l'):
            Load_miss += 1
        # Store
        else:
            Store_miss += 1
            #Store miss 이면서 allocate type이 write 인 경우 캐시를 이용해야하므로 
            if allocate_type == "write-allocate":
                pass
            #Store miss 이면서 allocate type이 no 인 경우 캐시 이용 안하고 메모리 직접 씀
            else:
                pass
            
        #allocate type이 write 인 경우 캐시를 이용해야하므로 
        if allocate_type == "write-allocate":
            pass
            
            # cache에 자리가 있을때
            if False in isCache[Set_Num][Block_Num]:
                index = 0
                #isCache를 돌다 
                for j in isCache[Set_Num][Block_Num]:
                    #false를 만나면 cach에 넣고 isCache에 True값 넣어서 값이 있음을 알림
                    if not j:
                        cach[Set_Num][Block_Num][index] = Adress
                        isCache[Set_Num][Block_Num][index] = True
                    index += 1  
                    
            
            # cache에 자리가 없을때
            else:
                #lru 일때
                if Out_type == "lru":
                    pass
                #fifo 일때
                elif Out_type == "fifo":
                    pass
                else:
                    pass
        
        
        #allocate type이 no 인 경우
        else:
            pass
            
        
            
            
            
            
            # Store 중 Miss 났을때 대처
            if Ls == 's':
                pass
            pass
            

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

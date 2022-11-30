import sys
Total_Load = 0
Total_Store = 0
Load_hit = 0
Load_miss = 0
Store_hit = 0
Store_miss = 0
Total_cycle = 0
#python Cach_Simulator.py

args = sys.argv[1:]

f = open("read01.trace","r")
data = f.read().strip()
f.close()

#data에는 리스트 자료형으로 파일 내용이 한줄 씩 들어있다.

cach = [[0 for x in range(5)] for i in range(3)]


data = list(data.strip().split("\n"))

for i in data:
    c__ = i.split()
    #Load 인지 Store인지 판단 할 ls 변수
    Ls = c__[0]
    #2진수가 들어있는 Adress 변수
    Adress = bin(int(c__[1], 16))[2:]


    #load,store판단후 카운트를 올려줄 부분
    if Ls == "l":
        Total_Load += 1
    else: Total_Store += 1

    #set와 block 변수를 이용해 cache 에 맵핑하는 부분
    print(Adress)
    


#총 출력할 부분
print(f"Total loads : {Total_Load}")
print(f"Total store : {Total_Store}")
print(f"Load hits : {Load_hit}")
print(f"Load misses : {Load_miss}")
print(f"Store hits : {Store_hit}")
print(f"Store misses : {Store_miss}")
print(f"Total cycles : {Total_cycle}")



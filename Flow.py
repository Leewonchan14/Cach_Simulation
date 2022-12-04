hit했을때 index구해서 리스트 맨뒤로 오게 만들기

#hit 라면
if hit :
    pass
    index = cach[Set_Num][Block_Num].index(Adress)
    #로드 수 올리고 끝
    if load:
        pass
        #load += 1
        #load hit += 1
    # hit인데 store인 경우
    elif store:
        pass
        #store += 1
        #store hit += 1
        # through 경우 캐시와 메모리 같이 저장 사이클 +101
        if through:
            #사이클 +100
            pass
        # back 경우 캐시에만 저장, dirty 표시, 나중에 dirty 수가 캐시에서 지워지면 사이클 +100
        elif back:
            pass
            #Dirty 표시
    #load이든 store이든 through든 back이든 사이클 +1
    ######## lru 라면 순서를 지키기위해 Adress의 index 찾고 뒤로 옮기기
    if out_type == "lru":
        pass
        

#miss 라면  
elif miss:
    pass
    if load:
        pass
        #load miss += 1
        #load += 1
    elif store:
        pass
        #store miss += 1
        #store += 1
        if allocate:
            pass
            #사이클 +1
    #사이클 +100
    #store-noallocate만 아니면 캐시저장을 하기 때문에
    if not (noallocate and store):
        pass

        #꽉 찼을때
        if cacheFull:
            pass
            #내보내는 실행 하기
            if lru or fifo:
                ######맨앞 삭제
                pass
            elif random:
                ######랜덤 삭제
                pass
            #사이클 +1
        #꽉 안찼을때
        elif caheNOTFull:
            pass

        ######캐시 저장 코드 바꾸기(append로 해결)

    elif noallocate:
        pass
        #아무것도 안해도 된다.


def Data_Out(cach,isCache):
    pass
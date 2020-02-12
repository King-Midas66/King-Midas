Min=1
Max=100

ans=int(input())
while True:
    print(Min,"< ? <",Max)
    keyin=int(input())

    if not Min<keyin<Max:
        print("out of range")
        continue
    if keyin>ans:
        Max=keyin
        print("wrong answer, guess smaller")
    elif keyin<ans:
        Min=keyin
        print("wrong answer, guess larger")
    else:
        print('bingo answer is',ans)
        break

def oprn(lst, cmd, *args):
    if cmd == 'remove':
        lst.remove(int(args[0]))
        print(cmd)
    elif cmd == 'discard':
        print(cmd)
        lst.discard(int(args[0]))
    elif cmd == 'pop':
        lst.pop()
    else: 
        print("Command not recognized!")

n = int(input())
s = set(map(int, input().split()))   
for _ in range(int(input())):
    oprn(s, *input().split())
print(sum(s))
n = int(input())
while(n>0):
    n-=1
    output = ""
    for music in input().split(", "):
        output += music[0]
    output += music.split(" i ")[-1][0]
    print(output.replace("Ò", "O").replace("À", "A").replace("Í", "I").replace("Ú", "U"))

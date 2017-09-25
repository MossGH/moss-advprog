def main():
    dic = {}
    dic[1]=10
    dic[2]=20
    dic[3]=30
    print dic
    dic1={1:10, 2:10}
    dic2={3:30, 4:40}
    dic3={5:50, 6:60}
    dic1.update(dic2)
    dic1.update(dic3)
    print dic1
    if input("key") not in dic1:
        print "not in"
    for key in dic1:
        print key
    for key in sorted(dic1.keys()):
        print key, dic1[key]
    dic4={}
    for i in range (1,16):
        dic4[i]=i**2
    print dic4
main()

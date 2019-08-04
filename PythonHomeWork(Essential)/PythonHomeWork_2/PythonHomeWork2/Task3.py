class A(object):
    pass
class B(A):
    pass
class C(A):
    pass
class D (C):
    pass
class E(D,B):
    pass

def main():
    
    print(E.mro())
    print(D.mro())
    print(C.mro())
    print(B.mro())



if __name__ == '__main__':
    main()

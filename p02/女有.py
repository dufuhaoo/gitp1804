class NV(object):
    __aa=None
    __name_a=False
    def __init__(self,name):
        if self.__name_a==False:
            self.name=name
            self.__name_a=True
    def __new__(cls,*k):
        if cls.__aa==None:
            cls.__aa=object.__new__(cls)
        return cls.__aa
nv1=NV('女友1')
print(nv1.name)
nv2=NV('女友2')
print(nv2.name)
print(id(nv1))
print(id(nv2))

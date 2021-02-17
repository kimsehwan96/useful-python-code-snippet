class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        # 유효성 검증 로직 추가
        self._x = value

    @x.deleter
    def x(self):
        del self._x

# 위는 getter, setter, deleter를 각각각 구현한것임.

class D:
    def __init__(self):
        self.y = None
    
# 원래는 d가 D의 인스턴스일경우. d.y 는 getter인것
# d.y = value 인경우 setter
# del d.y 는 deleter 인 경우안데. setter를 쓰는 이유는 값의 유효성 검증을 위한 것임. 따라서..

class E:
    def __init__(self):
        self._z = None
    
    def getz(self):
        return self._z
    
    def setz(self, value):
        # 유효성 검증 로직 추가
        self._z = value
    
    def delz(self):
        del self._z
    
    z = property(getz, setz, delz, "I'm the 'z' property")

# 이렇게 구현하면. e가 E의 인스턴스 일 경우
# e.z 는 게터를 호출
# e.z = value 는 세터를 호출
# del e.z 는 딜리터를 호출한다.

# D 클래스의 경우를 제외하고 C와 E클래스 모두 동일한 동작을 보장한다. 코딩 스타일에 따라서 구현하면 되는듯 !
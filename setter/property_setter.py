class TestClass(object):
    def __init__(self):
        print("instance made.")
        self.output = "this is origin output"
    
    def __str__(self):
        return f'This instance id : {id(self)}'

    @property
    def stdout(self):
        return self.output

    @stdout.setter
    def stdout(self, value):
        print("setter called")
        self.output = value

if __name__ == "__main__":
    tc = TestClass()
    print(tc)
    print(tc.stdout)
    tc.stdout = "this is modified output" #setter를 calling하는 방법. tc.stdout()과 같이 사용하는 것이 아님.
    print(tc.stdout)

# Below Line is console output
'''
instance made.
This instance id : 140397380905936
this is origin output
setter called
this is modified output
'''
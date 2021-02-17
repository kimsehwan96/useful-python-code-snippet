try:
    import msvcrt
    import _winapi
    isWindow = True
except ModuleNotFoundError:
    isWindow = False
    # posix api 등 unix에서 사용할것들을 import
    # ex:
    import _posixsubprocess
    import select

# from python builtin module 'subprocess'
# https://github.com/python/cpython/blob/3.9/Lib/subprocess.py


if __name__ == '__main__':
    print("This machine's os is window") if isWindow else print("This machine's os is not window")

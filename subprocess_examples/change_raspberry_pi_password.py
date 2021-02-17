# This code should be run as root
# 사용자의 어떤 입력도 없이 패스워드를 바꾸기위한 코드 스니펫 

import subprocess
from time import sleep

def change_password(user='pi', password=None) -> None: #return None 인 프로시져
    if not password:
        raise RuntimeError("you should input new password")
    command = ['/usr/bin/passwd', user]
    p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE) # interactive 하지 않은 환경에서 사용하는것을 고려함.
    p.stdin.write('{0}\n{0}\n'.format(password).encode())
    p.stdin.flush() # 표준 입출력 버퍼 flush

    # passwd 프로세스가 완료될때까지 1초정도의 텀을 줌. 이후 해당 프로세스 제거

    for x in range(0, 10):
        if p.poll() is not None:
            break
        sleep(0.1)
    else:
        p.terminate()
        sleep(1)
        p.kill() #passwd 프로세스 kill
        raise RuntimeError('패스워드 설정 실패, passwd 프로세스가 제거되지 않음')
    if p.returncode != 0:
        raise RuntimeError(f'리턴코드가 0이 아닙니다 : 리턴코드 {p.returncode}')
    return


## 라즈베리파이에서 sudo 권한으로 실행해보세요

if __name__ == "__main__":
    change_password(password="raspberry")

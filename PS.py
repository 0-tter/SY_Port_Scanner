import socket
import sys
from queue import Queue
import threading
from datetime import datetime
import os


def clear():
    # 윈도우
    if os.name == 'nt':
        _ = os.system('cls')

    # 맥 or 리눅스
    else:
        _ = os.system('clear')

clear()
#-> 프로그램이 실행될 때마다 터미널을 초기화 시킴.

print('''

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⠽⠭⣥⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠞⠉⠁⠀⠀⠀⠀⠉⠉⠛⠶⣤⣀⠀⠀⢀⣤⠴⠞⠛⠉⠉⠉⠛⠶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠀⠀⠀⠀⠀⠀⢀⣠⠤⠤⠤⠤⢤⣄⡀⠀⠀⠹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠐⠈⠁⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⢤⣽⡦⠐⠒⠒⠂⠀⠀⠀⠀⠐⠒⠀⢿⣦⣀⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡤⠤⠤⠤⠤⠠⠌⢻⣆⡀⠀⠀⠀⣀⣀⣀⡀⠤⠤⠄⠠⢉⣙⡿⣆⡀⠀
⠀⠀⠀⠀⣀⣴⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⢶⣛⣩⣶⣶⡾⢯⠿⠷⣖⣦⣤⣍⣿⣴⠖⣋⠭⣷⣶⣶⡶⠒⠒⣶⣒⣠⣀⣙⣿⣆
⠀⠀⢀⠞⠋⠀⡇⠀⠀⠀⠀⠀⠀⢀⣠⡶⣻⡯⣲⡿⠟⢋⣵⣛⣾⣿⣷⡄⠀⠈⠉⠙⠛⢻⣯⠤⠚⠋⢉⣴⣻⣿⣿⣷⣼⠁⠉⠛⠺⣿
⠀⣠⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣟⣫⣿⠟⠉⠀⠀⣾⣿⣻⣿⣤⣿⣿⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⣿⣿⣻⣿⣼⣿⣿⠇⠀⠀⠀⢙
⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⡶⣄⠀⠀⢻⣿⣿⣿⣿⣿⡏⠀⠀⠀⣀⣤⣾⣁⠀⠀⠀⠸⢿⣿⣿⣿⡿⠋⠀⣀⣠⣶⣿
⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠺⢿⣶⣶⣮⣭⣭⣭⣭⡴⢶⣶⣾⠿⠟⠋⠉⠉⠙⠒⠒⠊⠉⠈⠉⠚⠉⠉⢉⣷⡾⠯
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⢈⣽⠟⠁⠀⠀⠀⠀⣄⡀⠀⠀⠀⠀⠀⠀⢀⣴⡾⠟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡴⠞⠋⠁⠀⠀⠀⠀⠀⠀⠈⠙⢷⡀⠉⠉⠉⠀⠙⢿⣵⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠟⠋⠉⠀⠀⠉⠛⠛⠛⠛⠷⠶⠶⠶⠶⠤⢤⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡤⢿⣆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡶⠋⠀⠀⠀⠸⠿⠛⠛⠛⠓⠒⠲⠶⢤⣤⣄⣀⠀⠀⠀⠈⠙⠛⠛⠛⠛⠒⠶⠶⠶⣶⠖⠛⠛⠁⢠⣸⡟⠀
⠀⠀⠀⠀⠀⠀⢰⣆⠀⢸⣧⣤⣤⣤⣤⣤⣤⣤⣤⣤⣀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠓⠒⠲⠦⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣾⠋⠀⠀
⡀⠀⠀⠀⠀⠀⠀⠙⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠛⠲⠶⣶⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡾⠃⠀⠀⠀
⣿⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠛⠛⣳⣶⡶⠟⠉⠀⠀⠀⠀⠀
⠛⢷⣿⣷⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠙⠻⢷⣬⣗⣒⣂⡀⠠⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣤⡴⠾⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠿⠶⠶⠶⠶⣤⣤⣭⣭⣍⣉⣉⣀⣀⣀⣀⣼⣯⡽⠷⠿⠛⠙⠿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠈⠻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')

print("\nGithub: https://github.com/0-tter\n")
#->아스키 아트와 깃허브 주소

host = socket.gethostbyname(input("웹 사이트의 도메인/아이피를 입력 : ")) #사용자로부터 도메인 주소를 입력받음.
normalPortStart = 1 #기본스캔을 시작범위
normalPortEnd = 1024 #기본스캔의 종료범위
allPort = 1 #고급스캔을 시작범위
allPortEnd = 65535 # 고급스캔을 종료범위
customPortStart = 0 #맞춤형스캔 시작범위
customPortEnd = 0#맞춤형스캔 종료범위

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
#현재시간 캡쳐
print("검색 옵션을 선택하시오.: ")
print("[+] 기본 스캔(1-1024)")
print("[+] 고급 스캔(1-65535)")
print("[+] 맞춤형 스캔")
print("[+] 종료 \n")

mode = int(input("[+] 옵션 선택: "))
print()
# 옵션 선택

if mode == 3:
    customPortStart = int(input("[+] 시작할 포트 : "))
    customPortEnd = int(input("[+] 마지막 포트: "))
#맞춤형 스캔 범위설정
print("-" * 50)
print(f"대상 타겟: {host}")
print("스캔 시작 시간:" + str(datetime.now()))
print("-" * 50)
#스캔정보출력

def scan(port):
    s = socket.socket()
    s.settimeout(5)
    result = s.connect_ex((host, port))
    if result == 0:
        print("포트 오픈", port)
    s.close()
#소켓을 생성 후 타임아웃을 설정한 후 해당 호스트와 포트로 연결을 시도함.
#결과가 0이면 오픈포트로 판단 후 소켓 종료

queue = Queue()
#스레드 간에 포트를 공유하기 위한 큐


def get_ports(mode):
    if mode == 1:
        print("\n[+] 스캔 중..\n")
        for port in range(normalPortStart, normalPortEnd + 1):
            queue.put(port)
    elif mode == 2:
        print("\n[+] 스캔 중..\n")
        for port in range(allPort, allPortEnd + 1):
            queue.put(port)
    elif mode == 3:
        print("\n[+] 스캔 중..\n")
        for port in range(customPortStart, customPortEnd + 1):
            queue.put(port)
    elif mode == 4:
        print("[-] 종료...")
        sys.exit()

#포트를 큐에 추가

open_ports = []
#오픈포트 리스트 생성

def worker():
    while not queue.empty():
        port = queue.get()
        if scan(port):
            print("열려있는 {} 발견 !".format(port))
            open_ports.append(port)

#큐에 포트 번호를 하나씩 가져와서 검색 큐가 비어있을 때까지 반복

def run_scanner(threads, mode):
    get_ports(mode)

    thread_list = []

    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

#스캔속도 향상을 위한 쓰레드활용 병렬스캔 수행


run_scanner(1021, mode)
print(f"스캔 완료 : {current_time}")

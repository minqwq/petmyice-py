import random
import time
import sys
from typing import List

def randint(min_val: int, max_val: int) -> int:
    return random.randint(min_val, max_val)

def choice(options: List[str]) -> str:
    return random.choice(options)

def sleep(seconds: float):
    time.sleep(seconds)

def printa(content: str):
    for char in content:
        print(char, end='', flush=True)
        sleep(0.05)
    print()

class Outice:
    def __init__(self):
        self.blood = 100
        self.count = 0
        self.master = ""
    
    def eat(self):
        add_blood = randint(3, 5)
        self.blood += add_blood
        print(f"{self.master}喂outice吃了点东西。")
        print(f"血量增加{add_blood}点")
        print(f"当前血量: {self.blood}点")
    
    def speak(self, content: str):
        print(f"{self.master}的outice: {content}")
    
    def fuck(self):
        if self.blood <= 5:
            print("血量太低，无法强碱。")
            return
        
        self.count += 1
        load_list = ["\\", "|", "/", "-", "\\", "|", "/", "-"]
        
        for j in range(randint(3, 5)):
            for i in load_list:
                print(f"\r[{i}] 强碱中...", end='', flush=True)
                sleep(0.1)
        
        sub_blood = randint(25, 45)
        bark_list = ["唔", "嗷"]
        print("\r[*] 蛇了！！！")
        sleep(0.25)
        print()
        self.speak(choice(bark_list))
        self.blood -= sub_blood
        sleep(0.25)
        
        if self.blood <= 0:
            print(f"\n{self.master}的outice精尽而亡。")
            sys.exit(0)
        
        print("\n====[结算画面]====")
        print(f"血量减少: {sub_blood}")
        print(f"当前血量: {self.blood}")
        print("==================")
    
    def print_info(self):
        print(f"======[{self.master}的outice]======")
        print(f"血量: {self.blood}")
        print(f"强碱次数: {self.count}")
        print("==================")

def main():
    ice = Outice()
    print("==================")
    print("outice养宠游戏")
    print("by Mitsuki_Ice, Python 3 Ported by minqwq and DeepSeek")
    print("==================")
    ice.master = input("输入你的名字: ")
    age = int(input("输入你的年龄: "))
    
    if age < 18:
        print("未满18岁禁止游玩。")
        sys.exit(0)
    
    ice.print_info()
    print("exit: 退出")
    print("eat: 喂食")
    print("fuck: 强碱")
    print("info: 显示信息\n")
    
    while True:
        cmd = input("> ")
        
        if cmd == "exit":
            exit_choice = input("退出将会失去所有进度，是否退出? \n(输入Y退出，否则不退出)\n输入选择: ")
            if exit_choice == "Y":
                break
        elif cmd == "eat":
            ice.eat()
        elif cmd == "fuck":
            ice.fuck()
        elif cmd == "info":
            ice.print_info()
        elif cmd == "":
            pass
        else:
            print("未知操作。")

if __name__ == "__main__":
    main()
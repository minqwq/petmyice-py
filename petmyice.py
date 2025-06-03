import random
import time
import sys
from colorama import Fore as color
from typing import List

# Global Variables
version = "0.01a"

class logformat:
    agecrk = "[BypassAgeVerifier] "

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
        self.petname = ""
        self.countlevel = 1
    
    def eat(self):
        add_blood = randint(3, 5)
        self.blood += add_blood
        print(f"{self.master}喂" + self.petname +"吃了点东西。")
        print(f"血量增加{add_blood}点")
        print(f"当前血量: {self.blood}点")
    
    def speak(self, content: str):
        print(f"{self.master}的" + self.petname + ": {content}")
    
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
        print(self.petname + " 失去了 " + str(sub_blood) + " 血量。")
        self.exp += randint(75, 450) * self.countlevel / 1.5 * self.sub_blood * randint(1, 1.10)
        print("您的" + self.petname + "得取了" + str(self.exp) + "经验值，距离升级还需  ")
        sleep(0.25)
        
        if self.blood <= 0:
            print(f"\n{self.master}的" + self.petname + "似了。")
            sys.exit(0)
        
        print("\n====[结算画面]====")
        print(f"血量减少: {sub_blood}")
        print(f"当前血量: {self.blood}")
        print("==================")
    
    def print_info(self):
        print(f"======[{self.master}的" + self.petname + "]======")
        print(f"血量: {self.blood}")
        print(f"强碱次数: {self.count}")
        print("==================")

def main():
    ice = Outice()
    print("==================")
    print("outice养宠游戏")
    print("Original Creator: Mitsuki_Ice\nExtended by: minqwq")
    print("版本 " + version)
    print("==================")
    ice.master = input("输入你的名字: ")
    while ice.petname == "":
        ice.petname = input("输入宠物名字(留空则会要求您重新输入): ")
    age = 20
    print(logformat.agecrk + color.GREEN + "年龄验证已破解完成。" + color.RESET)
    
    if age < 18:
        print("未满18岁禁止游玩。")
        sys.exit(0)
    
    ice.print_info()
    print("exit: 退出")
    print("eat: 喂食")
    print("fuck: 强碱")
    print("info: 显示信息\n")
    
    while True:
        try:
            cmd = input("> ")
            
            if cmd == "exit":
                exit_choice = input("警告:没有保存功能插件，您确实要退出吗？？ \n(输入Y退出，否则不退出)\n输入选择: ")
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
        except KeyboardInterrupt:
            print("程序拒绝使用此组合键，请使用exit来退出程序。")

if __name__ == "__main__":
    main()

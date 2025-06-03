import random
import time
import sys
from colorama import Fore as color
from typing import List

# Global Variables
version = "0.01a"

class logformat:
    agecrk = "[BypassAgeVerifier] "
    goldapple = "[EnchantedGoldenApple] "
    diff = "[DifficultyChallange] "

def randint(min_val: int, max_val: int) -> int:
    return random.randint(min_val, max_val)

def choice(options: List[str]) -> str:
    return random.choice(options)

def sleep(seconds: float):
    time.sleep(seconds)

def printa(content: str):
    for char in content:
        print(char, end='', flush=True)
        sleep(0.02)
    print()
    
def flash_screen_ansi(times, delay):
    for _ in range(times):
        # 清除屏幕并设置背景色为白色
        print("\033[2J\033[47m\033[H\a", end="", flush=True)
        print(color.BLACK + "\r[*] 蛇了！！！")
        time.sleep(delay)
        # 清除屏幕并设置背景色为黑色
        print("\033[2J\033[40m\033[H", end="", flush=True)
        time.sleep(delay)
    
    # 重置终端属性
    print("\033[2J\033[0m\033[H", end="", flush=True)

class Outice:
    def __init__(self):
        self.blood = 100
        self.blood_max = 100
        self.count = 0
        self.master = ""
        self.mastervagremain = 50
        self.mastervagpush = 0
        self.master_wgboost = 0
        self.petname = ""
        self.countlevel = 1
        self.exp = 0
        self.countlevel_getup_required_exp = 1000
        self.sub_blood = 0
        self.noflash = ""
        self.difficulty = 0
    
    def chkdiff(self):
        if self.difficulty == 0:
            print("Normal")
        elif self.difficulty == 1:
            print(color.YELLOW + "Hard" + color.RESET)
        elif self.difficulty == 2:
            print(color.RED + "Lunatic" + color.RESET)
    
    def expcr(self):
        expadd = randint(75, 450) * self.countlevel / 2 * self.sub_blood * self.mastervagpush / 310
        if self.difficulty == 0:
            self.exp += expadd
        elif self.difficulty == 1:
            self.exp += expadd / 1.5
            print(logformat.diff + "已经将您的已获得经验除 1.5 倍，下述是您应该会在 Normal 难度下获得的经验值。")
        elif self.difficulty == 2:
            self.exp += expadd / 2
            print(logformat.diff + "已经将您的已获得经验除 2 倍，下述是您应该会在 Normal 难度下获得的经验值。")
        printa("您的" + self.petname + "得取了" + str(round(expadd)) + "经验值，距离升级还需" + str(round(self.countlevel_getup_required_exp - self.exp)))
        if self.exp >= self.countlevel_getup_required_exp:
            self.countlevel += 1
            self.countlevel_getup_required_exp += 1000
            self.blood_max += 100
            self.exp = 0
            print("恭喜您升级了！当前等级 " + str(self.countlevel) + " 。")
        
    def eat(self):
        add_blood = randint(30, 50)
        self.blood += add_blood
        if self.blood >= self.blood_max:
            self.blood = self.blood_max
        printa(f"{self.master}喂" + self.petname +"吃了点东西。")
        print(f"血量增加{add_blood}点")
        print(f"当前血量: {self.blood}点")

    def eatformaster(self):
        selwcone2eat = input("1: 正常吃点\n2: 吃伟哥\n君想食用何物？ > ")
        if selwcone2eat == "1":
            add_blood = randint(10, 40)
            self.mastervagremain += add_blood
            printa(f"{self.master}喂自己吃了点东西。")
            print(f"弹药库增加{add_blood}点")
            print(f"当前自身弹药库内剩余 {self.mastervagremain} 毫升。")
        elif selwcone2eat == "2":
            self.master_wgboost = 3
            printa("食用了伟哥，现在可以避免精尽而亡了。（可持续 3 回。）")
    
    def speak(self, content: str):
        if content == "":
            content = "请输入文本(没在 content 配置找到给予的文本。)"
        print(f"{self.master}的" + self.petname + f": {content}")
    
    def fuck(self):
        if self.blood <= 5:
            print("血量太低，无法强碱。")
            return
        
        self.count += 1
        load_list = ["\\", "|", "/", "-", "\\", "|", "/", "-"]
        
        for j in range(randint(3, 5)):
            for i in load_list:
                print(f"\r[{i}] 做艾中...", end='', flush=True)
                sleep(0.1)
        
        self.sub_blood = randint(25, 45)
        bark_list = ["唔", "嗷"]
        if self.noflash == "":
            for i in range(5):
                print("\r[*] 蛇了！！！")
                time.sleep(0.025)
                flash_screen_ansi(1, 0.1)
                time.sleep(0.025)
        elif self.noflash == "y" or self.noflash == "Y":
            print("\r[*] 蛇了！！！")
        sleep(0.25)
        print()
        self.speak(choice(bark_list))
        self.blood -= self.sub_blood
        if self.master_wgboost >= 1:
            self.master_wgboost -= 1
            self.mastervagpush = randint(5, 20) * 4
            printa("当前处于无限弹药状态并且一次的量已增加 4 倍，伟哥提供的效果还可持续 " + str(self.master_wgboost) + " 回。")
            printa(self.master + "蛇了 " + str(self.mastervagpush) + " ml。")
        elif self.master_wgboost <= 0:
            self.mastervagpush = randint(5, 20)
            self.mastervagremain -= self.mastervagpush
            printa(self.master + "蛇了 " + str(self.mastervagpush) + " ml，还剩 " + str(self.mastervagremain) + " ml。")
        printa(self.petname + " 失去了 " + str(self.sub_blood) + " 血量。")
        self.expcr()
        sleep(0.25)
        
        if self.blood <= 0:
            printa(f"\n{self.master}的" + self.petname + "似了。")
            sys.exit(0)
        elif self.mastervagremain <= 0:
            printa("你精尽而亡，rip。")
            sys.exit(0)
        
        print("\n====[结算画面]====")
        print(f"血量减少: {self.sub_blood}")
        print(f"当前血量: {self.blood}")
        print("==================")
    
    def print_info(self):
        print(f"======[{self.master}的" + self.petname + "]======")
        print(f"难度: ", end="")
        self.chkdiff()
        print(f"级别: {self.countlevel}")
        print(f"血量: {self.blood} / {self.blood_max}")
        print(f"做的次数: {self.count}")
        print("==================")
        print(f"弹药库: {self.mastervagremain} ml")

def main():
    ice = Outice()
    print("==================")
    print("outice养宠游戏")
    print("Original Creator: Mitsuki_Ice\nExtended by: minqwq")
    print("版本 " + version)
    print("==================")
    ice.difficulty = int(input("选择难度\n0:Normal\n1:Hard\n2:Lunatic\n> "))
    ice.master = input("输入你的名字: ")
    while ice.petname == "":
        ice.petname = input("输入宠物名字(留空则会要求您重新输入): ")
    ice.noflash = input("您要启用防闪烁模式吗？(如果你是光敏性癫痫患者的话)[Y/y 启用，其他键不启用]")
    age = 20
    print(logformat.agecrk + color.GREEN + "年龄验证已破解完成。" + color.RESET)
    print(logformat.goldapple + "食物增强已启用。")
    
    if age < 18:
        print("未满18岁禁止游玩。")
        sys.exit(0)
    
    ice.print_info()
    print("exit: 退出")
    print("eat: 喂食")
    print("selfeat: 喂食（给你自己）")
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
            elif cmd == "selfeat":
                ice.eatformaster()
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

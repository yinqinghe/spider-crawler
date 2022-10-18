# class Person(object):
#
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     # 访问器 - getter方法
#     @property
#     def name(self):
#         return self._name
#
#     # 访问器 - getter方法
#     @property
#     def age(self):
#         return self._age
#
#     # 修改器 - setter方法
#     @age.setter
#     def age(self, age):
#         self._age = age
#     # @name.
#     def play(self):
#         if self._age <= 16:
#             print('%s正在玩飞行棋.' % self._name)
#         else:
#             print('%s正在玩斗地主.' % self._name)
#
#
# def main():
#     person = Person('王大锤', 12)
#     person.play()
#     person.age = 22
#     person.play()
#     # person.name = '白元芳'  # AttributeError: can't set attribute
#
#
# if __name__ == '__main__':
#     main()
# print(3//5*4)

# """
# 递归回溯法：叫称为试探法，按选优条件向前搜索，当搜索到某一步，发现原先选择并不优或达不到目标时，就退回一步重新选择，比较经典的问题包括骑士巡逻、八皇后和迷宫寻路等。
# """
# import sys
# import time
#
# SIZE = 5
# total = 0
#
#
# def print_board(board):
#     for row in board:
#         for col in row:
#             print(str(col).center(4), end='')
#         print()
#
#
# def patrol(board, row, col, step=1):
#     if row >= 0 and row < SIZE and col >= 0 and col < SIZE and  board[row][col] == 0:
#         board[row][col] = step
#         # print('------',row,col)
#         if step == SIZE * SIZE:
#             global total
#             total += 1
#             print(f'第{total}种走法: ')
#             print_board(board)
#         patrol(board, row - 2, col - 1, step + 1)
#         patrol(board, row - 1, col - 2, step + 1)
#         patrol(board, row + 1, col - 2, step + 1)
#         patrol(board, row + 2, col - 1, step + 1)
#         patrol(board, row + 2, col + 1, step + 1)
#         patrol(board, row + 1, col + 2, step + 1)
#         patrol(board, row - 1, col + 2, step + 1)
#         patrol(board, row - 2, col + 1, step + 1)
#         board[row][col] = 0
#
#
# def main():
#     board = [[0] * SIZE for _ in range(SIZE)]
#     patrol(board, SIZE - 1, SIZE - 1)
#     # print(board)
#
#
# if __name__ == '__main__':
#     main()

# # 公鸡5元一只 母鸡3元一只 小鸡1元三只
# # 用100元买100只鸡 问公鸡/母鸡/小鸡各多少只
# for x in range(20):
#     for y in range(33):
#         z = 100 - x - y
#         if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
#             print(x, y, z)
#
# # A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
# # 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
# # B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
# # 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼
# fish = 6
# while True:
#     total = fish
#     enough = True
#     for _ in range(5):
#         if (total - 1) % 5 == 0:
#             total = (total - 1) // 5 * 4
#         else:
#             enough = False
#             break
#     if enough:
#         print(fish)
#         break
#     fish += 5

# def main():
#     items = list(map(int, input('请输入：').split()))
#     print(items)
#     overall = partial = items[0]
#     for i in range(1, len(items)):
#         partial = max(items[i], partial + items[i])
#         print(str(partial).center(20,'*'))
#         overall = max(partial, overall)
#         print(overall)
#     print(overall)
#
#
# if __name__ == '__main__':
#     main()

# """
# 贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
# 输入：
# 20 6
# 电脑 200 20
# 收音机 20 4
# 钟 175 10
# 花瓶 50 2
# 书 10 1
# 油画 90 9
# """
# class Thing(object):
#     """物品"""
#
#     def __init__(self, name, price, weight):
#         self.name = name
#         self.price = price
#         self.weight = weight
#
#     @property
#     def value(self):
#         """价格重量比"""
#         return self.price / self.weight
#
#
# def input_thing():
#     """输入物品信息"""
#     name_str, price_str, weight_str = input('请输入：').split()
#     return name_str, int(price_str), int(weight_str)
#
#
# def main():
#     """主函数"""
#     max_weight, num_of_things = map(int, input('请输入：').split())
#     all_things = []
#     for _ in range(num_of_things):
#         all_things.append(Thing(*input_thing()))
#     all_things.sort(key=lambda x: x.value, reverse=True)
#     total_weight = 0
#     total_price = 0
#     for thing in all_things:
#         if total_weight + thing.weight <= max_weight:
#             print(f'小偷拿走了{thing.name}')
#             total_weight += thing.weight
#             total_price += thing.price
#     print(f'总价值: {total_price}美元')
#
#
# if __name__ == '__main__':
#     main()

# """
# 经验：符号常量总是优于字面常量，枚举类型是定义符号常量的最佳选择
# """
# from enum import Enum, unique
#
# import random
#
#
# @unique
# class Suite(Enum):
#     """花色"""
#
#     SPADE, HEART, CLUB, DIAMOND = range(4)
#
#     def __lt__(self, other):
#         # print(self.value)
#         return self.value < other.value
#
#
# class Card():
#     """牌"""
#
#     def __init__(self, suite, face):
#         """初始化方法"""
#         self.suite = suite
#         self.face = face
#
#     def show(self):
#         """显示牌面"""
#         suites = ['♠︎', '♥︎', '♣︎', '♦︎']
#         faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
#         return f'{suites[self.suite.value]}{faces[self.face]}'
#
#     def __repr__(self):
#         return self.show()
#
#
# class Poker():
#     """扑克"""
#
#     def __init__(self):
#         self.index = 0
#         self.cards = [Card(suite, face)
#                       for suite in Suite
#                       for face in range(1, 14)]
#         print(self.cards)
#     def shuffle(self):
#         """洗牌（随机乱序）"""
#         random.shuffle(self.cards)
#         self.index = 0
#
#     def deal(self):
#         """发牌"""
#         card = self.cards[self.index]
#         self.index += 1
#         return card
#
#     @property
#     def has_more(self):
#         return self.index < len(self.cards)
#
#
# class Player():
#     """玩家"""
#
#     def __init__(self, name):
#         self.name = name
#         self.cards = []
#
#     def get_one(self, card):
#         """摸一张牌"""
#         self.cards.append(card)
#
#     def sort(self, comp=lambda card: (card.suite, card.face)):
#         """整理手上的牌"""
#         self.cards.sort(key=comp)
#
#
# def main():
#     """主函数"""
#     poker = Poker()
#     poker.shuffle()
#     players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
#     while poker.has_more:
#         for player in players:
#                 player.get_one(poker.deal())
#     for player in players:
#         player.sort()
#         print(player.name, end=': ')
#         print(player.cards)
#
# if __name__ == '__main__':
#     main()
# def calc_avg():
#     """流式计算平均值"""
#     total, counter = 0, 0
#     avg_value = None
#     while True:
#         value = yield avg_value
#         total, counter = total + value, counter + 1
#         avg_value = total / counter
#
#
# gen = calc_avg()
# next(gen)
# print(gen.send(100))
# print(gen.send(200))
# print(gen.send(30))

class A:
    def test(self):
        print('A')

class B:
    def test(self):
        print('B')

class C(A,B):
    def __init__(self):
        super().test()
        super(C, self).test()
        super(A, self).test()
        super(B, self).test()


C()
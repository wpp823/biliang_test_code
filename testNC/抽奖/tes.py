import random


def raffle(award, total):
    total_list = list(range(0, total))
    # while len(total_list) > 0:
    # 奖品总数
    luck_award_data = {}
    this_num = random.choice(total_list)
    # print(f"抽奖号码{this_num}")
    # 生成奖品幸运号码组
    for key, value in award.items():
        # 抽奖号码
        if value > 0:
            temp_total_list = list(range(0, total))
            # 中奖号码组
            award_luck_nums = random.sample(temp_total_list, k=value)
            luck_award_data[key] = award_luck_nums
            # 移除已经选中的数
            for i in award_luck_nums:
                temp_total_list.remove(i)

            if this_num in award_luck_nums:
                award[key] -= 1
                # 中奖,返回奖品等级
                return key
                # print(f"中奖 {key} 奖品剩余 [{award}] 剩余奖池 {len(total_list)}")
                # break
    return "未中奖"

    # total_list.remove(this_num)
    # # 依次遍历查看是否中奖
    # for key, value in luck_award_data.items():

    # print(f"未中奖 奖品剩余 [{award}] 剩余奖池 {len(total_list)}")
    # return award, total


award_0_num = 1
award_1_num = 2
award_2_num = 5
award_3_num = 10
award_4_num = 100
award_5_num = 500
total_num = 4000
award_data = {
    "award_0_num": award_0_num,
    "award_1_num": award_1_num,
    "award_2_num": award_2_num,
    "award_3_num": award_3_num,
    "award_4_num": award_4_num,
    "award_5_num": award_5_num
}
for i in range(total_num):
    raffle_result = raffle(award_data, total_num)
    print(f"{raffle_result} == {total_num}")
    total_num -= 1

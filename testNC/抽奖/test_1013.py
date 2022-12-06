import random


def test():
    total_num = 4000
    award_0_num = 1
    award_1_num = 2
    award_2_num = 5
    award_3_num = 10
    award_4_num = 100
    award_5_num = 500
    # award_data = self.redis.get()
    award_data = {
        0: award_0_num,
        1: award_1_num,
        2: award_2_num,
        3: award_3_num,
        4: award_4_num,
        5: award_5_num,
    }
    while total_num:
        is_ok = False
        award_list = (award_0_num, award_1_num, award_2_num, award_3_num, award_4_num, award_5_num)
        fail_award_num = 99

        total_list = list(range(0, total_num))

        # 抽奖号码
        this_num = random.choice(total_list)
        total_num -= 1
        for award_id in award_list:
            award_num = award_data.get(award_list.index(award_id))
            if award_num > 0:
                if this_num < award_id:
                    award_data[award_list.index(award_id)] -= 1
                    print(f"抽奖号码:{this_num} 中奖:{award_list.index(award_id)} 总抽奖次数 {total_num}")
                    is_ok=True
                    break
        if not is_ok:
            print(f"抽奖号码:{this_num} 未中奖 {fail_award_num} 总抽奖次数 {total_num}")




if __name__ == '__main__':
    test()
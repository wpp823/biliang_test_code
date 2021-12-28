# 签到任务
SIGN_IN_COIN = {}
COIN_SIGN_IN_CONFIG = []

# 计时任务
TIMING_COIN = {}

for i in range(31):
    day = i + 1
    if day < 7:
        coin = 300
    elif day == 7:
        coin = 1688
    elif day < 14:
        coin = 350
    elif day == 14:
        coin = 2388
    elif day < 21:
        coin = 400
    elif day == 21:
        coin = 3388
    elif day < 30:
        coin = 450
    elif day == 30:
        coin = 4388
    else:
        coin = 500

    SIGN_IN_COIN[day] = coin
    COIN_SIGN_IN_CONFIG.append({
        "day": day,
        "coin": coin,
    })


print(COIN_SIGN_IN_CONFIG)
import time


class class2:

    def func(self):
        time.sleep(0.5)

        print("class2_func")


class demo:
    async def func1(self):
        result = await self.sync_jindie_sal_in_bound_order()

        print(f"func1:result{result}")

    async def sync_jindie_sal_in_bound_order(self):
        print("sync_jindie_sal_in_bound_order")

        obj = class2()
        obj.func()

        return "ok"


if __name__ == "__main__":
    d_1 = demo()
    d_1.func1()

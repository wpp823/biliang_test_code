

import asyncio
import time
from bs4 import BeautifulSoup
from pyppeteer import launch



async def taobao_login(username, password, url):
    """
    淘宝登录主程序
    :param username: 用户名
    :param password: 密码
    :param url: 登录网址
    :return: 登录cookies
    """
    ###
    browser = await launch(headless=False, dumpio=True, autoClose=False, userDataDir='./userdata',
                           args=['--no-sandbox', '--window-size=1920,1080', '--disable-infobars'])  # 进入有头模式
    page = await browser.newPage()  # 打开新的标签页
    await page.setViewport({'width': 1920, 'height': 1080})  # 页面大小一致
    await page.goto(url)  # 访问主页

    await page.click('#J_QRCodeLogin > div.login-links > a.forget-pwd.J_Quick2Static')
    page.mouse
    time.sleep(1)
    # 输入用户名，密码
    await page.type('#TPL_username_1', username, {'delay':120})   # delay是限制输入的时间
    await page.type('#TPL_password_1', password, {'delay': 120})
    time.sleep(2)
    # 检测页面是否有滑块。原理是检测页面元素。
    slider = await page.Jeval('#nocaptcha', 'node => node.style')  # 是否有滑块

    if slider:
        print('当前页面出现滑块')
        # await page.screenshot({'path': './headless-login-slide.png'}) # 截图测试
        flag, page = await mouse_slide(page=page)  # js拉动滑块过去。
        if flag:
            await page.keyboard.press('Enter')  # 确保内容输入完毕，少数页面会自动完成按钮点击
            print("print enter", flag)
            await page.evaluate('''document.getElementById("J_SubmitStatic").click()''')  # 如果无法通过回车键完成点击，就调用js模拟点击登录按钮。
            time.sleep(2)
            cookies_list = await page.cookies()
            print(cookies_list)
            return await get_cookie(page)  # 导出cookie 完成登陆后就可以拿着cookie玩各种各样的事情了。
    else:
        print("")
        await page.keyboard.press('Enter')
        print("print enter")
        await page.evaluate('''document.getElementById("J_SubmitStatic").click()''')
        await page.waitFor(20)
        await page.waitForNavigation()

        try:
            global error  # 检测是否是账号密码错误
            print("error_1:", error)
            error = await page.Jeval('.error', 'node => node.textContent')
            print("error_2:", error)
        except Exception as e:
            error = None
        finally:
            if error:
                print('确保账户安全重新入输入')
                # 程序退出。
                loop.close()
            else:
                print(page.url)
                return await get_cookie(page)

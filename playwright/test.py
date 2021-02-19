# author:丑牛
# datetime:2020/12/22 11:16
from playwright import sync_playwright


def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.newContext()

    # Open new page
    page = context.newPage()

    # Go to http://login.cloud.zhengmeiji.com.cn:81/index.html
    page.goto("http://login.cloud.zhengmeiji.com.cn:81/index.html")

    # Click //span
    page.click("//span")

    # Click text="郑煤机用户"
    page.click("text=\"郑煤机用户\"")

    # Click //div[normalize-space(.)='用户名']/input[normalize-space(@type)='text']
    page.click("//div[normalize-space(.)='用户名']/input[normalize-space(@type)='text']")

    # Fill //div[normalize-space(.)='用户名']/input[normalize-space(@type)='text']
    page.fill("//div[normalize-space(.)='用户名']/input[normalize-space(@type)='text']",
              "wangzhaoxian")

    # Fill input[type="password"]
    page.fill("input[type=\"password\"]", "wzx670905")

    # Go to http://login.cloud.zhengmeiji.com.cn:81/page.html
    page.click("//button")
    # page.goto("http://login.cloud.zhengmeiji.com.cn:81/page.html")

    # Click div[aria-label="Next slide"]
    page.click("div[aria-label=\"Next slide\"]")

    # Click div[aria-label="Next slide"]
    page.click("div[aria-label=\"Next slide\"]")

    # Click //div[normalize-space(@aria-label)='16 / 19' and normalize-space(@role)='group']/div[normalize-space(.)='河南能源 2个子公司']
    # with page.expect_navigation(url="http://safetyui.cloud.zhengmeiji.com.cn:81/#/mainPage/autoSystem/equipmentMonitoring"):
    with page.expect_navigation():
        page.click(
            "//div[normalize-space(@aria-label)='16 / 19' and normalize-space(@role)='group']/div[normalize-space(.)='河南能源 2个子公司']")

    # Close page
    # page.close()
    # ---------------------
    # context.close()
    # browser.close()


with sync_playwright() as playwright:
    run(playwright)

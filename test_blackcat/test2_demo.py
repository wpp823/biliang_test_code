from PIL import Image


def circle():
    ima = Image.open("header.png").convert("RGBA")
    size = ima.size
    # 因为是要圆形，所以需要正方形的图片
    r2 = min(size[0], size[1])
    if size[0] != size[1]:
        ima = ima.resize((r2, r2), Image.ANTIALIAS)
    imb = Image.new('RGBA', (r2, r2), (255, 255, 255, 0))
    pima = ima.load()
    pimb = imb.load()
    r = float(r2 / 2)  # 圆心横坐标
    for i in range(r2):
        for j in range(r2):
            lx = abs(i - r + 0.5)  # 到圆心距离的横坐标
            ly = abs(j - r + 0.5)  # 到圆心距离的纵坐标
            l = pow(lx, 2) + pow(ly, 2)
            if l <= pow(r, 2):
                pimb[i, j] = pima[i, j]

    imb.save("test_circle.png")



def circle1():
    ima = Image.open("test_circle.png").convert("RGBA")
    size = ima.size
    # 因为是要圆形，所以需要正方形的图片
    r2 = min(size[0], size[1])
    if size[0] != size[1]:
        ima = ima.resize((r2, r2), Image.ANTIALIAS)

    pima = ima.load()
    r = float(r2 / 2)  # 圆心横坐标
    print(r)
    for i in range(r2):
        for j in range(r2):
            # print(pimb[i, j])
            lx = abs(i - r)  # 到圆心距离的横坐标
            ly = abs(j - r)  # 到圆心距离的纵坐标
            l = pow(lx, 2) + pow(ly, 2)
            # print(pima[i, j])
            if pow(r, 2) >= l > pow(r - 8, 2):
                # print(pima[i, j])
                pima[i, j] = (255, 255, 255, 255)
    ima.save("test_circle1.png")


circle()
circle1()

import random


def package():
    x = random.randint(1, 5)
    y = random.randint(1, 5)
    z = random.randint(1, 5)
    return x*y*z


class Road():

    def __init__(self, x):
        self.packages_on_road = 0
        self.total = x
        self.packages = []

    def add_package(self, pack):
        if self.packages_on_road < self.total:
            self.packages_on_road += 1
            self.packages.append(pack)

    def remove_package(self):
        if self.packages_on_road > 0:
            self.packages_on_road -= 1
            return self.packages.pop(0)

    def get_packages_quantity(self):
        return self.packages_on_road

    def get_packages_tab(self):
        return self.packages

    def get_info_about_current_pack(self):
        try:
            tmp = self.packages[0]
        except IndexError:
            return None
        return self.packages[0]


def create_and_set_global_road(x):
    globalroad = Road(x)
    for i in range(x):
        globalroad.add_package(package())
    return globalroad

n = 4800

road1 = Road(n)  # small priority
road2 = Road(n)  # medium priority
road3 = Road(n)  # large priority

globalroad = create_and_set_global_road(n)


courier = 0


for i in range(n):
    actual_pack = globalroad.remove_package()

    if actual_pack >= 0 and actual_pack <= 20:
        road1.add_package(actual_pack)
        #print('dodaje 1',actual_pack)
    elif actual_pack >= 21 and actual_pack <= 49:
        road2.add_package(actual_pack)
        #print('dodaje 2',actual_pack)
    else:
        road3.add_package(actual_pack)
        #print('dodaje 3',actual_pack)


for i in range(int(n/6)):
    pack_tab = []
    for i in range(3):
        if road1.get_info_about_current_pack() == None:
            break
        pack_tab.append(road1.remove_package())

    for i in range(2):
        if road2.get_info_about_current_pack() == None:
            break
        pack_tab.append(road2.remove_package())

    for i in range(1):
        if road3.get_info_about_current_pack() == None:
            break
        pack_tab.append(road3.remove_package())

    if courier + sum(pack_tab) > 900:
        print('Kurier wysłany!', 'Kurier przyjął: ', courier,'j')
        courier = 0
    courier += sum(pack_tab)


def big():
    def small():
        print("Hay guys!")
    return small


def out(msg):
    def inn():
        print(f"hay this is {msg}")
    return inn()


boo=big()
boo()


poo=out("ashik")
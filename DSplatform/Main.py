import mode as md

def distinguish(modeSelect, modeInfo):
    for index, value in enumerate(modeInfo):
        if (index == modeSelect - 1) : return value


md.Welcome.start()






# # start screen should be modified.
# modeSelect = int(input(startScreen))

# modeInfo = ["g", "f", "a"]









# modeInfo = [{""
# "name" : "gathering",
# "mode" : [{
# "name" : "survey",
# "mode" : []
# }, {"n" : "dsfg",
# "mode" : []}]
# }, "frm", "Anz"]




# g = mode("Gathering", ["Direct Input", "New Survey"])
#
# distinguish(modeSelect,modeInfo)
#
#
# modeScreen = """
# ==You have selected {}"==
# 1.
# 2/3245
# 2113qwer
#
# Select Mode :"""
# print(modeScreen.format((distinguish(modeSelect,modeInfo))))
# print("Select Mode:".format)

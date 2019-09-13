import pytesseract
import random

from gym_pc.envs import LinuxEnv

if __name__ == '__main__':
    env = LinuxEnv()
    while True:
        action = random.choice(["test", "asdf"])
        img, reward, _, _ = env.step(action)
        # env.render()
        wrd = pytesseract.image_to_string(img, lang="eng", config="--psm 4 --oem 3 -c tessedit_char_whitelist=command")
        print('Action: ' + action + ', Reward: ' + str(reward))

# import pytesseract
# import unicodedata
# from PIL import Image
# 
# #...
# img = Image.open('test5.png')
# wrd = pytesseract.image_to_string(img, lang="eng", config="--psm 4 --oem 3 -c tessedit_char_whitelist=command")
# #img.show()
# #print(wrd)
# normwrd = unicodedata.normalize('NFKD', wrd).encode('ascii','ignore')
# #print(normwrd)
# wrdlst= normwrd.split(" ")
# #print(type(wrdlst))
# 
# 
# txt_len = len(wrdlst)
# #print(txt_len)
# nmb_apprs = 0
# for ii in range(0, txt_len):
#     if str(wrdlst[ii]) == "command":
#         nmb_apprs += 1
#         #this type of string comparison works
#     print(nmb_apprs)
#      #this is printing the number of time the word command appears
#     #multiple of these are getting printed

# Class는 새로운 타입을 만들어 자원을 공유 가능

# class Singer:           # class는 
#     title_song = "빛나라 대한민국"

#     def sing(self):
#         msg = "노래는 "
#         print(msg, self.title_song)

# import ex22singer 이렇게 부를 수도 있지만.
# bts = ex22singer.Singer()
# from ex22singer import Singer 이렇게 쓰자.

from ex22singer import Singer

bts = Singer() # 생성자 호출해 객체 생성후 주소를 bts에 치환

bts.sing()
print(type(bts))    # <class '__main__.Singer'> 새로운 타입.

bts.title_song = "Permission to Dance"

bts.sing()

bts.corperation = "BigHit Entertament"
print("소속사 : ", bts.corperation)


ive = Singer()
ive.sing()
print(type(ive))
#print("소속사 : ", ive.corp)

Singer.title_song = "아 대한민국"
bts.sing()
ive.sing()

niceGroup = ive
niceGroup.sing()


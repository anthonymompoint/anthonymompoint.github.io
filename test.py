import os
files = ["bean.jpeg" ,"butterflyin.jpeg" ,"cruisin.jpeg" ,"dinosaurin.jpeg" ,"first_disney.jpeg" ,"goirls_2.jpeg" ,"halloween.jpeg" ,"horse.jpeg" ,"jamaica_1.jpeg" ,"jamaica_4.jpeg" ,"lastscream.jpeg" ,"newyears.jpeg" ,"piratescove.jpeg" ,"sexynerds.jpeg" ,"toofless.jpeg", "ben.jpeg" ,"cosplay_1.jpeg" ,"dasboischrysler.jpeg" ,"eevui.jpeg" ,"georgia2024.jpeg" ,"goirls_3.jpeg" ,"hoes.jpeg" ,"icydicey.jpeg" ,"jamaica_2.jpeg" ,"jazzy.jpeg" ,"mexico.jpeg" ,"Nook.jpeg" ,"prommin.jpeg" ,"su.jpeg" ,"venue.jpeg"
,"brown.jpeg" ,"cosplay_2.jpeg" ,"dinobitin.jpeg" ,"fire.jpeg" ,"goirls.jpeg" ,"graduation.jpeg" ,"homecoming2017.jpeg" ,"irishhandcuffs.jpeg" ,"jamaica_3.jpeg" ,"keepinitoldschool.jpeg" ,"mypippa.jpeg" ,"piratecrawl.jpeg" ,"raisemeup.jpeg" ,"thechose.jpeg" ,"whatthebirddoin.jpeg"]


for file in files:
    print(f"<!-- Gallery item start --> \n\t<div class=\"gallery-item\"> \n\t\t<div class=\"gallery-item-inner\">\n\t\t\t<img src=\"img/gallery/thumbnails/thumb-{os.path.splitext(file)[0]}.jpg\" data-large=\"img/gallery/{file}\" alt=\"{file}\">\n\t\t</div>\n\t</div>\n<!-- Gallery item end -->")
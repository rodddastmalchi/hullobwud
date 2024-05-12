class Emotions:
    SAD = "sad"
    HAPPY = 'happy'
    MEMEY = 'memey'
    TIRED = 'tired'
    SLOSHED = 'sloshed'
    RANDOM = 'random'


class ImageWithText:
    def __init__(self, text, img, emotion) -> None:
        self.img_path = emotion + '/' + img
        self.text = text
        self.emotion = emotion


h1text = ("I'm not quite too shore hwaay you were so happy jumping in this picture. Regardless, it was a gr9 time with "
          "you and Diana in Boston hopefully we can fuckin do it again in Texas.")
h1img = 'IMG_2926.png'
h1 = ImageWithText(h1text, h1img, Emotions.HAPPY)

h2text = ("When we were Copenhagen queens. One of the very few pictures of both us (lol) but also our first "
          "internation trip together. I had a lot of fun and I can't wait for our next trip.")
h2img = 'IMG_5101.png'
h2emotion = Emotions.HAPPY
h2 = ImageWithText(h2text, h2img, Emotions.HAPPY)

h3text = ("Another rare selfie of us. Our first time being Sweden sisters, it was surprising how dead the city was and "
          "just like many other places, this castle was closed. But hey, at least we didn't get deported for not "
          "having a passports.")
h3img = 'IMG_5187.png'
h3 = ImageWithText(h3text, h3img, Emotions.HAPPY)

h4text = ("Our first time cooking/baking together. We had just come back from New York and were inspired to make "
          "cheesecake. It was hulluh good and who would've thought this would be the first of so many meals we would "
          "make.")
h4img = 'IMG_7607.png'
h4 = ImageWithText(h4text, h4img, Emotions.HAPPY)

h5text = ("Ayo, this is my swamp. Some people say Disneyland is the happiest place on Earth, I beg to differ. Nothing "
          "shlaps as much as In n Out. Thanks for taking me to the motherland for our 1 year bwud, it was truly a "
          "religious journey for me.")
h5img = 'IMG_7832.png'
h5 = ImageWithText(h5text, h5img, Emotions.HAPPY)

h6text = ("Look at the pure joy on your face when you pink AMF. This was actually in Irvine right before we ate dinner "
          "with Taylor. If you search of pure, unbridled joy on Google, this is for shorely the first image that "
          "shows up.")
h6img = 'IMG_9334.png'
h6 = ImageWithText(h6text, h6img, Emotions.HAPPY)

memey1Text = ("This is a certified Hayley classic. In Boston when we went to the museum, you said \"look it's my "
              "ancestors\" and then you did this. Truly one of my favorite Hayley moments (and of course you were "
              "sloshed).")
memey1Img = "IMG_2759.png"
m1 = ImageWithText(memey1Text, memey1Img, Emotions.MEMEY)

memey2Text = ("Shoutout to Diana for this picture. If it wasn't for her, we'd have approximately 0 pictures of us in "
              "Boston. This documenting a rare occasion of you eating huge.")
memey2Img = 'IMG_2900.png'
m2 = ImageWithText(memey2Text, memey2Img, Emotions.MEMEY)

memey3Text = ("Do I even need to explain this one? I love your touch of adding the beef chow fun, because you're damn "
              "right - I FUCKIN DID IT AGAIN.")
memey3Img = 'IMG_4049.png'
m3 = ImageWithText(memey3Text, memey3Img, Emotions.MEMEY)

memey4Text = ("This is a bit of a throwback to one of our first ever memes. Back when a certain someone posted a "
              "ridiculous picture on their Instagram, you quickly understood the assignment - we had to recreate it. "
              "This is one of our first ever memes and for shore it wasn't the last.")
memey4Img = 'IMG_5462.png'
m4 = ImageWithText(memey4Text, memey4Img, Emotions.MEMEY)

memey5Text = "Yessir, this pretty much sums up our relationship. We are absolutely gr∞ at texting what can I say."
memey5Img = 'IMG_8048.png'
m5 = ImageWithText(memey5Text, memey5Img, Emotions.MEMEY)

memey6Text = ("One of my all time favorite memes. This one is truly the pinnacle of all memes, by itself it's a good "
              "meme but in context, it's top tier content.")
memey6Img = 'IMG_8816.png'
m6 = ImageWithText(memey6Text, memey6Img, Emotions.MEMEY)

memey7Text = ('Ayo, periodT. Not sure hwaay I have this in my camera roll but yessir. We love a good period, '
              'especially when it comes to fok smashing white sheets.')
memey7Img = 'IMG_8966.png'
m7 = ImageWithText(memey7Text, memey7Img, Emotions.MEMEY)

memey8Text = ("This image definitely could have gone in the sad category. If you are ever feeling like a plastic bag "
              "drifting through the wind wanting to start again, just know that it could be worse, you could be "
              "driving for Ferrari.")
memey8Img = 'IMG_9018.png'
m8 = ImageWithText(memey8Text, memey8Img, Emotions.MEMEY)

random1Text = ("Not gonna lie, but I have no idea where this came from. I was just looking through my photos and this "
               "one was there and I felt like I had to include it. Hopefully Guodong is having a nice life.")
random1Img = 'IMG_7920.png'
r1 = ImageWithText(random1Text, random1Img, Emotions.RANDOM)

random2Text = ("If there was a scary or frightening category, this image would be the first one in it. I still have no "
               "idea how the fok you even made this face, but it reminds me of Jack Nicholson when he said \"here "
               "comes Johnny!\"")
random2Img = 'IMG_8306.png'
r2 = ImageWithText(random2Text, random2Img, Emotions.RANDOM)

random3Text = ("You know exactly hwaay I put this here. I just had to remind you that even though you are the biggest "
               "beta I know, I still love you.")
random3Img = 'IMG_8552.png'
r3 = ImageWithText(random3Text, random3Img, Emotions.RANDOM)

random4Text = ("This has got to be the best hairdo you have ever had. This is a 10/10, look at how many strands are "
               "sticking straight up. I think you should keep it like this.")
random4Img = 'IMG_9086.png'
r4 = ImageWithText(random4Text, random4Img, Emotions.RANDOM)

random5Text = ("I'm always on the lookout for a good hairdo. This one proves that your hair sticks straight up "
               "anywhere in the world, whether it's the US or even in Scandinavia.")
random5Img = 'IMG_9502.png'
r5 = ImageWithText(random5Text, random5Img, Emotions.RANDOM)

sad1Text = ("A picture of us in that random church we found in Lisbon. Thanks for being such a spontaneous sister with "
            "me, so where are we visiting next?")
sad1Img = '9DBFE218-2581-4109-8AC3-0DDED713A438.png'
s1 = ImageWithText(sad1Text, sad1Img, Emotions.SAD)

sad2Text = ("If you are feeling sad, just remember this tasty creation I made for you. This was peak culinary activity "
            "for shore, the gummy dolphins truly topped it off")
sad2Img = '64583126668__92610E8C-C189-4634-B9D8-2F8CBDD8E19E.png'
s2 = ImageWithText(sad2Text, sad2Img, Emotions.SAD)

sad3Text = ("This is during our impromptu excursion to Madeira. I had a lot of fun, thanks for facing your inner "
            "demons and riding on the gondola with us. Miss you bwud, can't wait for our next adventure!")
sad3Img = 'F5B4474A-2B61-4FF4-8178-F23EACE80118.png'
s3 = ImageWithText(sad3Text, sad3Img, Emotions.SAD)

sad4Text = ("Ah yes, the classic dress you bought that literally doesn't match any other color. I still don't know if "
            "that dress was more purple or more grey. Either way, thanks for bringing me to the beta club formal, "
            "anything for you.")
sad4Img = 'IMG_5953.png'
s4 = ImageWithText(sad4Text, sad4Img, Emotions.SAD)

sad5Text = ("This was ogre the summer when we went to Irvine and stayed at your place. Nothing compares to the sadness "
            "of being in front of the law school without Athena's Java City cart being there.")
sad5Img = 'IMG_8008.png'
s5 = ImageWithText(sad5Text, sad5Img, Emotions.SAD)

sad6Text = ("The free coffee from Dunkin was truly very sad, I'd rather my coffee not taste like Chipotle. Good effort "
            "from you to try and make it better with some sister sprinkles, because everything is better with "
            "sprinkles.")
sad6Img = 'IMG_8828.png'
s6 = ImageWithText(sad6Text, sad6Img, Emotions.SAD)

sad7Text = ("The single most disappointing place on Earth. With such a legendary name, it should be illegal to have "
            "such garbage donuts. The only redeeming quality of this picture is that this was the start of 2 years "
            "with you my bruvr and for that I can't complain.")
sad7Img = 'IMG_9438.png'
s7 = ImageWithText(sad7Text, sad7Img, Emotions.SAD)

sloshed1Text = ("This was in Mesa Towers after a friend gave you a nice necklace. Another installation of an iconic "
                "sloshed Hayley selfie.")
sloshed1Img = 'IMG_4760.png'
sl1 = ImageWithText(sloshed1Text, sloshed1Img, Emotions.SLOSHED)

sloshed2Text = ("I don't know where you are, you don't know where you are, but we can both agree that this such a "
                "classic moment for you. Also, it could really be anywhere considering you were sloshed pretty often "
                "freshman year.")
sloshed2Img = 'IMG_5244.png'
sl2 = ImageWithText(sloshed2Text, sloshed2Img, Emotions.SLOSHED)

sloshed3Text = ("Here you got sloshed in the morning after Sabrina made us drink hulluh Soju before having breakfast "
                "in Danville. Also, random side note, this was the day UCI basketball team beat Kansas State in March"
                " Madness.")
sloshed3Img = 'IMG_5306.png'
sl3 = ImageWithText(sloshed3Text, sloshed3Img, Emotions.SLOSHED)

sloshed4Text = ("Not quite too shore hwaay you're laying on the floor, but what can I say, there is no point in "
                "questioning sloshed Hayley.")
sloshed4Img = 'IMG_7981.png'
sl4 = ImageWithText(sloshed4Text, sloshed4Img, Emotions.SLOSHED)

tired1Text = ("If you are ever tired, just think of your favorite place in the world, your true home, and you'll be "
              "reinvigorated. VEGAS BABY!")
tired1Img = 'A68B8641-CB5B-45FC-ADF4-D08761CCF4E0.png'
t1 = ImageWithText(tired1Text, tired1Img, Emotions.TIRED)

tired2Text = ("Our first trip to Santa Barbara after starting college. It was nap time until it very suddenly wasn't. "
              "As CupcakKe once said, eyes wide open. I'm paraphrasing.")
tired2Img = 'IMG_4930.png'
t2 = ImageWithText(tired2Text, tired2Img, Emotions.TIRED)

tired3Text = ("Our favorite time: NAP TIME. Thanks for all the nap times we've had together bwud and you should "
              "#never5get that every time is nap time. So if you're tired, you know what you need to do.")
tired3Img = 'IMG_8548.png'
t3 = ImageWithText(tired3Text, tired3Img, Emotions.TIRED)

HAPPY = [h1, h2, h3, h4, h5, h6]
MEMEY = [m1, m2, m3, m4, m5, m6, m7, m8]
RANDOM = [r1, r2, r3, r4, r5]
SAD = [s1, s2, s3, s4, s5, s6, s7]
SLOSHED = [sl1, sl2, sl3, sl4]
TIRED = [t1, t2, t3]

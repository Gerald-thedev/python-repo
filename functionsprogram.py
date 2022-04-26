import random
def socialPlatforms(media):
    if media == 1:
        return 'Twitter'
    elif media == 2:
        return 'Instagram'
    elif media == 3:
        return 'Snapchat'
    elif media == 4:
        return 'Tiktok'
    elif media == 5:
        return 'Whatsapp'
    elif media == 6:
        return 'Linkedin'
    elif media == 7:
        return 'Facebook'
    elif media == 8:
        return 'Gmail'
mostUsed = random.randint(1,8)
bestMedia = socialPlatforms(mostUsed)
print(bestMedia)

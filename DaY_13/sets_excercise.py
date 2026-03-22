media=list(input("enter the photoes and vidoes with extensions:").split())
photoes=[]
vidoes=[]
for i in media:
    if i.endswith("png") or i.endswith("jpg"):
        photoes.append(i)
    else:
        vidoes.append(i)
if photoes:
    print("PHOTO GALLERY")
    print("------------------------")
    for photo in photoes:
        print(f"{photoes.index(photo)} {photo}")
        share_pic=input("enter the pic to share:").split()
        print(f"{share_pic} shared")
        print("\n")
if vidoes:
    print("VIDOES")
    print("------------------------")
    for video in vidoes:
        print(f"{vidoes.index(video)}) {video}")
        share_video=input("enter the video to share:")
        print(f"{share_video} shared")

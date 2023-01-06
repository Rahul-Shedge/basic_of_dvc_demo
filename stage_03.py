with open("Artifacts.txt","r") as f:
    text = f.read()


with open("Artifacts2.txt","w+") as f:
    f.write(text +"added lines")


print("stage 3 ends")
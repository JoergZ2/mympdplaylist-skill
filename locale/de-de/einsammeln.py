import os
files = os.listdir()
files.sort()
for i in range(len(files)):
    f = open(files[i], "r")
    filename = files[i]
    content = f.readlines()
    f2 = open("sampler.txt", "a")
    f2.write("**" + filename + "**\n")
    #print(filename)
    for i2 in range(len(content)):
        f2.write(content[i2] + "\n")
        #print(content[i2])
    f2.write('\n\n')
    f.close()
f2.close()


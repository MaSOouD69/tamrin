with open("primenumbers.txt","r") as pr:
    line_pr=pr.readlines()
with open('happynumbers.txt','r') as hp:
    line_hp=hp.readlines()
x=[]
with open("newtxt.txt",'w') as wfile:
    for line1 in line_hp:
        for line2 in line_pr:
            if line1==line2:
                wfile.write(line1)

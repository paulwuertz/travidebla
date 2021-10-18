from svgutils.compose import *
import svgutils.transform as sg
import itertools

# load matpotlib-generated figures

#alle rotationen
cards = { i:[sg.fromstring(open('mcards_'+str(i)+'.svg').read()).find_id("layer"+str(i)) for r in range(8)] for i in [1,2,3,4] }
for i in range(1,4):
    for r in range(1,4):
        cards[i][r].rotate(90*r, 30, 30)
        fig = sg.SVGFigure('60', '60')
        fig.append([cards[i][r]])
        fig.save("gen/single"+str(i)+"_"+str(r)+".svg")
    for r in range(1,4):
        cards[i][r].scale(x=-1, y=1)
        cards[i][r].moveto(x=60, y=0)
        cards[i][r].rotate(90*r, 30, 30)
        fig = sg.SVGFigure('60', '60')
        fig.append([cards[i][r]])
        fig.save("gen/single_ud"+str(i)+"_"+str(r)+".svg")

#kombinieren

cnt=0
positions_taken = []
for i in range(4):
    positions_taken.append(i)
    for j in range(4):
        if j in positions_taken: continue
        positions_taken.append(j)
        for k in range(4):
            if k in positions_taken: continue
            positions_taken.append(k)
            for l in range(4):
                if l in positions_taken: continue
                fig = sg.SVGFigure('60', '60')
                print(cnt, ":", i, j, k, l)
                fig.append([cards[1][i]])
                fig.append([cards[2][j]])
                fig.append([cards[3][k]])
                fig.append([cards[4][l]])
                fig.save("gen/fig_final"+str(cnt)+".svg")
                cnt+=1
            positions_taken.remove(k)
        positions_taken.remove(j)
    positions_taken.remove(i)

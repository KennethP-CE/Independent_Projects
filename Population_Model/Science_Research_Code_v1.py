import math
import matplotlib.pyplot as plt
import sys
import random

yr = 0
beary = []
bearm = []
sealy = []
sealm = []
cody = []
codm = []
AxisXy = []
AxisXm = []
TimeXy = 1
TimeXm = 1
sealhunt = 205/12
sealEloss = 511/375
phunti = .45
phuntn = .1
polarEloss = .05
pstarve = 1/450
pstarvewfac = 2/3
pdnat = 1/300
sstarve = 1/1200
sdnat = 7/4800
cdnat = .03
cfacfac = 1/12000
cbirth = 0.0416
pwas = 750
swas = 125
cwas = 10
pwi = 1000
swi = 150
pbirthfac = 1/15
pst = round(float(input("What is the starting polar bear population size (1000)?: ")), 0)
sst = round(float(input("What is the starting seal population (200,000)?: ")), 0)
cst = round(float(input("What is the starting cod population (300,000,000)?: ")), 0)
p = pst
s = sst
c = cst
pw = pwas*p
sw = swas*s
icel = round(float(input("Should the simulation use modern (1) or historic (2) sea ice levels?: ")))
if icel == 1:
    seaice = [12.3, 13.5, 13.9, 14.0, 13.5, 11.6, 9.2, 6.4, 4.8, 5.1, 7.7, 9.6]
if icel == 2:
    seaice = [13.7, 14.9, 15.5, 15.4, 14.1, 12.6, 10.9, 8.3, 6.7, 7.0, 9.7, 11.9]
yrc = round(float(input("How many years should the simulation encompass?: ")), 0)

def run_simulation(yr, TimeXy, TimeXm, AxisXy, AxisXm, p, s, c, pw, sw, seaice, yrc, pst, sst, cst, pwas, swas, cwas, pstarve, polarEloss, phunti, phuntn, pwi, pdnat, pstarvewfac, sstarve, swi, sdnat, cdnat, cfacfac, cbirth):
    while yr<yrc:
        AxisXy.append(TimeXy)
        beary.append(p)
        sealy.append(s)
        cody.append(c)
        yr = yr + 1
        TimeXy = TimeXy + 1
        #Month #1
        AxisXm.append(TimeXm)
        bearm.append(p)
        sealm.append(s)
        codm.append(c)
        TimeXm = TimeXm + 1
        swa = round(s/sw, 0) #Est. 125
        codh = round(c*(1/cst)*s*(sealhunt)) #Est. 3,416,667 (17.1)
        sw = round((sw - ((sealEloss)*sw) + (codh*cwas)), 0) #Est. +.7
        iceh = round(seaice[0]/15*pst, 0) #Est. 777
        if p > iceh:
            sealh = round((((1/sst)*s*phunti*iceh)+((1/sst)*s*phuntn*(p-iceh))), 0) #Est. 372 (0.372)
        else:
            sealh = round(((1/sst)*s*phunti*p), 0) #Est 450 (.45)
        pw = round(pw - (polarEloss*pw) + (sealh*swa*(4/5)), 0) #Est. -.3
        pwa = round(pw/p, 0) #Est. 750
        if pwa<1000:
            sp = round((p*(pstarve)*(pwi-pwa)*(1/(pwi-pwas))), 0) #Est. 2.2 (2=1/500)
        else:
            sp = 0
        dp = round((p*(pdnat)), 0) #Est. 3.3
        p = round((p-(dp+sp)), 0) #Est. -5.5 (5 = 1/200)
        pw = round((pw - ((pwa*dp)+(pwa*(pstarvewfac)*sp))), 0) #Est. -3575 (-3.57)
        if swa<150:
            ss = round((s*(sstarve)*(swi-swa)*(1/(swi-swas))), 0) #Est. 167
        else:
            ss = 0
        ds = round(((sdnat)*s), 0) #Est. 292
        s = round(s-(ds+ss+sealh)) #Est. -831
        sw = round((sw - ((swa*(ds+sealh))+(swa*(2/3)*ss))), 0) #Est. -96,917 (-.48)
        cfac = round((c-cst)*(1/(cst/100)), 0) #Est. 0
        cd = round((c*(cdnat+(cfac*(cfacfac)))), 0) #Est. 9,000,000 (3%)
        c = round((c - (codh+cd) + (cbirth*c)), 0) #Est. +63333 (0.02%)
        #Month #2
        AxisXm.append(TimeXm)
        bearm.append(p)
        sealm.append(s)
        codm.append(c)
        TimeXm = TimeXm + 1
        swa = round(s/sw, 0) #Est. 125
        codh = round(c*(1/cst)*s*(sealhunt)) #Est. 3,416,667 (17.1)
        sw = round((sw - ((sealEloss)*sw) + (codh*cwas)), 0) #Est. +.7
        iceh = round(seaice[1]/15*pst, 0) #Est. 777
        if p > iceh:
            sealh = round((((1/sst)*s*phunti*iceh)+((1/sst)*s*phuntn*(p-iceh))), 0) #Est. 372 (0.372)
        else:
            sealh = round(((1/sst)*s*phunti*p), 0) #Est 450 (.45)
        pw = round(pw - (polarEloss*pw) + (sealh*swa*(4/5)), 0) #Est. -.3
        pwa = round(pw/p, 0) #Est. 750
        if pwa<1000:
            sp = round((p*(pstarve)*(pwi-pwa)*(1/(pwi-pwas))), 0) #Est. 2.2 (2=1/500)
        else:
            sp = 0
        dp = round((p*(pdnat)), 0) #Est. 3.3
        p = round((p-(dp+sp)), 0) #Est. -5.5 (5 = 1/200)
        pw = round((pw - ((pwa*dp)+(pwa*(pstarvewfac)*sp))), 0) #Est. -3575 (-3.57)
        if swa<150:
            ss = round((s*(sstarve)*(swi-swa)*(1/(swi-swas))), 0) #Est. 167
        else:
            ss = 0
        ds = round(((sdnat)*s), 0) #Est. 292
        s = round(s-(ds+ss+sealh)) #Est. -831
        sw = round((sw - ((swa*(ds+sealh))+(swa*(2/3)*ss))), 0) #Est. -96,917 (-.48)
        cfac = round((c-cst)*(1/(cst/100)), 0) #Est. 0
        cd = round((c*(cdnat+(cfac*(cfacfac)))), 0) #Est. 9,000,000 (3%)
        c = round((c - (codh+cd) + (cbirth*c)), 0) #Est. +63333 (0.02%)
        #Month #3
        AxisXm.append(TimeXm)
        bearm.append(p)
        sealm.append(s)
        codm.append(c)
        TimeXm = TimeXm + 1
        swa = round(s/sw, 0) #Est. 125
        codh = round(c*(1/cst)*s*(sealhunt)) #Est. 3,416,667 (17.1)
        sw = round((sw - ((sealEloss)*sw) + (codh*cwas)), 0) #Est. +.7
        iceh = round(seaice[2]/15*pst, 0) #Est. 777
        if p > iceh:
            sealh = round((((1/sst)*s*phunti*iceh)+((1/sst)*s*phuntn*(p-iceh))), 0) #Est. 372 (0.372)
        else:
            sealh = round(((1/sst)*s*phunti*p), 0) #Est 450 (.45)
        pw = round(pw - (polarEloss*pw) + (sealh*swa*(4/5)), 0) #Est. -.3
        pwa = round(pw/p, 0) #Est. 750
        if pwa<1000:
            sp = round((p*(pstarve)*(pwi-pwa)*(1/(pwi-pwas))), 0) #Est. 2.2 (2=1/500)
        else:
            sp = 0
        dp = round((p*(pdnat)), 0) #Est. 3.3
        p = round((p-(dp+sp)), 0) #Est. -5.5 (5 = 1/200)
        pw = round((pw - ((pwa*dp)+(pwa*(pstarvewfac)*sp))), 0) #Est. -3575 (-3.57)
        if swa<150:
            ss = round((s*(sstarve)*(swi-swa)*(1/(swi-swas))), 0) #Est. 167
        else:
            ss = 0
        ds = round(((sdnat)*s), 0) #Est. 292
        s = round(s-(ds+ss+sealh)) #Est. -831
        sw = round((sw - ((swa*(ds+sealh))+(swa*(2/3)*ss))), 0) #Est. -96,917 (-.48)
        cfac = round((c-cst)*(1/(cst/100)), 0) #Est. 0
        cd = round((c*(cdnat+(cfac*(cfacfac)))), 0) #Est. 9,000,000 (3%)
        c = round((c - (codh+cd) + (cbirth*c)), 0) #Est. +63333 (0.02%)
        #Month #4
        AxisXm.append(TimeXm)
        bearm.append(p)
        sealm.append(s)
        codm.append(c)
        TimeXm = TimeXm + 1
        swa = round(s/sw, 0) #Est. 125
        codh = round(c*(1/cst)*s*(sealhunt)) #Est. 3,416,667 (17.1)
        sw = round((sw - ((sealEloss)*sw) + (codh*cwas)), 0) #Est. +.7
        iceh = round(seaice[3]/15*pst, 0) #Est. 777
        if p > iceh:
            sealh = round((((1/sst)*s*phunti*iceh)+((1/sst)*s*phuntn*(p-iceh))), 0) #Est. 372 (0.372)
        else:
            sealh = round(((1/sst)*s*phunti*p), 0) #Est 450 (.45)
        pw = round(pw - (polarEloss*pw) + (sealh*swa*(4/5)), 0) #Est. -.3
        pwa = round(pw/p, 0) #Est. 750
        if pwa<1000:
            sp = round((p*(pstarve)*(pwi-pwa)*(1/(pwi-pwas))), 0) #Est. 2.2 (2=1/500)
        else:
            sp = 0
        dp = round((p*(pdnat)), 0) #Est. 3.3
        p = round((p-(dp+sp)), 0) #Est. -5.5 (5 = 1/200)
        pw = round((pw - ((pwa*dp)+(pwa*(pstarvewfac)*sp))), 0) #Est. -3575 (-3.57)
        if swa<150:
            ss = round((s*(sstarve)*(swi-swa)*(1/(swi-swas))), 0) #Est. 167
        else:
            ss = 0
        ds = round(((sdnat)*s), 0) #Est. 292
        s = round(s-(ds+ss+sealh)) #Est. -831
        sw = round((sw - ((swa*(ds+sealh))+(swa*(2/3)*ss))), 0) #Est. -96,917 (-.48)
        cfac = round((c-cst)*(1/(cst/100)), 0) #Est. 0
        cd = round((c*(cdnat+(cfac*(cfacfac)))), 0) #Est. 9,000,000 (3%)
        c = round((c - (codh+cd) + (cbirth*c)), 0) #Est. +63333 (0.02%)
        #Month #5
        AxisXm.append(TimeXm)
        bearm.append(p)
        sealm.append(s)
        codm.append(c)
        TimeXm = TimeXm + 1
        swa = round(s/sw, 0) #Est. 125
        codh = round(c*(1/cst)*s*(sealhunt)) #Est. 3,416,667 (17.1)
        sw = round((sw - ((sealEloss)*sw) + (codh*cwas)), 0) #Est. +.7
        iceh = round(seaice[4]/15*pst, 0) #Est. 777
        if p > iceh:
            sealh = round((((1/sst)*s*phunti*iceh)+((1/sst)*s*phuntn*(p-iceh))), 0) #Est. 372 (0.372)
        else:
            sealh = round(((1/sst)*s*phunti*p), 0) #Est 450 (.45)
        pw = round(pw - (polarEloss*pw) + (sealh*swa*(4/5)), 0) #Est. -.3
        pwa = round(pw/p, 0) #Est. 750
        if pwa<1000:
            sp = round((p*(pstarve)*(pwi-pwa)*(1/(pwi-pwas))), 0) #Est. 2.2 (2=1/500)
        else:
            sp = 0
        dp = round((p*(pdnat)), 0) #Est. 3.3
        p = round((p-(dp+sp)), 0) #Est. -5.5 (5 = 1/200)
        pw = round((pw - ((pwa*dp)+(pwa*(pstarvewfac)*sp))), 0) #Est. -3575 (-3.57)
        if swa<150:
            ss = round((s*(sstarve)*(swi-swa)*(1/(swi-swas))), 0) #Est. 167
        else:
            ss = 0
        ds = round(((sdnat)*s), 0) #Est. 292
        s = round(s-(ds+ss+sealh)) #Est. -831
        sw = round((sw - ((swa*(ds+sealh))+(swa*(2/3)*ss))), 0) #Est. -96,917 (-.48)
        cfac = round((c-cst)*(1/(cst/100)), 0) #Est. 0
        cd = round((c*(cdnat+(cfac*(cfacfac)))), 0) #Est. 9,000,000 (3%)
        c = round((c - (codh+cd) + (cbirth*c)), 0) #Est. +63333 (0.02%)
        #Month #6
        AxisXm.append(TimeXm)
        bearm.append(p)
        sealm.append(s)
        codm.append(c)
        TimeXm = TimeXm + 1
        swa = round(s/sw, 0) #Est. 125
        codh = round(c*(1/cst)*s*(sealhunt)) #Est. 3,416,667 (17.1)
        sw = round((sw - ((sealEloss)*sw) + (codh*cwas)), 0) #Est. +.7
        iceh = round(seaice[5]/15*pst, 0) #Est. 777
        if p > iceh:
            sealh = round((((1/sst)*s*phunti*iceh)+((1/sst)*s*phuntn*(p-iceh))), 0) #Est. 372 (0.372)
        else:
            sealh = round(((1/sst)*s*phunti*p), 0) #Est 450 (.45)
        pw = round(pw - (polarEloss*pw) + (sealh*swa*(4/5)), 0) #Est. -.3
        pwa = round(pw/p, 0) #Est. 750
        if pwa<1000:
            sp = round((p*(pstarve)*(pwi-pwa)*(1/(pwi-pwas))), 0) #Est. 2.2 (2=1/500)
        else:
            sp = 0
        dp = round((p*(pdnat)), 0) #Est. 3.3
        p = round((p-(dp+sp)), 0) #Est. -5.5 (5 = 1/200)
        pw = round((pw - ((pwa*dp)+(pwa*(pstarvewfac)*sp))), 0) #Est. -3575 (-3.57)
        if swa<150:
            ss = round((s*(sstarve)*(swi-swa)*(1/(swi-swas))), 0) #Est. 167
        else:
            ss = 0
        ds = round(((sdnat)*s), 0) #Est. 292
        s = round(s-(ds+ss+sealh)) #Est. -831
        sw = round((sw - ((swa*(ds+sealh))+(swa*(2/3)*ss))), 0) #Est. -96,917 (-.48)
        cfac = round((c-cst)*(1/(cst/100)), 0) #Est. 0
        cd = round((c*(cdnat+(cfac*(cfacfac)))), 0) #Est. 9,000,000 (3%)
        c = round((c - (codh+cd) + (cbirth*c)), 0) #Est. +63333 (0.02%)
        #Month #7
        AxisXm.append(TimeXm)
        bearm.append(p)
        sealm.append(s)
        codm.append(c)
        TimeXm = TimeXm + 1
        swa = round(s/sw, 0) #Est. 125
        codh = round(c*(1/cst)*s*(sealhunt)) #Est. 3,416,667 (17.1)
        sw = round((sw - ((sealEloss)*sw) + (codh*cwas)), 0) #Est. +.7
        iceh = round(seaice[6]/15*pst, 0) #Est. 777
        if p > iceh:
            sealh = round((((1/sst)*s*phunti*iceh)+((1/sst)*s*phuntn*(p-iceh))), 0) #Est. 372 (0.372)
        else:
            sealh = round(((1/sst)*s*phunti*p), 0) #Est 450 (.45)
        pw = round(pw - (polarEloss*pw) + (sealh*swa*(4/5)), 0) #Est. -.3
        pwa = round(pw/p, 0) #Est. 750
        if pwa<1000:
            sp = round((p*(pstarve)*(pwi-pwa)*(1/(pwi-pwas))), 0) #Est. 2.2 (2=1/500)
        else:
            sp = 0
        dp = round((p*(pdnat)), 0) #Est. 3.3
        p = round((p-(dp+sp)), 0) #Est. -5.5 (5 = 1/200)
        pw = round((pw - ((pwa*dp)+(pwa*(pstarvewfac)*sp))), 0) #Est. -3575 (-3.57)
        if swa<150:
            ss = round((s*(sstarve)*(swi-swa)*(1/(swi-swas))), 0) #Est. 167
        else:
            ss = 0
        ds = round(((sdnat)*s), 0) #Est. 292
        s = round(s-(ds+ss+sealh)) #Est. -831
        sw = round((sw - ((swa*(ds+sealh))+(swa*(2/3)*ss))), 0) #Est. -96,917 (-.48)
        cfac = round((c-cst)*(1/(cst/100)), 0) #Est. 0
        cd = round((c*(cdnat+(cfac*(cfacfac)))), 0) #Est. 9,000,000 (3%)
        c = round((c - (codh+cd) + (cbirth*c)), 0) #Est. +63333 (0.02%)
        #Month #8
        AxisXm.append(TimeXm)
        bearm.append(p)
        sealm.append(s)
        codm.append(c)
        TimeXm = TimeXm + 1
        swa = round(s/sw, 0) #Est. 125
        codh = round(c*(1/cst)*s*(sealhunt)) #Est. 3,416,667 (17.1)
        sw = round((sw - ((sealEloss)*sw) + (codh*cwas)), 0) #Est. +.7
        iceh = round(seaice[7]/15*pst, 0) #Est. 777
        if p > iceh:
            sealh = round((((1/sst)*s*phunti*iceh)+((1/sst)*s*phuntn*(p-iceh))), 0) #Est. 372 (0.372)
        else:
            sealh = round(((1/sst)*s*phunti*p), 0) #Est 450 (.45)
        pw = round(pw - (polarEloss*pw) + (sealh*swa*(4/5)), 0) #Est. -.3
        pwa = round(pw/p, 0) #Est. 750
        if pwa<1000:
            sp = round((p*(pstarve)*(pwi-pwa)*(1/(pwi-pwas))), 0) #Est. 2.2 (2=1/500)
        else:
            sp = 0
        dp = round((p*(pdnat)), 0) #Est. 3.3
        p = round((p-(dp+sp)), 0) #Est. -5.5 (5 = 1/200)
        pw = round((pw - ((pwa*dp)+(pwa*(pstarvewfac)*sp))), 0) #Est. -3575 (-3.57)
        if swa<150:
            ss = round((s*(sstarve)*(swi-swa)*(1/(swi-swas))), 0) #Est. 167
        else:
            ss = 0
        ds = round(((sdnat)*s), 0) #Est. 292
        s = round(s-(ds+ss+sealh)) #Est. -831
        sw = round((sw - ((swa*(ds+sealh))+(swa*(2/3)*ss))), 0) #Est. -96,917 (-.48)
        cfac = round((c-cst)*(1/(cst/100)), 0) #Est. 0
        cd = round((c*(cdnat+(cfac*(cfacfac)))), 0) #Est. 9,000,000 (3%)
        c = round((c - (codh+cd) + (cbirth*c)), 0) #Est. +63333 (0.02%)
        #Month #10
        AxisXm.append(TimeXm)
        bearm.append(p)
        sealm.append(s)
        codm.append(c)
        TimeXm = TimeXm + 1
        swa = round(s/sw, 0) #Est. 125
        codh = round(c*(1/cst)*s*(sealhunt)) #Est. 3,416,667 (17.1)
        sw = round((sw - ((sealEloss)*sw) + (codh*cwas)), 0) #Est. +.7
        iceh = round(seaice[9]/15*pst, 0) #Est. 777
        if p > iceh:
            sealh = round((((1/sst)*s*phunti*iceh)+((1/sst)*s*phuntn*(p-iceh))), 0) #Est. 372 (0.372)
        else:
            sealh = round(((1/sst)*s*phunti*p), 0) #Est 450 (.45)
        pw = round(pw - (polarEloss*pw) + (sealh*swa*(4/5)), 0) #Est. -.3
        pwa = round(pw/p, 0) #Est. 750
        if pwa<1000:
            sp = round((p*(pstarve)*(pwi-pwa)*(1/(pwi-pwas))), 0) #Est. 2.2 (2=1/500)
        else:
            sp = 0
        dp = round((p*(pdnat)), 0) #Est. 3.3
        p = round((p-(dp+sp)), 0) #Est. -5.5 (5 = 1/200)
        pw = round((pw - ((pwa*dp)+(pwa*(pstarvewfac)*sp))), 0) #Est. -3575 (-3.57)
        if swa<150:
            ss = round((s*(sstarve)*(swi-swa)*(1/(swi-swas))), 0) #Est. 167
        else:
            ss = 0
        ds = round(((sdnat)*s), 0) #Est. 292
        s = round(s-(ds+ss+sealh)) #Est. -831
        sw = round((sw - ((swa*(ds+sealh))+(swa*(2/3)*ss))), 0) #Est. -96,917 (-.48)
        cfac = round((c-cst)*(1/(cst/100)), 0) #Est. 0
        cd = round((c*(cdnat+(cfac*(cfacfac)))), 0) #Est. 9,000,000 (3%)
        c = round((c - (codh+cd) + (cbirth*c)), 0) #Est. +63333 (0.02%)
        pbirthfac = round((1/15)*(25/24)*(pwa/pwas))
        #Month #11
        AxisXm.append(TimeXm)
        bearm.append(p)
        sealm.append(s)
        codm.append(c)
        TimeXm = TimeXm + 1
        swa = round(s/sw, 0) #Est. 125
        codh = round(c*(1/cst)*s*(sealhunt)) #Est. 3,416,667 (17.1)
        sw = round((sw - ((sealEloss)*sw) + (codh*cwas)), 0) #Est. +.7
        iceh = round(seaice[10]/15*pst, 0) #Est. 777
        if p > iceh:
            sealh = round((((1/sst)*s*phunti*iceh)+((1/sst)*s*phuntn*(p-iceh))), 0) #Est. 372 (0.372)
        else:
            sealh = round(((1/sst)*s*phunti*p), 0) #Est 450 (.45)
        pw = round(pw - (polarEloss*pw) + (sealh*swa*(4/5)), 0) #Est. -.3
        pwa = round(pw/p, 0) #Est. 750
        if pwa<1000:
            sp = round((p*(pstarve)*(pwi-pwa)*(1/(pwi-pwas))), 0) #Est. 2.2 (2=1/500)
        else:
            sp = 0
        dp = round((p*(pdnat)), 0) #Est. 3.3
        p = round((p-(dp+sp)), 0) #Est. -5.5 (5 = 1/200)
        pw = round((pw - ((pwa*dp)+(pwa*(pstarvewfac)*sp))), 0) #Est. -3575 (-3.57)
        if swa<150:
            ss = round((s*(sstarve)*(swi-swa)*(1/(swi-swas))), 0) #Est. 167
        else:
            ss = 0
        ds = round(((sdnat)*s), 0) #Est. 292
        s = round(s-(ds+ss+sealh)) #Est. -831
        sw = round((sw - ((swa*(ds+sealh))+(swa*(2/3)*ss))), 0) #Est. -96,917 (-.48)
        cfac = round((c-cst)*(1/(cst/100)), 0) #Est. 0
        cd = round((c*(cdnat+(cfac*(cfacfac)))), 0) #Est. 9,000,000 (3%)
        c = round((c - (codh+cd) + (cbirth*c)), 0) #Est. +63333 (0.02%)
        #Month #12
        AxisXm.append(TimeXm)
        bearm.append(p)
        sealm.append(s)
        codm.append(c)
        TimeXm = TimeXm + 1
        swa = round(s/sw, 0) #Est. 125
        codh = round(c*(1/cst)*s*(sealhunt)) #Est. 3,416,667 (17.1)
        sw = round((sw - ((sealEloss)*sw) + (codh*cwas)), 0) #Est. +.7
        iceh = round(seaice[11]/15*pst, 0) #Est. 777
        if p > iceh:
            sealh = round((((1/sst)*s*phunti*iceh)+((1/sst)*s*phuntn*(p-iceh))), 0) #Est. 372 (0.372)
        else:
            sealh = round(((1/sst)*s*phunti*p), 0) #Est 450 (.45)
        pw = round(pw - (polarEloss*pw) + (sealh*swa*(4/5)), 0) #Est. -.3
        pwa = round(pw/p, 0) #Est. 750
        if pwa<1000:
            sp = round((p*(pstarve)*(pwi-pwa)*(1/(pwi-pwas))), 0) #Est. 2.2 (2=1/500)
        else:
            sp = 0
        dp = round((p*(pdnat)), 0) #Est. 3.3
        p = round((p-(dp+sp)), 0) #Est. -5.5 (5 = 1/200)
        pw = round((pw - ((pwa*dp)+(pwa*(pstarvewfac)*sp))), 0) #Est. -3575 (-3.57)
        if swa<150:
            ss = round((s*(sstarve)*(swi-swa)*(1/(swi-swas))), 0) #Est. 167
        else:
            ss = 0
        ds = round(((sdnat)*s), 0) #Est. 292
        s = round(s-(ds+ss+sealh)) #Est. -831
        sw = round((sw - ((swa*(ds+sealh))+(swa*(2/3)*ss))), 0) #Est. -96,917 (-.48)
        cfac = round((c-cst)*(1/(cst/100)), 0) #Est. 0
        cd = round((c*(cdnat+(cfac*(cfacfac)))), 0) #Est. 9,000,000 (3%)
        c = round((c - (codh+cd) + (cbirth*c)), 0) #Est. +63333 (0.02%)
import math
import matplotlib.pyplot as plt
import sys
import random

yr = 0
bearw = []
sealw = []
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
sealhunt = 95
sealEloss = 47/30
phunti = 1840/699
phuntn = 0
polarEloss = 7/20
pstarve = 17/9900
pstarvewfac = 2/3
pdnat = 1/300
sstarve = 1/1200
sdnat = 1/540
cdnat = 0
cfacfac = 1/1000
cbirth = 1/24
pwas = 350
swas = 60
cwas = 1
pwi = 445
swi = 70
pbirthfac = 1/16.5
sbirthfac = 1/20
pst = round(float(input("What is the starting Ursus maritimus population size (1000)?: (0 for default) ")), 0)
if pst == 0:
    pst = 1000
if pst == 1:
    pst = 0
sst = round(float(input("What is the starting Pusa hispida population (1,380,000)?: (0 for default) ")), 0)
if sst == 0:
    sst = 1380000
if sst == 1:
    sst = 0
cst = round(float(input("What is the starting Boreogadus saida biomass in kg (3,130,530,000)?: (0 for default) ")), 0)
if cst == 0:
    cst = 3130530000
if cst == 1:
    cst = 0
p = pst
s = sst
c = cst
pw = pwas*p
sw = swas*s
pwa = pw/p
swa = sw/s
icel = round(float(input("Should the simulation use modern (1) or historic (2) sea ice levels?: ")))
if icel == 1:
    seaice = [12.3, 13.5, 13.9, 14.0, 13.5, 11.6, 9.2, 6.4, 4.8, 5.1, 7.7, 9.6]
if icel == 2:
    seaice = [13.7, 14.9, 15.5, 15.4, 14.1, 12.6, 10.9, 8.3, 6.7, 7.0, 9.7, 11.9]
yrc = round(float(input("How many years should the simulation encompass? (100): (0 for default) ")), 0)
if yrc == 0:
    yrc = 100

def run_simulation(yr, TimeXy, TimeXm, AxisXy, AxisXm, p, s, c, pw, sw, seaice, yrc, pst, sst, cst, pwas, swas, cwas, pstarve, polarEloss, phunti, phuntn, pwi, pdnat, pstarvewfac, sstarve, swi, sdnat, cdnat, cfacfac, cbirth, pbirthfac, sbirthfac, bearw, sealw, pwa, swa, beary, bearm, sealy, sealm, cody, codm, sealhunt, sealEloss):
    while yr<yrc:
        AxisXy.append(TimeXy)
        beary.append(p)
        sealy.append(s)
        cody.append(c)
        yr = yr + 1
        TimeXy = TimeXy + 1
        #Month #1
        bearw.append(pwa)
        AxisXm.append(TimeXm)
        bearm.append(p)
        sealm.append(s)
        codm.append(c)
        TimeXm = TimeXm + 1
        swa = round(sw/s, 0)
        sealw.append(swa)
        codh = round(c*(1/cst)*s*(sealhunt))
        sw = round((sw - (sealEloss*sw) + (codh*cwas)), 0)
        iceh = round(seaice[0]/15*pst, 0)
        if p > iceh:
            sealh = round((((1/sst)*s*phunti*iceh)+((1/sst)*s*phuntn*(p-iceh))), 0)
        else:
            sealh = round(((1/sst)*s*phunti*p), 0)
        pw = round(pw - (polarEloss*pw) + (sealh*swa*(4/5)), 0)
        pwa = round(pw/p, 0)
        if pwa<1000:
            sp = round((p*(pstarve)*(pwi-pwa)*(1/(pwi-pwas))), 0)
        else:
            sp = 0
        dp = round((p*(pdnat)), 0)
        p = round((p-(dp+sp)), 0)
        pw = round((pw - ((pwa*dp)+(pwa*(pstarvewfac)*sp))), 0)
        if swa<150:
            ss = round((s*(sstarve)*(swi-swa)*(1/(swi-swas))), 0)
        else:
            ss = 0
        ds = round(((sdnat)*s), 0)
        s = round(s-(ds+ss+sealh))
        sw = round((sw - ((swa*(ds+sealh))+(swa*(2/3)*ss))), 0)
        cfac = round((c-cst)*(1/(cst/100)), 0)
        cd = round((c*(cdnat+(cfac*(cfacfac)))), 0)
        c = round((c - (codh+cd) + (cbirth*c)), 0)
        #Month #2
        bearw.append(pwa)
        sealw.append(swa)
        AxisXm.append(TimeXm)
        bearm.append(p)
        sealm.append(s)
        codm.append(c)
        TimeXm = TimeXm + 1
        swa = round(sw/s, 0)
        codh = round(c*(1/cst)*s*(sealhunt))
        sw = round((sw - (sealEloss*sw) + (codh*cwas)), 0)
        iceh = round(seaice[1]/15*pst, 0)
        if p > iceh:
            sealh = round((((1/sst)*s*phunti*iceh)+((1/sst)*s*phuntn*(p-iceh))), 0)
        else:
            sealh = round(((1/sst)*s*phunti*p), 0) 
        pw = round(pw - (polarEloss*pw) + (sealh*swa*(4/5)), 0)
        pwa = round(pw/p, 0)
        if pwa<1000:
            sp = round((p*(pstarve)*(pwi-pwa)*(1/(pwi-pwas))), 0)
        else:
            sp = 0
        dp = round((p*(pdnat)), 0)
        p = round((p-(dp+sp)), 0)
        pw = round((pw - ((pwa*dp)+(pwa*(pstarvewfac)*sp))), 0)
        if swa<150:
            ss = round((s*(sstarve)*(swi-swa)*(1/(swi-swas))), 0)
        else:
            ss = 0
        ds = round(((sdnat)*s), 0)
        s = round(s-(ds+ss+sealh))
        sw = round((sw - ((swa*(ds+sealh))+(swa*(2/3)*ss))), 0)
        cfac = round((c-cst)*(1/(cst/100)), 0)
        cd = round((c*(cdnat+(cfac*(cfacfac)))), 0)
        c = round((c - (codh+cd) + (cbirth*c)), 0)
        #Month #3
        bearw.append(pwa)
        sealw.append(swa)
        AxisXm.append(TimeXm)
        bearm.append(p)
        sealm.append(s)
        codm.append(c)
        TimeXm = TimeXm + 1
        pbirth = round((pbirthfac*p*(1/2)), 0)
        p = round((p+pbirth), 0)
        pwa = round((pw/p), 0)
        sbirthi = round((sbirthfac*s), 0)
        sbirthd = round(((sbirthi)*((1-(seaice[2]/15.5))+.1)), 0)
        sbirthh = round(((sbirthi)*(p/pst)*(15.5/seaice[2])*(.4)), 0)
        sbirth = round((sbirthi - (sbirthd+sbirthh)), 0) 
        s = round((s + sbirth), 0)
        sw = round(sw - (10*(sbirthd+sbirthh)), 0)
        swa = round((sw/s), 0) 
        pw = round((pw + (10*sbirthh)), 0) 
        pwa = round((pw/p), 0)
        swa = round(sw/s, 0)
        codh = round(c*(1/cst)*s*(sealhunt)) 
        sw = round((sw - (sealEloss*sw) + (codh*cwas)), 0)
        iceh = round(seaice[2]/15*pst, 0) 
        if p > iceh:
            sealh = round((((1/sst)*s*phunti*iceh)+((1/sst)*s*phuntn*(p-iceh))), 0)
        else:
            sealh = round(((1/sst)*s*phunti*p), 0) 
        pw = round(pw - (polarEloss*pw) + (sealh*swa*(4/5)), 0) 
        pwa = round(pw/p, 0)
        if pwa<1000:
            sp = round((p*(pstarve)*(pwi-pwa)*(1/(pwi-pwas))), 0)
        else:
            sp = 0
        dp = round((p*(pdnat)), 0)
        p = round((p-(dp+sp)), 0) 
        pw = round((pw - ((pwa*dp)+(pwa*(pstarvewfac)*sp))), 0)
        if swa<150:
            ss = round((s*(sstarve)*(swi-swa)*(1/(swi-swas))), 0)
        else:
            ss = 0
        ds = round(((sdnat)*s), 0) 
        s = round(s-(ds+ss+sealh))
        sw = round((sw - ((swa*(ds+sealh))+(swa*(2/3)*ss))), 0)
        cfac = round((c-cst)*(1/(cst/100)), 0) 
        cd = round((c*(cdnat+(cfac*(cfacfac)))), 0)
        c = round((c - (codh+cd) + (cbirth*c)), 0)
        #Month #4
        bearw.append(pwa)
        sealw.append(swa)
        AxisXm.append(TimeXm)
        bearm.append(p)
        sealm.append(s)
        codm.append(c)
        TimeXm = TimeXm + 1
        pbirth = round((pbirthfac*p*(1/2)), 0)
        p = round((p+pbirth), 0)
        pwa = round((pw/p), 0)
        sbirthi = round((sbirthfac*s), 0)
        sbirthd = round(((sbirthi)*((1-(seaice[3]/15.5))+.1)), 0) 
        sbirthh = round(((sbirthi)*(p/pst)*(15.5/seaice[3])*(.4)), 0)
        sbirth = round((sbirthi - (sbirthd+sbirthh)), 0)
        s = round((s + sbirth), 0) 
        sw = round(sw - (10*(sbirthd+sbirthh)), 0) 
        swa = round((sw/s), 0)
        pw = round((pw + (10*sbirthh)), 0) 
        pwa = round((pw/p), 0)
        swa = round(sw/s, 0)
        codh = round(c*(1/cst)*s*(sealhunt))
        sw = round((sw - (sealEloss*sw) + (codh*cwas)), 0)
        iceh = round(seaice[3]/15*pst, 0)
        if p > iceh:
            sealh = round((((1/sst)*s*phunti*iceh)+((1/sst)*s*phuntn*(p-iceh))), 0)
        else:
            sealh = round(((1/sst)*s*phunti*p), 0) 
        pw = round(pw - (polarEloss*pw) + (sealh*swa*(4/5)), 0) 
        pwa = round(pw/p, 0)
        if pwa<1000:
            sp = round((p*(pstarve)*(pwi-pwa)*(1/(pwi-pwas))), 0)
        else:
            sp = 0
        dp = round((p*(pdnat)), 0)
        p = round((p-(dp+sp)), 0)
        pw = round((pw - ((pwa*dp)+(pwa*(pstarvewfac)*sp))), 0)
        if swa<150:
            ss = round((s*(sstarve)*(swi-swa)*(1/(swi-swas))), 0)
        else:
            ss = 0
        ds = round(((sdnat)*s), 0)
        s = round(s-(ds+ss+sealh)) 
        sw = round((sw - ((swa*(ds+sealh))+(swa*(2/3)*ss))), 0)
        cfac = round((c-cst)*(1/(cst/100)), 0)
        cd = round((c*(cdnat+(cfac*(cfacfac)))), 0)
        c = round((c - (codh+cd) + (cbirth*c)), 0)
        #Month #5
        bearw.append(pwa)
        sealw.append(swa)
        AxisXm.append(TimeXm)
        bearm.append(p)
        sealm.append(s)
        codm.append(c)
        TimeXm = TimeXm + 1
        swa = round(sw/s, 0)
        codh = round(c*(1/cst)*s*(sealhunt))
        sw = round((sw - (sealEloss*sw) + (codh*cwas)), 0)
        iceh = round(seaice[4]/15*pst, 0) 
        if p > iceh:
            sealh = round((((1/sst)*s*phunti*iceh)+((1/sst)*s*phuntn*(p-iceh))), 0)
        else:
            sealh = round(((1/sst)*s*phunti*p), 0)
        pw = round(pw - (polarEloss*pw) + (sealh*swa*(4/5)), 0) 
        pwa = round(pw/p, 0)
        if pwa<1000:
            sp = round((p*(pstarve)*(pwi-pwa)*(1/(pwi-pwas))), 0)
        else:
            sp = 0
        dp = round((p*(pdnat)), 0)
        p = round((p-(dp+sp)), 0)
        pw = round((pw - ((pwa*dp)+(pwa*(pstarvewfac)*sp))), 0)
        if swa<150:
            ss = round((s*(sstarve)*(swi-swa)*(1/(swi-swas))), 0)
        else:
            ss = 0
        ds = round(((sdnat)*s), 0)
        s = round(s-(ds+ss+sealh))
        sw = round((sw - ((swa*(ds+sealh))+(swa*(2/3)*ss))), 0)
        cfac = round((c-cst)*(1/(cst/100)), 0) 
        cd = round((c*(cdnat+(cfac*(cfacfac)))), 0)
        c = round((c - (codh+cd) + (cbirth*c)), 0)
        #Month #6
        bearw.append(pwa)
        sealw.append(swa)
        AxisXm.append(TimeXm)
        bearm.append(p)
        sealm.append(s)
        codm.append(c)
        TimeXm = TimeXm + 1
        swa = round(sw/s, 0)
        codh = round(c*(1/cst)*s*(sealhunt))
        sw = round((sw - (sealEloss*sw) + (codh*cwas)), 0) 
        iceh = round(seaice[5]/15*pst, 0) #Est. 777
        if p > iceh:
            sealh = round((((1/sst)*s*phunti*iceh)+((1/sst)*s*phuntn*(p-iceh))), 0) 
        else:
            sealh = round(((1/sst)*s*phunti*p), 0)
        pw = round(pw - (polarEloss*pw) + (sealh*swa*(4/5)), 0)
        pwa = round(pw/p, 0)
        if pwa<1000:
            sp = round((p*(pstarve)*(pwi-pwa)*(1/(pwi-pwas))), 0)
        else:
            sp = 0
        dp = round((p*(pdnat)), 0)
        p = round((p-(dp+sp)), 0)
        pw = round((pw - ((pwa*dp)+(pwa*(pstarvewfac)*sp))), 0)
        if swa<150:
            ss = round((s*(sstarve)*(swi-swa)*(1/(swi-swas))), 0)
        else:
            ss = 0
        ds = round(((sdnat)*s), 0)
        s = round(s-(ds+ss+sealh))
        sw = round((sw - ((swa*(ds+sealh))+(swa*(2/3)*ss))), 0)
        cfac = round((c-cst)*(1/(cst/100)), 0)
        cd = round((c*(cdnat+(cfac*(cfacfac)))), 0)
        c = round((c - (codh+cd) + (cbirth*c)), 0)
        #Month #7
        bearw.append(pwa)
        sealw.append(swa)
        AxisXm.append(TimeXm)
        bearm.append(p)
        sealm.append(s)
        codm.append(c)
        TimeXm = TimeXm + 1
        swa = round(sw/s, 0)
        codh = round(c*(1/cst)*s*(sealhunt))
        sw = round((sw - (sealEloss*sw) + (codh*cwas)), 0)
        iceh = round(seaice[6]/15*pst, 0)
        if p > iceh:
            sealh = round((((1/sst)*s*phunti*iceh)+((1/sst)*s*phuntn*(p-iceh))), 0)
        else:
            sealh = round(((1/sst)*s*phunti*p), 0)
        pw = round(pw - (polarEloss*pw) + (sealh*swa*(4/5)), 0)
        pwa = round(pw/p, 0)
        if pwa<1000:
            sp = round((p*(pstarve)*(pwi-pwa)*(1/(pwi-pwas))), 0)
        else:
            sp = 0
        dp = round((p*(pdnat)), 0)
        p = round((p-(dp+sp)), 0) 
        pw = round((pw - ((pwa*dp)+(pwa*(pstarvewfac)*sp))), 0) 
        if swa<150:
            ss = round((s*(sstarve)*(swi-swa)*(1/(swi-swas))), 0) 
        else:
            ss = 0
        ds = round(((sdnat)*s), 0) 
        s = round(s-(ds+ss+sealh)) 
        sw = round((sw - ((swa*(ds+sealh))+(swa*(2/3)*ss))), 0)
        cfac = round((c-cst)*(1/(cst/100)), 0) 
        cd = round((c*(cdnat+(cfac*(cfacfac)))), 0) 
        c = round((c - (codh+cd) + (cbirth*c)), 0)
        sbirthfac = ((1/20)*(swa/swas))
        #Month #8
        bearw.append(pwa)
        sealw.append(swa)
        AxisXm.append(TimeXm)
        bearm.append(p)
        sealm.append(s)
        codm.append(c)
        TimeXm = TimeXm + 1
        swa = round(sw/s, 0) 
        codh = round(c*(1/cst)*s*(sealhunt)) 
        sw = round((sw - (sealEloss*sw) + (codh*cwas)), 0) 
        iceh = round(seaice[7]/15*pst, 0) 
        if p > iceh:
            sealh = round((((1/sst)*s*phunti*iceh)+((1/sst)*s*phuntn*(p-iceh))), 0) 
        else:
            sealh = round(((1/sst)*s*phunti*p), 0)
        pw = round(pw - (polarEloss*pw) + (sealh*swa*(4/5)), 0) 
        pwa = round(pw/p, 0) 
        if pwa<1000:
            sp = round((p*(pstarve)*(pwi-pwa)*(1/(pwi-pwas))), 0)
        else:
            sp = 0
        dp = round((p*(pdnat)), 0) 
        p = round((p-(dp+sp)), 0) 
        pw = round((pw - ((pwa*dp)+(pwa*(pstarvewfac)*sp))), 0)
        if swa<150:
            ss = round((s*(sstarve)*(swi-swa)*(1/(swi-swas))), 0)
        else:
            ss = 0
        ds = round(((sdnat)*s), 0) 
        s = round(s-(ds+ss+sealh))
        sw = round((sw - ((swa*(ds+sealh))+(swa*(2/3)*ss))), 0) 
        cfac = round((c-cst)*(1/(cst/100)), 0)
        cd = round((c*(cdnat+(cfac*(cfacfac)))), 0)
        c = round((c - (codh+cd) + (cbirth*c)), 0) 
        #Month #9
        bearw.append(pwa)
        sealw.append(swa)
        AxisXm.append(TimeXm)
        bearm.append(p)
        sealm.append(s)
        codm.append(c)
        TimeXm = TimeXm + 1
        swa = round(sw/s, 0)
        codh = round(c*(1/cst)*s*(sealhunt)) 
        sw = round((sw - (sealEloss*sw) + (codh*cwas)), 0) 
        iceh = round(seaice[8]/15*pst, 0)
        if p > iceh:
            sealh = round((((1/sst)*s*phunti*iceh)+((1/sst)*s*phuntn*(p-iceh))), 0)
        else:
            sealh = round(((1/sst)*s*phunti*p), 0) 
        pw = round(pw - (polarEloss*pw) + (sealh*swa*(4/5)), 0) 
        pwa = round(pw/p, 0)
        if pwa<1000:
            sp = round((p*(pstarve)*(pwi-pwa)*(1/(pwi-pwas))), 0) 
        else:
            sp = 0
        dp = round((p*(pdnat)), 0)
        p = round((p-(dp+sp)), 0) 
        pw = round((pw - ((pwa*dp)+(pwa*(pstarvewfac)*sp))), 0) 
        if swa<150:
            ss = round((s*(sstarve)*(swi-swa)*(1/(swi-swas))), 0) 
        else:
            ss = 0
        ds = round(((sdnat)*s), 0)
        s = round(s-(ds+ss+sealh)) 
        sw = round((sw - ((swa*(ds+sealh))+(swa*(2/3)*ss))), 0)
        cfac = round((c-cst)*(1/(cst/100)), 0) 
        cd = round((c*(cdnat+(cfac*(cfacfac)))), 0)
        c = round((c - (codh+cd) + (cbirth*c)), 0)
        #Month #10
        bearw.append(pwa)
        sealw.append(swa)
        AxisXm.append(TimeXm)
        bearm.append(p)
        sealm.append(s)
        codm.append(c)
        TimeXm = TimeXm + 1
        swa = round(sw/s, 0)
        codh = round(c*(1/cst)*s*(sealhunt))
        sw = round((sw - (sealEloss*sw) + (codh*cwas)), 0) 
        iceh = round(seaice[9]/15*pst, 0)
        if p > iceh:
            sealh = round((((1/sst)*s*phunti*iceh)+((1/sst)*s*phuntn*(p-iceh))), 0)
        else:
            sealh = round(((1/sst)*s*phunti*p), 0)
        pw = round(pw - (polarEloss*pw) + (sealh*swa*(4/5)), 0)
        pwa = round(pw/p, 0)
        if pwa<1000:
            sp = round((p*(pstarve)*(pwi-pwa)*(1/(pwi-pwas))), 0)
        else:
            sp = 0
        dp = round((p*(pdnat)), 0)
        p = round((p-(dp+sp)), 0)
        pw = round((pw - ((pwa*dp)+(pwa*(pstarvewfac)*sp))), 0)
        if swa<150:
            ss = round((s*(sstarve)*(swi-swa)*(1/(swi-swas))), 0)
        else:
            ss = 0
        ds = round(((sdnat)*s), 0)
        s = round(s-(ds+ss+sealh))
        sw = round((sw - ((swa*(ds+sealh))+(swa*(2/3)*ss))), 0)
        cfac = round((c-cst)*(1/(cst/100)), 0)
        cd = round((c*(cdnat+(cfac*(cfacfac)))), 0)
        c = round((c - (codh+cd) + (cbirth*c)), 0)
        pbirthfac = ((1/15)*(pwa/(pwas-100)))
        #Month #11
        bearw.append(pwa)
        sealw.append(swa)
        AxisXm.append(TimeXm)
        bearm.append(p)
        sealm.append(s)
        codm.append(c)
        TimeXm = TimeXm + 1
        swa = round(sw/s, 0)
        codh = round(c*(1/cst)*s*(sealhunt)) 
        sw = round((sw - (sealEloss*sw) + (codh*cwas)), 0)
        iceh = round(seaice[10]/15*pst, 0)
        if p > iceh:
            sealh = round((((1/sst)*s*phunti*iceh)+((1/sst)*s*phuntn*(p-iceh))), 0)
        else:
            sealh = round(((1/sst)*s*phunti*p), 0)
        pw = round(pw - (polarEloss*pw) + (sealh*swa*(4/5)), 0)
        pwa = round(pw/p, 0)
        if pwa<1000:
            sp = round((p*(pstarve)*(pwi-pwa)*(1/(pwi-pwas))), 0) 
        else:
            sp = 0
        dp = round((p*(pdnat)), 0)
        p = round((p-(dp+sp)), 0)
        pw = round((pw - ((pwa*dp)+(pwa*(pstarvewfac)*sp))), 0)
        if swa<150:
            ss = round((s*(sstarve)*(swi-swa)*(1/(swi-swas))), 0)
        else:
            ss = 0
        ds = round(((sdnat)*s), 0)
        s = round(s-(ds+ss+sealh)) 
        sw = round((sw - ((swa*(ds+sealh))+(swa*(2/3)*ss))), 0)
        cfac = round((c-cst)*(1/(cst/100)), 0)
        cd = round((c*(cdnat+(cfac*(cfacfac)))), 0) 
        c = round((c - (codh+cd) + (cbirth*c)), 0)
        #Month #12
        bearw.append(pwa)
        sealw.append(swa)
        AxisXm.append(TimeXm)
        bearm.append(p)
        sealm.append(s)
        codm.append(c)
        TimeXm = TimeXm + 1
        swa = round(sw/s, 0) 
        codh = round(c*(1/cst)*s*(sealhunt))
        sw = round((sw - (sealEloss*sw) + (codh*cwas)), 0) 
        iceh = round(seaice[11]/15*pst, 0) 
        if p > iceh:
            sealh = round((((1/sst)*s*phunti*iceh)+((1/sst)*s*phuntn*(p-iceh))), 0) 
        else:
            sealh = round(((1/sst)*s*phunti*p), 0) 
        pw = round(pw - (polarEloss*pw) + (sealh*swa*(4/5)), 0) 
        pwa = round(pw/p, 0) 
        if pwa<1000:
            sp = round((p*(pstarve)*(pwi-pwa)*(1/(pwi-pwas))), 0) 
        else:
            sp = 0
        dp = round((p*(pdnat)), 0)
        p = round((p-(dp+sp)), 0)
        pw = round((pw - ((pwa*dp)+(pwa*(pstarvewfac)*sp))), 0)
        if swa<150:
            ss = round((s*(sstarve)*(swi-swa)*(1/(swi-swas))), 0)
        else:
            ss = 0
        ds = round(((sdnat)*s), 0) 
        s = round(s-(ds+ss+sealh)) 
        sw = round((sw - ((swa*(ds+sealh))+(swa*(2/3)*ss))), 0) 
        cfac = round((c-cst)*(1/(cst/100)), 0)
        cd = round((c*(cdnat+(cfac*(cfacfac)))), 0) 
        c = round((c - (codh+cd) + (cbirth*c)), 0) 
run_simulation(yr, TimeXy, TimeXm, AxisXy, AxisXm, p, s, c, pw, sw, seaice, yrc, pst, sst, cst, pwas, swas, cwas, pstarve, polarEloss, phunti, phuntn, pwi, pdnat, pstarvewfac, sstarve, swi, sdnat, cdnat, cfacfac, cbirth, pbirthfac, sbirthfac, bearw, sealw, pwa, swa, beary, bearm, sealy, sealm, cody, codm, sealhunt, sealEloss)
print("bearm: ", bearm)
print("sealm: ", sealm)
print("codm: ", codm)
print("beary: ", beary)
print("sealy: ", sealy)
print("cody: ", cody)
print("bearw: ", bearw)
print("sealw: ", sealw)
print("beary: ", beary)
print("sealy: ", sealy)
plt.plot(AxisXy, beary, marker='', label="Ursus maritimus")
plt.xlabel("time (years)")
plt.ylabel("Ursus maritimus population")
plt.title("Ursus maritimus population vs. Time")
plt.legend()
plt.grid(True)
plt.show()
input("Type something to view the next graph: ")
plt.plot(AxisXy, sealy, marker='')
plt.xlabel("time (years)")
plt.ylabel("Pusa hispida population")
plt.title("Pusa hispida population vs. Time")
plt.grid(True)
plt.show()
input("Type something to view the next graph: ")
plt.plot(beary, sealy, marker='')
plt.xlabel("Ursus maritimus population")
plt.ylabel("Pusa hispida population")
plt.title("Ursus maritimus vs. Pusa hispida")
plt.grid(True)
plt.show()
input("Type something to view the next graph: ")
plt.plot(AxisXm, bearm, marker='')
plt.xlabel("time (months)")
plt.ylabel("Ursus maritimus population")
plt.title("Ursus maritimus population vs. time (months)")
plt.grid(True)
plt.show()
input("Type something to view the next graph: ")
plt.plot(AxisXm, sealm, marker='')
plt.xlabel("time (months)")
plt.ylabel("Pusa hispida population")
plt.title("Pusa hispida population vs. time (months)")
plt.grid(True)
plt.show()
input("Type something to view the next graph: ")
plt.plot(AxisXm, bearw, marker='')
plt.xlabel("time (months)")
plt.ylabel("average weight")
plt.title("average weight vs. time")
plt.grid(True)
plt.show()
input("Type something to view the next graph: ")
plt.plot(AxisXm, sealw, marker='')
plt.xlabel("time (months)")
plt.ylabel("average weight")
plt.title("sealw vs. time")
plt.grid(True)
plt.show()
input("Type something to view the next graph: ")
fig, ax1 = plt.subplots()
ax1.plot(AxisXy, beary, color='blue', label='Ursus maritimus')
ax1.set_ylabel('Ursus maritimus population', color='blue')
ax2 = ax1.twinx()
ax2.plot(AxisXy, sealy, color='green', label='Pusa hispida')
ax2.set_ylabel('Pusa hispida population', color='green')
plt.title("Ursus maritimus & Pusa hispida Population Over Time")
plt.show()
input("Type something to view the next graph: ")
plt.plot(AxisXm, codm, marker='')
plt.xlabel("time (months)")
plt.ylabel("Boreogadus saida biomass")
plt.title("Boreogadus saida biomass vs. time")
plt.grid(True)
plt.show()
input("Type something to view the next graph: ")
plt.plot(AxisXy, cody, marker='')
plt.xlabel("time (years)")
plt.ylabel("Boreogadus saida biomass")
plt.title("Boreogadus saida biomass vs. time")
plt.grid(True)
plt.show()
input("Type something to view the next graph: ")
fig, ax1 = plt.subplots()
ax1.plot(AxisXy, beary, color='blue', label='Ursus maritimus')
ax1.set_ylabel('Ursus maritimus population', color='blue')
ax2 = ax1.twinx()
ax2.plot(AxisXy, sealy, color='green', label='Pusa hispida')
ax2.set_ylabel('Pusa hispida population', color='green')
ax3 = ax1.twinx()
ax3.spines["right"].set_position(("axes", 1.15))
ax3.plot(AxisXy, cody, color='red')
ax3.set_ylabel("Boreogadus saida population", color='red')
plt.title("Ursus maritimus, Pusa hispida, and Boreogadus saida vs. Time")
plt.show()
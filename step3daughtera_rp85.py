import sys, os

#get arguments
cmdargs = sys.argv
alpha = cmdargs[1]
year = cmdargs[2]
alpham = cmdargs[3]
yearm = cmdargs[4]
yearp4 = cmdargs[5]

os.popen('cp /work/mki005/EAS44RP85'+alpham+'/wrfrst* /work/mki005/EAS44RP85'+alpha)
os.popen('mv /work/mki005/EAS44RP85'+alpham+'/met_em*'+yearm+'* /work/mki005/EAS44RP85'+alpha)
tyme=os.popen('ls /work/mki005/EAS44RP85'+alpham+'/wrfrst*').read()
ys=tyme[-20:-16]
ms=tyme[-15:-13]
ds=tyme[-12:-10]
hs=tyme[-9:-7]

os.popen('sed /"start_year"/s/"2060"/"'+ys+'"/ WRF_EAS44RP85'+alpha+'/namelist.input > rub.input')
os.popen('mv rub.input WRF_EAS44RP85'+alpha+'/namelist.input')
# 
os.popen('sed /"start_month"/s/"01"/"'+ms+'"/ WRF_EAS44RP85'+alpha+'/namelist.input > rub.input')
os.popen('mv rub.input WRF_EAS44RP85'+alpha+'/namelist.input')
# 
os.popen('sed /"start_day"/s/"01"/"'+ds+'"/ WRF_EAS44RP85'+alpha+'/namelist.input > rub.input')
os.popen('mv rub.input WRF_EAS44RP85'+alpha+'/namelist.input')
#
os.popen('sed /"start_hour"/s/"00"/"'+hs+'"/ WRF_EAS44RP85'+alpha+'/namelist.input > rub.input')
os.popen('mv rub.input WRF_EAS44RP85'+alpha+'/namelist.input')
#
os.popen('sed /"end_year"/s/"2064"/"'+yearp4+'"/ WRF_EAS44RP85'+alpha+'/namelist.input > rub.input')
os.popen('mv rub.input WRF_EAS44RP85'+alpha+'/namelist.input')

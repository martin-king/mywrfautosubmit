import os

yearstart=range(2075,2090,5)

alphabets=map(chr,range(65, 91))
#count=0 is A, count=1 is B...
count=15

jobie='1028017'

for y in yearstart:
# os.popen('cp /work/mki005/EAS44RP85'+alphabets[count-1]+'/wrfrst* /work/mki005/EAS44RP85'+alphabets[count])
# os.popen('mv /work/mki005/EAS44RP85'+alphabets[count-1]+'/met_em*'+str(y-1)+'* /work/mki005/EAS44RP85'+alphabets[count])
# tyme=os.popen('ls /work/mki005/EAS44RP85'+alphabets[count-1]+/wrfrst*').read()
# ys=tyme[-20:-16]
# ms=tyme[-15:-13]
# ds=tyme[-12:-10]
# hs=tyme[-9:-7]
# os.popen('sed /"start_year"/s/"1950"/"'+str(ys)+'"/ WRF_EAS44RP85'+alphabets[count]+'/namelist.input > rub.input')
# os.popen('mv rub.input WRF_EAS44RP85'+alphabets[count]+'/namelist.input')
# os.popen('sed /"start_month"/s/"01"/"'+str(ms)+'"/ WRF_EAS44RP85'+alphabets[count]+'/namelist.input > rub.input')
# os.popen('mv rub.input WRF_EAS44RP85'+alphabets[count]+'/namelist.input')
# os.popen('sed /"start_day"/s/"01"/"'+str(ds)+'"/ WRF_EAS44RP85'+alphabets[count]+'/namelist.input > rub.input')
# os.popen('mv rub.input WRF_EAS44RP85'+alphabets[count]+'/namelist.input')
# os.popen('sed /"start_hour"/s/"00"/"'+str(hs)+'"/ WRF_EAS44RP85'+alphabets[count]+'/namelist.input > rub.input')
# os.popen('mv rub.input WRF_EAS44RP85'+alphabets[count]+'/namelist.input')
# os.popen('sed /"end_year"/s/"1954"/"'+str(y+4)+'"/ WRF_EAS44RP85'+alphabets[count]+'/namelist.input > rub.input')
# os.popen('mv rub.input WRF_EAS44RP85'+alphabets[count]+'/namelist.input')

 jobia=os.popen('qsub -W depend=afterok:'+jobie[0:7]+' -v ALPHA="'+alphabets[count]+'",YEAR="'+str(y)+ \
                '",ALPHAM="'+alphabets[count-1]+'",YEARM="'+str(y-1)+'",YEARP4="'+str(y+4)+'"'+ \
                ' ./RUN_PYTHON_RP85.sh').read()
 jobid=os.popen('qsub -W depend=afterok:'+jobia[0:7]+' -v EXP="EAS44RP85'+alphabets[count]+ \
                '" WRF_EAS44RP85'+alphabets[count]+'/RUN_WRF_REAL.sh').read()
 jobie=os.popen('qsub -W depend=afterok:'+jobid[0:7]+' -v EXP="EAS44RP85'+alphabets[count]+ \
                '" WRF_EAS44RP85'+alphabets[count]+'/RUN_WRF_EXE.sh').read()
 count=count+1

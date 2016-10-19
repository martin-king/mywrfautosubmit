import os

yearstart=range(2065,2090,5)

alphabets=map(chr,range(65, 91))

count=13

for y in yearstart:
 jobid=os.popen('qsub -v EXP="EAS44RP85'+alphabets[count]+'" WRF_EAS44RP85'+alphabets[count]+'/RUN_WRF_GEO_UNGRIB.sh').read()
 jobie=os.popen('qsub -W depend=afterok:'+jobid[0:7]+' -v EXP="EAS44RP85'+alphabets[count]+'" WRF_EAS44RP85'+alphabets[count]+'/RUN_WRF_METGRID.sh').read()
#jobie=os.popen('qsub -v EXP="EAS44RP85'+alphabets[count]+'" WRF_EAS44RP85'+alphabets[count]+'/RUN_WRF_METGRID.sh').read()
 count=count+1

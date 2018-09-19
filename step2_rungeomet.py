#To run: python step2_rungeomet.py

import os

# 5-year long experiments starting 2065, 2070...
yearstart=range(2065,2090,5)

alphabets=map(chr,range(65, 91))
#count=0 is A, count=1 is B...
count=13

for y in yearstart:
# submit batch script (RUN_WRF_GEO_UNGRIB.sh) for geogrid and ungrib
 jobid=os.popen('qsub -v EXP="EAS44RP85'+alphabets[count]+'" WRF_EAS44RP85'+alphabets[count]+ \
                '/RUN_WRF_GEO_UNGRIB.sh').read()
# jobid from above is used as dependency to start next line to submit
# batch script (RUN_WRF_METGRID.sh)
 jobie=os.popen('qsub -W depend=afterok:'+jobid[0:7]+' -v EXP="EAS44RP85'+alphabets[count]+ \
                '" WRF_EAS44RP85'+alphabets[count]+'/RUN_WRF_METGRID.sh').read()
#jobie=os.popen('qsub -v EXP="EAS44RP85'+alphabets[count]+'" WRF_EAS44RP85'+alphabets[count]+'/RUN_WRF_METGRID.sh').read()
 count=count+1

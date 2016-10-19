yearstart=range(2065,2090,5)

alphabets=map(chr,range(65, 91))

count=13

for y in yearstart:
  print "mkdir WRF_EAS44RP85"+alphabets[count]
  print "cd WRF_EAS44RP85M"
  print "cp -r * ../WRF_EAS44RP85"+alphabets[count]
  print "cd ../WRF_EAS44RP85"+alphabets[count]
  print 'sed /"start_date"/s/"2060"/"'+str(y)+'"/ namelist.wps > rub.wps'
  print "mv rub.wps namelist.wps"
  print 'sed /"end_date"/s/"2064"/"'+str(y+4)+'"/ namelist.wps > rub.wps'
  print "mv rub.wps namelist.wps"
  print 'sed /"restart"/s/"false"/"true"/ namelist.input > rub.input'
  print "mv rub.input namelist.input"
  print "cd .."
  print "mkdir /work/mki005/EAS44RP85"+alphabets[count]
  for i in range(0,5):
     print "ln -s /work/shared/bjerknes/mki005/noresm2wrfim.dir/OUTPUT_rcp85/*"+str(y+i)+"* /work/mki005/EAS44RP85"+alphabets[count]+"/."
  count=count+1

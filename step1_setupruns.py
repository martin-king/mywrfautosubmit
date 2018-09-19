% To run: python step1_setupruns.py > doit
% Then check doit, chmod a+x doit, ./doit
  
yearstart=range(2065,2090,5)

alphabets=map(chr,range(65, 91))

count=13

for y in yearstart:
% In home, make new folder to contain experiment scripts
  print "mkdir WRF_EAS44RP85"+alphabets[count]
  print "cd WRF_EAS44RP85M"
% copy previously set up files to the new folder
  print "cp -r * ../WRF_EAS44RP85"+alphabets[count]
% go to the new folder  
  print "cd ../WRF_EAS44RP85"+alphabets[count]
% change start year in namelist.wps  
  print 'sed /"start_date"/s/"2060"/"'+str(y)+'"/ namelist.wps > rub.wps'
  print "mv rub.wps namelist.wps"
% change end year in namelist.wps (these are five-year runs)
  print 'sed /"end_date"/s/"2064"/"'+str(y+4)+'"/ namelist.wps > rub.wps'
  print "mv rub.wps namelist.wps"
% change restart to true in namelist.input
  print 'sed /"restart"/s/"false"/"true"/ namelist.input > rub.input'
  print "mv rub.input namelist.input"
  print "cd .."
% make experiment folder in work
  print "mkdir /work/mki005/EAS44RP85"+alphabets[count]
% make links to input files in work 
  for i in range(0,5):
     print "ln -s /work/shared/bjerknes/mki005/noresm2wrfim.dir/OUTPUT_rcp85/*"+str(y+i)+"*  \
      /work/mki005/EAS44RP85"+alphabets[count]+"/."
  count=count+1

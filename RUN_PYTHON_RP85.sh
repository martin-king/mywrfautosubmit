#!/bin/sh
#
#  Make sure I use the correct shell.
#
#PBS -S /bin/sh
#
#  Give the job a name
# 
#PBS -N "MY_PY"
#
#  Specify the project the job belongs to
#
#PBS -A bjerknes 
#
#PBS -l walltime=01:00:00,mppwidth=1
#
#  The job needs 8000 MB memory per process:
####PBS -l mppmem=1000mb
#
#
#  Write the standard output of the job to file 'mpijob.out' (optional)
#PBS -o MY_PY.out
#
#  Write the standard error of the job to file 'mpijob.err' (optional)
#PBS -e MY_PY.err
#
# ##################################################################################

# USAGE: $ qsub -v EXP="TEST" RUN_WRF_HEXAGON.sh

# Export variables
export PATH=$PATH:/usr/local/bin:/usr/etc:~/bin:./

# directory where this script is located:
HDIR="$HOME"

cd $HOME
python step3daughtera_rp85.py "$ALPHA" "$YEAR" "$ALPHAM" "$YEARM" "$YEARP4"

exit $?

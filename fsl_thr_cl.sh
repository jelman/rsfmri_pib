#!/bin/bash

if [ $# -eq 0 ]; then
	echo "Usage: fsl_thr_cl FILENAME DHL VOL ZTHR PTHR OFILE"
	exit 0
fi

FILE=$1;
FILENAME=`basename $FILE`;
DIR=${FILE/$FILENAME/};
N=${FILENAME/.nii.gz/}; N=`expr match $N '.*\([a-z][0-9]*\)'`; N=${N:1:${#N}-1};
 
DHL=$2;
VOL=$3;
THR=$4;
P=$5;
 
if [ ${6} ]; then
	OFILE=$6;
	OFILENAME=`basename $OFILE`;
	ODIR=${OFILE/$OFILENAME/};

	if [[ ! -d "${ODIR}" ]]; then
		mkdir ${ODIR}
	fi
	${FSLDIR}/bin/fslmaths ${FILE} -mas ${DIR}../mask ${OFILE}
	${FSLDIR}/bin/cluster -i ${OFILE} -c ${DIR}cope${N} -t ${THR} -p ${P} -d ${DHL} --volume=${VOL} --othresh=${OFILE} >> /dev/null
else
	${FSLDIR}/bin/fslmaths ${FILE} -mas ${DIR}../mask /tmp/out
	${FSLDIR}/bin/cluster -i /tmp/out -c ${DIR}cope${N} -t ${THR} -p ${P} -d ${DHL} --volume=${VOL} >> /tmp/out
	for E in `cat /tmp/out | awk '{print $2}'`; do tmp=$E; done;
	if (( $E == Index )); then E=0; fi;
	echo -e "$THR\t$E";
	rm /tmp/out.nii.gz /tmp/out
fi

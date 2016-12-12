#!/bin/bash
#$ -M kmeranda@nd.edu	# email when done
#$ -m abe		# email when done
#$ -q *@@nlp-gpu	# which queue
#$ -l gpu=1		# am using a gpu

module load keras
#module load tensorflow
export CUDA_VISIBLE_DEVICES=`/afs/crc.nd.edu/group/nlp/software/crc/findgpu.pl`
fsync -d 30 output.log &
python MLP.py > output.txt 2>&1


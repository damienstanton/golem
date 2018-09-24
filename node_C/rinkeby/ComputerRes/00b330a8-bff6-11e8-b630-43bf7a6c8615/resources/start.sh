#!/bin/bash

GOLEM_OUTPUT=/golem/output
mkdir -p $GOLEM_OUTPUT/out1
cp resource/resource1.txt .
cp resource/resource1.txt $MY_DIR
cp resource/resource1.txt $GOLEM_OUTPUT/out1

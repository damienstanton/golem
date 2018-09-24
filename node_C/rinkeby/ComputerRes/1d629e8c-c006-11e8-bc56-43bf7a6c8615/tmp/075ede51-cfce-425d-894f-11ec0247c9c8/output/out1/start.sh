#!/bin/bash

GOLEM_OUTPUT=/golem/output
GOLEM_RESOURCES=/golem/resources
echo "no elo"
mkdir -p $GOLEM_OUTPUT/out1
touch $GOLEM_OUTPUT/out1/somefile
cp $GOLEM_RESOURCES/start.sh $GOLEM_OUTPUT/out1/

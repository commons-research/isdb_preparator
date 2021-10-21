#!/bin/sh 

sudo docker run --rm=true -v $(pwd):/cfmid/public/ -i wishartlab/cfmid:latest sh -c "cd /cfmid/public/; cfm-predict opennpdb_0002.txt 0.001 /trained_models_cfmid4.0/[M+H]+/param_output.log /trained_models_cfmid4.0/[M+H]+/param_config.txt 1 output_cfm/output_opennpdb_0002" &> /dev/null
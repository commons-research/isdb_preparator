#!/bin/sh 


sudo docker run --rm=true -v /home/allardpm/cfm:/cfmid/public/ -i wishartlab/cfmid:latest sh -c "cd /cfmid/public/; cfm-predict cfm_input/splitted/lotus_to_frag_00000.txt 0.001 /trained_models_cfmid4.0/[M+H]+/param_output.log /trained_models_cfmid4.0/[M+H]+/param_config.txt 1 cfm_output/" & >/dev/null
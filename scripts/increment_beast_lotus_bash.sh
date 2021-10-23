for ((i=0; i<=290; i++)); do
   printf -v fn '%05d' $i
   test
   sed "s/lotus_to_frag_00000/lotus_to_frag_${fn}/g" ../beast_lotus/bash_beast_lotus_template.sh > "../beast_lotus/bash_beast_lotus_${fn}.sh" 
done
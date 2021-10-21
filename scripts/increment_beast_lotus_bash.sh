for ((i=0; i<=10; i++)); do
   printf -v fn '%04d' $i
   test
   sed "s/opennpdb_0000/opennpdb_${fn}/g" ../beast_lotus/bash_beast_lotus_template.sh > "../beast_lotus/bash_beast_lotus_${fn}.sh" 
done
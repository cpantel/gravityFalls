for test in test*.py; do 
   echo "####################### $test #####################"
   python "$test"
done

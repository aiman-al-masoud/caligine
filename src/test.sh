
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'
TEST_DIR='src/examples'
FILTER=$1

for test in $(ls "$TEST_DIR" | egrep '^test' | egrep "$FILTER" )
do
    ./src/main.py "$TEST_DIR/$test" > /dev/null
    test_result=$?

    if [ $test_result == 1 ]
    then
        echo -e "$RED FAIL $test $NC" 
    elif [ $test_result == 0 ]
    then
        echo -e "$GREEN OK $test $NC" 
    fi

done

#! bin/bash 

if [ -z $1 ]
then 
		echo "first parameter is null"
else
		echo "first parameter is not null"
fi 

if [ -n $2 ]
then
		echo "$2 is not null"
else
		echo "$2 is null"
fi 

if [ 10 -gt 5 ] 
then
		echo "Happy Happy Happy"
fi

if [[ $1 == $2 ]]
then 
		echo "SAME"
else 
		echo "NOT SAME"
fi 

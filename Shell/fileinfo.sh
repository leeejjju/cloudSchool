#! /bin/bash

if [ -f $1 ] 
then 
		if [ -L $1 ] 
				then echo "SYMBOLIC LINK"
				else echo "FILE"
		fi 
else echo "NOT A FILE"
fi

if [ -s $1 ]
then 
		if [ -O $1 ]
		then echo "and it's yours"
		else echo "and it's not yours"
		fi
fi

if [ -r $1 ]
then echo "You can read it"
fi

if [ -w $1 ]
then echo "You can write on it"
fi

if [ -x $1 ]
then echo "You can execute it"
fi 


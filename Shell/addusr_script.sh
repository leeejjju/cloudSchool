# 셔뱅shebang: 파일에 대한 설명 
#! /bin/bash

# 매개변수 두 개: ID와 PW를 입력했는지 확인 
if [[ -n $1 ]] && [[ -n $2 ]]
then 
		UserList=($1)
		Password=($2)

		# UserList를 돌면서 do 이하의 작업을 하는 반복문 
		for (( i=0; i<${#UserList[@]}; i++))
		do
				# 기존 유저 리스트에 없는 사용자라면... 
				if [[ $(cat /etc/passwd | grep ${UserList[$i]} | wc -l) == 0 ]] 
				then 
						# useradd를 수행하고 
						sudo useradd ${UserList[$i]}
						# Passwd[i]를 뒤 passwd 명령의 stdin으로 집어넣음 
						echo ${Passwd[$i]} | sudo passwd ${UserList[$i]} 
				else 
						# 만약 계정이 존재하면 이미 있다고 메시지 출력 
						echo "This user ${UserList[$i]} is existing."
				fi

		done
		
else
		# 매개변수가 올바르게 들어오지 않았을 경우 
		echo 'Please input user id and password.'
		echo -e "Usage: ./$0 \"user01 user02\" \"pw01 pw02\""
fi

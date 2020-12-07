#!/bin/bash
input="input.txt"
matches=0
while IFS= read -r line
do
number1=`echo -n "$line" | awk '{print $1}' | cut -f1 -d"-"`
number2=`echo -n "$line" | awk '{print $1}' |cut -f2 -d"-"`
letter=`echo -n "$line" | awk '{print $2}' | egrep -o "^."`
password=`echo -n "$line" | awk '{print $3}'`
hit1=`echo -n "$password" | cut -c${number1}`
hit2=`echo -n "$password" | cut -c${number2}`

if [ "$hit1" == "$letter" ] && [ "$hit2" != "$letter" ]; then
matches=$((matches+1))
fi

if [ "$hit1" != "$letter" ] && [ "$hit2" == "$letter" ]; then
matches=$((matches+1))
fi

#echo $matches
done < "$input"
echo $matches

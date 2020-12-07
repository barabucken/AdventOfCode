#!/bin/bash
input="input.txt"

matches=0

while IFS= read -r line
do

number1=`echo -n "$line" | awk '{print $1}' | cut -f1 -d"-"`
number2=`echo -n "$line" | awk '{print $1}' |cut -f2 -d"-"`
letter=`echo -n "$line" | awk '{print $2}' | egrep -o "^."`
password=`echo -n "$line" | awk '{print $3}'`
testhits=`echo -n "$line" | awk '{print $3}' | grep -o "$letter" | wc -l`


if ((testhits >= $number1 && testhits <= $number2)); then
matches=$((matches+1))
fi

echo $matches


done < "$input"

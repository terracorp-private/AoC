#!/bin/bash

pattern=^000
hash="bgvyzdsv"
postfix=0

while true
do
    hash=$(echo -n $hash$postfix | md5sum)
    if [[ $hash =~ $pattern ]]; then
        echo $hash
        echo $postfix
        break
    fi
    let "postfix++"
done


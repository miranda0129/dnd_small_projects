#!/bin/bash

echo "Welcome to the D&D Race Search Tool!"
echo "------------------------------------"
echo

read -p "Enter the name of a D&D race: " race_name

curl -L "https://www.dnd5eapi.co/api/races/$race_name" -H 'Accept: application/json' | python3 -m json.tool

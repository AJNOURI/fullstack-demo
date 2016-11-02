#!/bin/bash
for i in {1..100}; do echo 'db.credentials.insert({"name":"'name$i'","surname":"'surname$i'","login":"'login$i'","passowrd":"'password$i'"})';done

#!/bin/bash
if  [ "$1" = "" ] ; then
  mongorestore /backup/mongodb-latest/
else
  mongorestore /backup/mongodb-$1/
fi

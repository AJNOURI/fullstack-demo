#!/bin/bash
mongodump --out /backup/mongodb-$(date +"%d-%m-%Y-%H:%M:%S")
mongodump --out /backup/mongodb-latest

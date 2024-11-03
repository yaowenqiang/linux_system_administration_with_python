#!/usr/bin/env bash

function uname_func() 
{
  UNAME='uname -a'
  printf "Gathering system information with $UNAME command"
  $UNAME
}

function disk_func() 
{
  DISKSPACE='df -h'
  printf "Gathering system information with $DISKSPACE command"
  $DISKSPACE
}

function main() {
  uname_func
  disk_func
}

main

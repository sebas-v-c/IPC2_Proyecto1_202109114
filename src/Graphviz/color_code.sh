#!/usr/bin/env sh


echo -n "$1" | md5sum | cut -c1-6

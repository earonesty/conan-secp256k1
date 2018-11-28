# Conan packager for secp256k1

Bitcoin's libsecp256k1 packaged for conan.io / cmake.  Mostly used as an example. 

## Overview

1. Don't use binaries of this package that were uploaded to bintray, uninstead use your own internal conan repo, and use this packager to build it from source

2. To use, fork this repo, modify the the "upload.sh", "build.py" and other things with your own parameters.   This repo is mostly just an example of autotools->conan....!


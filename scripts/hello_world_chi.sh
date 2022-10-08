#!/bin/bash
# LANGUAGE: bash
# DESCRIPTION: decode the text "Hello, World!" encrypted by base64

echo Hello, World! | base64 | base64 -d

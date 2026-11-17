#!/bin/bash

echo "========== Docker File =========="
cat Dockerfile

echo "========== Docker Ignore File =========="
cat .dockerignore

echo "========== Requirements File =========="
cat requirements.txt

echo "========== Main Application File =========="
cat app/main.py

echo "========== Test File =========="
cat tests/test_app.py
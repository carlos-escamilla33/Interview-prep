#!/bin/bash
echo "What has been changed?"

read comment

git add .
git commit -m "$comment"
git push
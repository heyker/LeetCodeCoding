#########################################################################
# File Name: commit.sh
# Author: heyker
# Mail: heyker.he@gmail.com
# Created Time: 2017年01月22日 星期日 10时35分01秒
#########################################################################
#!/bin/bash
git add .
git commit -m "update files"

git remote add origin git@github.com:heyker/LeetCodeCoding.git
git push -u origin master

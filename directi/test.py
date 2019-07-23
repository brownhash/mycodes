import os
import stat

inode = os.lstat("process.log")[stat.ST_INO]

print(inode)
# List of Linux Commands
## A Quick Reference Guide for Every Linux User

---

## 1. Basic Linux Commands

| Command | Description |
|---------|-------------|
| `pwd` | Display the current working directory. |
| `ls` | List files and directories. |
| `ls -l` | Display files in long format. |
| `ls -a` | Show hidden files. |
| `cd directory_name` | Change to another directory. |
| `cd ..` | Move one directory up. |
| `mkdir directory_name` | Create a new directory. |
| `mkdir -p dir1/dir2/dir3` | Create nested directories. |
| `touch file.txt` | Create an empty file. |
| `touch file1 file2 file3` | Create multiple files at once. |
| `rm file.txt` | Remove a file. |
| `rm -r directory_name` | Remove a directory and its contents. |
| `echo "Hello"` | Print text to the terminal. |
| `history` | Display previously executed commands. |
| `clear` | Clear the terminal screen. |
| `cat file.txt` | Display the contents of a file. |

---

## 2. Linux Editors

| Editor/Command | Purpose |
|----------------|---------|
| `nano filename` | Beginner-friendly text editor. |
| `vi filename` | Open a file in the Vi editor. |
| `vim filename` | Advanced version of Vi with more features. |
| `cat &gt; filename` | Create or edit a file directly from the terminal. |
| `sed` | Stream editor used for searching, replacing, and editing text. |

---

## 3. File Management Commands

| Command | Description |
|---------|-------------|
| `cp source destination` | Copy files or directories. |
| `cp -r source destination` | Copy directories recursively. |
| `mv source destination` | Move a file or directory. |
| `mv oldname newname` | Rename a file or directory. |

---

## 4. Disk Usage Commands

| Command | Description |
|---------|-------------|
| `df -h` | Display disk space usage in a human-readable format. |
| `du -sh directory_name` | Show the total size of a directory. |

---

## 5. User Management Commands

| Command | Description |
|---------|-------------|
| `useradd username` | Create a new user. |
| `passwd username` | Set or change a user's password. |
| `userdel username` | Delete a user account. |
| `userdel -r username` | Delete a user along with their home directory. |
| `usermod -l newname oldname` | Rename an existing user. |
| `usermod -u USER_ID username` | Change a user's User ID (UID). |

---

## 6. Group Management Commands

| Command | Description |
|---------|-------------|
| `groupadd groupname` | Create a new group. |
| `gpasswd groupname` | Set or manage the group's password. |
| `cat /etc/group` | Display all groups on the system. |
| `usermod -aG groupname username` | Add a user to a supplementary group. |
| `gpasswd -a username groupname` | Add a user to a group. |
| `groupdel groupname` | Delete an existing group. |

---

&gt; **Quick Tip:** Practice these commands in your terminal regularly. The more you use them, the more powerful you become in Linux!

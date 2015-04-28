SrvIt
=====

A Simple Web Server to share files, written because AirDrop is horrible.

Usage: sudo python srvit.py [file1] [file2]
--
It will generate an index.html listing the files you've listed.

Note that it will share the entire directory the files you are sharing.

Also note it uses multiprocessing to spawn a new PID to sanely kill it.

Release Notes
--
v0.2 - Added code to get and show your IP address. 

v0.1 - Initial Release

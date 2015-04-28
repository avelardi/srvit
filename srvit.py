#!/usr/bin/env python
# encoding: utf-8
"""
srvit.py
Simple, temporary webserver. It'll generate an index.html file for the files you list. 
Note this does not validate if the files are there. 

I also did not like slaughtering the server, so it runs using multiprocessing.process. 

Created by Tony Velardi
"""

import sys
import os
import getopt
import SimpleHTTPServer
import SocketServer
import multiprocessing

port = 80
indexfilename = 'index.html'

def htmlgen(itemlist):
	indexfile = open(indexfilename, 'w')
	html_file_begin = """
	<!DOCTYPE html>
	<html lang="en">
	<head>
	  <meta charset="utf-8">
	  <title>Can Haz Fielz</title>
	  <meta name="viewport" content="width=device-width, initial-scale=1.0">
	  <meta name="description" content="">
	  <meta name="author" content="">

		<!--link rel="stylesheet/less" href="less/bootstrap.less" type="text/css" /-->
		<!--link rel="stylesheet/less" href="less/responsive.less" type="text/css" /-->
		<!--script src="js/less-1.3.3.min.js"></script-->
		<!--append ‘#!watch’ to the browser URL, then refresh the page. -->

		<link href="css/bootstrap.min.css" rel="stylesheet">
		<link href="css/style.css" rel="stylesheet">

	  <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
	  <!--[if lt IE 9]>
	    <script src="js/html5shiv.js"></script>
	  <![endif]-->

	  <!-- Fav and touch icons -->
	  <link rel="apple-touch-icon-precomposed" sizes="144x144" href="img/apple-touch-icon-144-precomposed.png">
	  <link rel="apple-touch-icon-precomposed" sizes="114x114" href="img/apple-touch-icon-114-precomposed.png">
	  <link rel="apple-touch-icon-precomposed" sizes="72x72" href="img/apple-touch-icon-72-precomposed.png">
	  <link rel="apple-touch-icon-precomposed" href="img/apple-touch-icon-57-precomposed.png">
	  <link rel="shortcut icon" href="img/favicon.png">

		<script type="text/javascript" src="js/jquery.min.js"></script>
		<script type="text/javascript" src="js/bootstrap.min.js"></script>
		<script type="text/javascript" src="js/scripts.js"></script>
	</head>

	<body>
	<div class="container">
		<div class="row clearfix">
			<div class="col-md-12 column">
				<h3 class="text-center">
					Schedules
				</h3>
				<div class="row clearfix">
					<div class="col-md-4 column">
					</div>
					<div class="col-md-4 column">
					"""
					
	html_file_end = """</div>
					<div class="col-md-4 column">
					</div>
				</div>
				<blockquote class="pull-right">
					 <small><span>"The words of avelardi are both invaluable and worthless"</span></small><small>Abraham Lincoln</small>
				</blockquote>
			</div>
		</div>
	</div>
	</body>
	</html>"""
	buttonList = []
	for item in itemlist:
		button = "<a href=/"+ item + " class=\"btn btn-block btn-primary btn-default\">" + item + "</a> "
		buttonList.append(button)
	#combine 'em all
	buttonHtml = ''.join(str(x) for x in buttonList)
	finalHtml = html_file_begin + buttonHtml + html_file_end
	indexfile.write(finalHtml)
	indexfile.close()

def threadprocess(httpd):
	httpd.serve_forever()

def webserver(args):
	Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
	httpd = SocketServer.TCPServer(("", port), Handler)
	print "File list:"
	for arg in args:
		print arg
	p = multiprocessing.Process(target=threadprocess, args=(httpd,))
	p.start()
	raw_input("Server running, hit enter to kill")
	p.terminate()
	
def main(args):
	#take list of args as files, gen html
	htmlgen(args)
	#run server
	webserver(args)	

if __name__ == '__main__':
	main(sys.argv[1:])


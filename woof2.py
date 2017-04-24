
#import sys, os, errno, socket, getopt, commands, tempfile
#import cgi, urllib, urlparse, BaseHTTPServer
#import readline
#import ConfigParser
#import shutil, tarfile, zipfile
#import struct

import SimpleHTTPServer
import SocketServer
import os
import sys
import getopt

config = {
		"port": 8888,
		"address": 'machinename',
		"maxdownloads": 1,
		"upload": False,
}


def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)
    
def usage (defport, defmaxdown, errmsg = None):
        name = os.path.basename(sys.argv[0])
        print >>sys.stderr, """
        Usage: %s [-i <ip_addr>] [-p <port>] [-c <count>] <file>
           %s [-i <ip_addr>] [-p <port>] [-c <count>] [-z|-j|-Z|-u] <dir>
           %s [-i <ip_addr>] [-p <port>] [-c <count>] -s
           %s [-i <ip_addr>] [-p <port>] [-c <count>] -U

           %s <url>
   
        Serves a single file <count> times via http on port <port> on IP
        address <ip_addr>.
        When a directory is specified, an tar archive gets served. By default
        it is gzip compressed. You can specify -z for gzip compression, 
        -j for bzip2 compression, -Z for ZIP compression or -u for no compression.
        You can configure your default compression method in the configuration 
        file described below.
    
        When -s is specified instead of a filename, %s distributes itself.
    
        When -U is specified, woof provides an upload form, allowing file uploads.
       
        defaults: count = %d, port = %d
    
        If started with an url as an argument, woof acts as a client,
        downloading the file and saving it in the current directory.
    
        You can specify different defaults in two locations: /etc/woofrc
        and ~/.woofrc can be INI-style config files containing the default
        port and the default count. The file in the home directory takes
        precedence. The compression methods are "off", "gz", "bz2" or "zip".
    
        Sample file:
    
            [main]
            port = 8008
            count = 2
            ip = 127.0.0.1
            compressed = gz
        """ % (name, name, name, name, name, name, defmaxdown, defport)

        if errmsg:
                print >> sys.stderr, errmsg
                print >> sys.stderr
                sys.exit(1)

def main():
        try:
                options, filenames = getopt.getopt (sys.argv[1:], "hUszjZui:c:p:")
        except getopt.GetoptError, desc:
                usage(config['port'], config['maxdownloads'], desc)
                
        for option, value in options:
                if option == '-c':
                        try:
                                config['maxdownloads'] = int(value)
                                if maxdown <= 0:
                                        raise ValueError
                        except ValueError:
                                usage(config['port'], config['maxdownloads'], "invalid download count: %r. Please specify an integer >= 0." % value)
                elif option == '-i':
                        config['address'] = value
                elif option == '-p':
                        try:
                                config['port']= int(value)
                        except ValueError:
                                usage(config['port'], config['maxdownloads'], "invalid port number: %r. Please specify an integer" % value)
                elif option == '-s':
                        filenames.append (__file__)
                elif option == '-h':
                        usage(config['port'], config['maxdownloads'])
                elif option == '-U':
                        config['upload'] = True
                elif option == '-z':
                        compressed = 'zip'
                elif option == '-u':
                        compressed = ''
                else:
                        usage(config['port'], config['maxdownloads'], "Unknown option: %r" % option)
                        
        #Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
		#httpd = SocketServer.TCPServer((config['address'], config['port']), Handler)


  #print "serving at port", PORT
  #httpd.serve_forever()

if __name__=='__main__':
   try:
      main ()
   except KeyboardInterrupt:
      print

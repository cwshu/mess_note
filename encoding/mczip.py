"""
This script is from: http://www.robberphex.com/2013/05/141
"""
#!/usr/bin/python2
# -*- coding: utf-8 -*- 
 
import os
import sys
import zipfile
from optparse import OptionParser
 
def listZip(zipf):
    print "Archive:  %s" %zipf
    print "  Length      Date    Time    Name"
    print "---------  ---------- -----   ----"
    filist=zipfile.ZipFile(zipf).infolist()
    totalnum=0
    totalsize=0
    for finfo in filist:
        totalnum+=1
        totalsize+=finfo.file_size
        print "%9d " %finfo.file_size ,
        print "%04d-%02d-%02d" %(finfo.date_time[0],finfo.date_time[1],finfo.date_time[2]),
        print "%02d:%02d  " %(finfo.date_time[3],finfo.date_time[4]),
        print finfo.filename.decode('gb18030').encode('utf-8')
    print "---------                     -------"
    print "%9d" %totalsize ,
    print "                   ",
    print "%d files" %totalnum
 
def exZip(zipf,exdir):
    zf=zipfile.ZipFile(zipf)
    nlist=zf.namelist()
    nlist.sort(key=lambda x:len(x))
    for fn in nlist:
        fnew=unicode(fn,'gb2312').encode('utf8')
        if fnew.endswith('/'):
            os.mkdir(exdir+fnew)
        else:
            file(exdir+fnew,'wb').write(zf.read(fn))
        print fnew
    zf.close()
 
def main():
    usage = "usage: "+sys.argv[0]+" [options] zipfile1 zipfile2"
    parser = OptionParser(usage=usage)
    parser.add_option("-l","--list",action="store_true",help="list files in zip file",dest="islist",default=True)
    parser.add_option("-x","--extract",action="store_true",help="extract zip files",dest="isex",default=False)
    parser.add_option("-d","--exdir",action="store",help="define extract directory",dest="exdir",default=".")
    #parser.add_option("-z","--exdir",action="store",dest="exidr")
 
    (options,args)=parser.parse_args();
 
    if(options.isex):
        for zf in args:
            exZip(zf,options.exdir+"/")
    else:
        if(options.islist):
            for zf in args:
                listZip(zf)
 
if __name__ == "__main__":
    main()

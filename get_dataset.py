# encoding: utf-8
import urllib2

BLOCK_SIZE = 8192

def download_file(file_url):
    """ Download a file from the given file_url and returns the name with which it was saved """

    file_name = file_url.split('/')[-1]
    response = urllib2.urlopen(file_url)

    with open(file_name, 'wb') as file:
        total_bytes = int(response.info().getheaders("Content-Length")[0])
        print "Descargando archivo: %s" % (file_name)
        print "Tamaño: %s KBs" % (total_bytes/1024.0)

        while True:
            buffer = response.read(BLOCK_SIZE)
            if not buffer:
                break
            file.write(buffer)
    return file_name

data_set_url = "http://files.grouplens.org/datasets/movielens/ml-1m.zip"
download_file(data_set_url)
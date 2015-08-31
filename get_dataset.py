# encoding: utf-8
import urllib2
import sys

BLOCK_SIZE   = 8192
FULL_SQUARE  = "█"
EMPTY_SQUARE = " "
BACKSPACE    = chr(8)
TOTAL_BAR_LENGTH = 70
EXAMPLE_DATASET_URL = "http://files.grouplens.org/datasets/movielens/ml-1m.zip"

def download_file(file_url):
    """ Download a file from the given file_url and returns the name with which it was saved """

    file_name = file_url.split('/')[-1]
    response = urllib2.urlopen(file_url)

    with open(file_name, 'wb') as file:
        total_bytes = int(response.info().getheaders("Content-Length")[0])
        print "Descargando archivo: %s" % (file_name)
        print "Tamaño: %s KBs" % (total_bytes/1024.0)

        downloaded_bytes = 0
        while True:
            buffer = response.read(BLOCK_SIZE)
            if not buffer:
                break

            downloaded_bytes += len(buffer)
            file.write(buffer)
            write_progress_bar(downloaded_bytes, total_bytes)

    return file_name

def write_progress_bar(downloaded_bytes, total_bytes):
    """ Prints a string representing download progress. Can be called inside a loop and it overwrites itself """

    downloaded_fraction = float(downloaded_bytes)/total_bytes
    downloaded_bar_length = int(TOTAL_BAR_LENGTH*downloaded_fraction)
    empty_bar_length = TOTAL_BAR_LENGTH - downloaded_bar_length

    progress_bar = "\r[%s%s]" % (FULL_SQUARE*downloaded_bar_length, EMPTY_SQUARE*empty_bar_length)
    percentage_string =  r" %3.2f%%" % (downloaded_fraction*100.0)

    total_length = (1 + TOTAL_BAR_LENGTH + len(percentage_string))
    carriage_return = BACKSPACE*total_length

    print progress_bar+percentage_string+carriage_return,


if __name__ == '__main__':
    """ Runs the script. If an argument is given, it's used as a url """

    if len(sys.argv) <= 1:
        print "Script para descargar en la carpeta del proyecto un dataset a partir de una url"
        print "Modo de uso: \n\t" \
              "python -m get_dataset [url]"
        print "Ejemplo: \n\t" \
              'python -m get_dataset "'+EXAMPLE_DATASET_URL+'"'
    else:
        data_set_url = sys.argv[1]
        download_file(data_set_url)
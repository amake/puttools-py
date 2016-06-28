#!/usr/bin/python

import sys
import os
import putio

TYPE_DELIMITER = '::'

def main():
    api = putio.get_api()
    torrent_args = [x for x in sys.argv[1:] if not x.startswith('--')]
    if len(torrent_args) > 0:
        for arg in torrent_args:
            if arg.count(TYPE_DELIMITER) == 1:
                the_type, torrent = arg.split(TYPE_DELIMITER)
                api.add(torrent, putio.CALLBACK_URL + '?amk_type=' + the_type)
            else:
                api.add(arg)
    else:
        download = '--download' in sys.argv
        delete = '--delete' in sys.argv
        if len(sys.argv) == 1:
            download = raw_input('Download all? (y/N) ').lower() == 'y'
            if download:
                delete = raw_input('Delete after? (y/N) ').lower() == 'y'
        if download:
            downloaded = api.download(0, os.getcwd())
            if delete:
                for d in downloaded:
                    api.delete(d)

if __name__ == '__main__':
    main()

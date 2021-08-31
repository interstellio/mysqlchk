# -*- coding: utf-8 -*-
# Copyright (c) 2021 Interstellio (PTY) LTD - All Rights Reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.
# Proprietary and confidential.
import sys
import argparse
import configparser

import pymysql
from aiohttp import web


from mysqlchk import metadata


def mysqlchk(args):
    try:
        config = configparser.ConfigParser()
        config.read('/etc/nebularstack/mysqlchk.ini')
        host = config['mysql']['host']
        username = config['mysql']['username']
        password = config['mysql']['password']

        connection = pymysql.connect(host=host,
                                     user=username,
                                     password=password,
                                     cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as crsr:
            crsr.execute("show status like 'wsrep_local_state_comment'")
            res = crsr.fetchone()
            if res['Value'].lower() != 'synced':
                connection.close()
                return (False, 'Not-In-Sync',)

            crsr.execute("show status like 'wsrep_ready'")
            res = crsr.fetchone()
            if res['Value'].lower() != 'on':
                connection.close()
                return (False, 'WSREP not ready',)

            connection.close()
            return (True, 'Synced',)

    except Exception as err:
        return (False, err,)


def test(args):
    print(mysqlchk(args)[1])


def server(args):
    async def hello(request):
        good, msg = mysqlchk(None)
        if good:
            return web.Response(text=msg)
        else:
            return web.Response(text=msg, status=500)

    app = web.Application()
    app.add_routes([web.route('*', '/', hello)])

    web.run_app(app, port=8080)


def main(argv):
    print(metadata.description + ' ' + metadata.version)

    parser = argparse.ArgumentParser(description=metadata.description)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-t',
                       dest='funcs',
                       action='append_const',
                       const=test,
                       help='Run test + output')
    group.add_argument('-s',
                       dest='funcs',
                       action='append_const',
                       const=server,
                       help='Run Server')

    args = parser.parse_args()

    if args.funcs is not None:
        for func in args.funcs:
            func(args)


def entry_point():
    """Zero-argument entry point for use with setuptools/distribute."""
    raise SystemExit(main(sys.argv))


if __name__ == '__main__':
    entry_point()

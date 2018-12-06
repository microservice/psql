#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import traceback

from flask import Flask, jsonify, request

import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)


@app.route('/execute', methods=['post'])
def execute():
    req = request.json
    query = req['query']
    args = req.get('data', {})
    with psycopg2.connect(os.environ.get('POSTGRES_DSN'),
                          cursor_factory=RealDictCursor) as conn:
        with conn.cursor() as cur:
            cur.execute(query, args)
            return cur.fetchall()


def app_error(e):
    print(traceback.format_exc())
    return jsonify({"message": repr(e)}), 400


if __name__ == "__main__":
    app.register_error_handler(Exception, app_error)
    app.run(host='0.0.0.0', port=8000)

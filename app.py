#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import traceback

from flask import Flask, jsonify, make_response, request

import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)


@app.route('/execute', methods=['post'])
def execute():
    req = request.get_json()
    query = req['query']
    args = req.get('data', {})
    conn = psycopg2.connect(os.environ.get('POSTGRES_DSN'),
                            cursor_factory=RealDictCursor)
    cur = conn.cursor()

    try:
        cur.execute(query, args)
        results = cur.fetchall()
        conn.commit()
    except BaseException as e:
        traceback.print_exc(e)
        resp = make_response('{"status": "fail"}')
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        return resp
    finally:
        cur.close()
        conn.close()

    res = {
        'status': 'ok',
        'results': results
    }
    resp = make_response(json.dumps(res))
    resp.headers['Content-Type'] = 'application/json; charset=utf-8'
    return resp


def app_error(e):
    return jsonify({"message": str(e)}), 400


if __name__ == "__main__":
    app.register_error_handler(Exception, app_error)
    app.run(host='0.0.0.0', port=8000)

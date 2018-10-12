# -*- coding: utf-8 -*-
import json
import os
import traceback

from flask import Flask, request, make_response

import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)


@app.route('/select', methods=['post'])
def select():
    req = request.get_json()
    query = req['query']
    args = req.get('data', {})
    conn = psycopg2.connect(os.environ.get('POSTGRES_DSN'),
                            cursor_factory=RealDictCursor)
    cur = conn.cursor()

    try:
        cur.execute(query, args)
        results = cur.fetchall()
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


if __name__ == "__main__":
    app.run(port=8000)

{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from flask import Flask, jsonify\
from pytrends.request import TrendReq\
import os\
\
app = Flask(__name__)\
\
@app.get("/health")\
def health():\
    return \{"ok": True\}\
\
@app.get("/trends")\
def trends():\
    pytrends = TrendReq(hl="en-US", tz=360)\
    df = pytrends.trending_searches(pn="united_states")\
    keywords = df[0].dropna().astype(str).head(30).tolist()\
\
    return jsonify(\{\
        "source": "pytrends",\
        "geo": "US",\
        "keywords": keywords\
    \})\
\
if __name__ == "__main__":\
    port = int(os.environ.get("PORT", "8080"))\
    app.run(host="0.0.0.0", port=port)}
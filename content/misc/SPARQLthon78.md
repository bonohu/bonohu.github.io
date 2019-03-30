Title: SPARQLthon78
Date: 2019-03-29 21:00
Category: DBCLS

Joined [SPARQLthon](http://wiki.lifesciencedb.jp/mw/SPARQLthon) held at DBCLS Mishima.
This was [78th SPARQLthon](http://wiki.lifesciencedb.jp/mw/SPARQLthon78).

First, I tried to execute SPARQL from UNIX command line for the integration of unfamiliar data.
According to the SPARQL book (p145), I could make it.

```
# command line execution of SPARQL 
% curl -F query=@hoge.rq -H "Accept: application/sparql-results+xml" (URL for SPARQL endpoint)
```

SPARQL in `hoge.rq`, and the result in XML.
You can change to JSON by replacing `xml` to `json`.

On the second day, I tackled to update [AOE](http://aoe.dbcls.jp/) data for the latest one.
By fixing description in the data from DDBJ GEA (the information about date is not formally described, in the comment line..), we can include data from GEA.
It is not easy to automate this process now.

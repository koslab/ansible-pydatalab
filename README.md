# Python Big Data Scientific Computing Kit

This ansible script deploys a server with a collection of Python Big Data 
and Scientific Computing tools and libraries, preconfigured for running
on a local Spark cluster.

Included packages:

 * Base Python
   * Anaconda Python Distribution 2.7 (http://docs.continuum.io/anaconda/)
 * Development tool
   * Jupyter (https://jupyter.org/)
 * Data visualization
   * Bokeh (http://bokeh.pydata.org/)
   * Pygal (http://www.pygal.org)
   * Seaborn (http://stanford.edu/~mwaskom/software/seaborn/)
 * Text and Sentiment
   * Gensim (https://radimrehurek.com/gensim/)
   * vaderSentiment (https://pypi.python.org/pypi/vaderSentiment)
 * Machine learning
   * Gensim (https://radimrehurek.com/gensim/)
   * Tensorflow (http://tensorflow.org/)
 * Distributed processing
   * Spark 1.3.1 (http://spark.apache.org)
   * Luigi (http://luigi.readthedocs.org)
   * mrjob (https://pythonhosted.org/mrjob/)
 * Data access
   * Python HDFS (https://pypi.python.org/pypi/hdfs/)
 * Web scraper
   * Scrapy (http://scrapy.org)
 * GIS
   * Geojson (https://pypi.python.org/pypi/geojson)
   * Geocoder (https://pypi.python.org/pypi/geocoder)
 * Javascript visualization libraries
   * D3.js (http://d3js.org)
   * DC.js (https://dc-js.github.io/dc.js/)
   * NVD3.js (http://nvd3.org)
   * Dimple.js (http://dimplejs.org)
   * Crossfilter.js (http://square.github.io/crossfilter/)

## Installation

 1. Setup a server or VM with CentOS7
 2. Ensure FQDN is configured correctly. Spark requires the host system 
    hostname to be resolvable, quickest fix is to ensure the hostname 
    resolves as 127.0.0.1 by adding an entry in /etc/hosts:

        127.0.0.1 localhost.localdomain localhost pydatalab.server.local pydatalab

 3. Create an ansible hosts inventory (assuming server hostname is your hostname is :

        [master]
        pydatalab.server.local

 4. Execute ansible

        ansible-playbook -i hosts playbook.yml

 5. Jupyter should be running at pydatalab.server.local:8888

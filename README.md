# Python Big Data Scientific Computing Kit

This ansible script deploys a server with a collection of Python Big Data 
and Scientific Computing tools and libraries, preconfigured for running
on a local Spark cluster.

Included packages:

 * Anaconda Python Distribution 2.7 (http://docs.continuum.io/anaconda/)
 * Jupyter (https://jupyter.org/)
 * Bokeh (http://bokeh.pydata.org/)
 * Python HDFS (https://pypi.python.org/pypi/hdfs/)
 * Spark 1.3.1 (http://spark.apache.org)
 * java-1.8.0-openjdk (http://openjdk.java.net/)

## Installation

 1. Setup a server or VM with CentOS7
 2. Ensure FQDN is configured correctly. Spark requires the system 
    hostname to be resolvable, quickest fix is to ensure the hostname 
    resolves as 127.0.0.1 by adding an entry in /etc/hosts
 3. Create an ansible hosts inventory:

        [master]
        my.pybigdatakit.server.local

 4. Execute ansible

        ansible-playbook -i hosts playbook.yml

 5. Jupyter should be running at my.pybigdatakit.server.local:8888

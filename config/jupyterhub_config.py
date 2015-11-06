import os
os.environ['JUPYTER_CONFIG_DIR'] = '/usr/local/share/jupyter'
c.Spawner.env_keep.append('JUPYTER_CONFIG_DIR')
c.Spawner.env_keep.append('HADOOP_HOME')
c.Spawner.notebook_dir = '~/notebooks'

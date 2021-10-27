# -*- coding: utf-8 -*-
from resource_management import *

config = Script.get_config()
stack_root = Script.get_stack_root()

ambari_version = default("/repositoryFile/repoVersion", "3.1.5.0-152")

# 获取tdengine-env.xml的TDengine pid文件夹
jupyter_pid_dir = config['configurations']['jupyter-config']['jupyter_pid_dir']

# 获取tdengine-env.xml的TDengine pid文件
jupyter_pid_file = format("{jupyter_pid_dir}/jupyter.pid")

# 获取tdengine-env.xml的TDengine pid文件夹
jupyter_log_dir = config['configurations']['jupyter-config']['jupyter_log_dir']

# jupyter配置文件目录
jupyter_dir = format("{stack_root}/{ambari_version}/jupyter")

# 获取本机主机名称
fqdn = config['agentLevelParams']['hostname']

# 获取服务端口地址
server_port = config['configurations']['jupyter-config']['server_port']

# Jupyter下载地址
if config.get('repositoryFile'):
    urls = config['repositoryFile']['repositories']
    for url in urls:
        if (url['repoName'] == "HDP") | (url['repoName'] is "HDP"):
            baseUrl = url['baseUrl']

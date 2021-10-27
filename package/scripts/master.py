# -*- coding: utf-8 -*-

import os
from resource_management import *


class Master(Script):

    def install(self, env):
        import params
        env.set_params(params)

        Logger.info("安装开始")

        Execute("rm -rf /data/jupyter && mkdir -p /data/jupyter/")

        # 安装python setuptools
        Execute(format("wget {baseUrl}/python/setuptools-44.1.1.zip"))
        Execute("unzip -o -q setuptools-44.1.1.zip && rm -rf setuptools-44.1.1.zip")
        Execute("cd setuptools-44.1.1 && python setup.py install")
        Execute("rm -rf setuptools-44.1.1")

        # 安装python pip
        Execute(format("wget {baseUrl}/python/pip-19.3.1.tar.gz"))
        Execute("tar -zxvf pip-19.3.1.tar.gz && rm -rf pip-19.3.1.tar.gz")
        Execute("cd pip-19.3.1 && python setup.py install")
        Execute("rm -rf pip-19.3.1")

        # 创建jupyter安装目录
        Execute("rm -rf /opt/jupyter && mkdir /opt/jupyter")

        # 下载安装jupyter notebook模块需要的安装包（已在本地源内部配置）
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/ipython_genutils-0.2.0-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/pyzmq-19.0.2-cp27-cp27mu-manylinux1_x86_64.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/prometheus_client-0.11.0-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/ipaddress-1.0.23-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/futures-3.3.0-py2-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/backports_abc-0.5-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/MarkupSafe-1.1.1-cp27-cp27mu-manylinux1_x86_64.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/pandocfilters-1.5.0-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/defusedxml-0.7.1-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/mistune-0.8.4-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/Pygments-2.5.2-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/testpath-0.4.4-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/six-1.16.0-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/enum34-1.1.10-py2-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/ptyprocess-0.7.0-py2.py3-none-any.whl"))
        Execute(format(
            "cd /opt/jupyter && wget {baseUrl}/jupyter/backports.shutil_get_terminal_size-1.0.0-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/pexpect-4.8.0-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/configparser-4.0.2-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/webencodings-0.5.1-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/functools32-3.2.3-2.tar.gz"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/pyrsistent-0.16.1.tar.gz"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/attrs-21.2.0-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/scandir-1.10.0.tar.gz"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/pyparsing-2.4.7-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/contextlib2-0.6.0.post1-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/zipp-1.2.0-py2.py3-none-any.whl"))
        Execute(format(
            "cd /opt/jupyter && wget {baseUrl}/jupyter/backports.functools_lru_cache-1.6.4-py2.py3-none-any.whl"))

        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/Jinja2-2.11.3-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/Send2Trash-1.8.0.tar.gz"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/traitlets-4.3.3-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/jupyter_core-4.6.3-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/singledispatch-3.7.0-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/python_dateutil-2.8.2-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/entrypoints-0.3-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/pathlib2-2.3.6-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/simplegeneric-0.8.1.zip"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/pickleshare-0.7.5-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/packaging-20.9-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/importlib_metadata-2.1.1-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/wcwidth-0.2.5-py2.py3-none-any.whl"))

        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/tornado-5.1.1.tar.gz"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/jupyter_client-5.3.5-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/terminado-0.8.3-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/bleach-3.3.1-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/jsonschema-3.2.0-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/prompt_toolkit-1.0.18-py2-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/nbformat-4.4.0-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/ipython-5.10.0-py2-none-any.whl"))

        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/ipykernel-4.10.1-py2-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/nbconvert-5.6.1-py2.py3-none-any.whl"))
        Execute(format("cd /opt/jupyter && wget {baseUrl}/jupyter/notebook-5.7.13-py2.py3-none-any.whl"))

        # 解压安装包
        Execute(format("pip install /opt/jupyter/ipython_genutils-0.2.0-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/pyzmq-19.0.2-cp27-cp27mu-manylinux1_x86_64.whl"))
        Execute(format("pip install /opt/jupyter/prometheus_client-0.11.0-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/ipaddress-1.0.23-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/futures-3.3.0-py2-none-any.whl"))
        Execute(format("pip install /opt/jupyter/backports_abc-0.5-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/MarkupSafe-1.1.1-cp27-cp27mu-manylinux1_x86_64.whl"))
        Execute(format("pip install /opt/jupyter/pandocfilters-1.5.0-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/defusedxml-0.7.1-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/mistune-0.8.4-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/Pygments-2.5.2-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/testpath-0.4.4-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/six-1.16.0-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/enum34-1.1.10-py2-none-any.whl"))
        Execute(format("pip install /opt/jupyter/ptyprocess-0.7.0-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/backports.shutil_get_terminal_size-1.0.0-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/pexpect-4.8.0-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/configparser-4.0.2-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/webencodings-0.5.1-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/functools32-3.2.3-2.tar.gz"))
        Execute(format("pip install /opt/jupyter/pyrsistent-0.16.1.tar.gz"))
        Execute(format("pip install /opt/jupyter/attrs-21.2.0-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/scandir-1.10.0.tar.gz"))
        # pyparsing>=2.0.2,系统存在1.5.6的版本，直接安装报错，需要删除该文件才能成功升级安装
        Execute("rm -rf /usr/lib/python2.7/site-packages/pyparsing-1.5.6-py2.7.egg-info")
        Execute(format("pip install /opt/jupyter/pyparsing-2.4.7-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/contextlib2-0.6.0.post1-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/zipp-1.2.0-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/backports.functools_lru_cache-1.6.4-py2.py3-none-any.whl"))

        Execute(format("pip install /opt/jupyter/Jinja2-2.11.3-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/Send2Trash-1.8.0.tar.gz"))
        Execute(format("pip install /opt/jupyter/traitlets-4.3.3-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/jupyter_core-4.6.3-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/singledispatch-3.7.0-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/python_dateutil-2.8.2-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/entrypoints-0.3-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/pathlib2-2.3.6-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/simplegeneric-0.8.1.zip"))
        Execute(format("pip install /opt/jupyter/pickleshare-0.7.5-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/packaging-20.9-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/importlib_metadata-2.1.1-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/wcwidth-0.2.5-py2.py3-none-any.whl"))

        Execute(format("pip install /opt/jupyter/tornado-5.1.1.tar.gz"))
        Execute(format("pip install /opt/jupyter/jupyter_client-5.3.5-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/terminado-0.8.3-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/bleach-3.3.1-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/jsonschema-3.2.0-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/prompt_toolkit-1.0.18-py2-none-any.whl"))
        Execute(format("pip install /opt/jupyter/nbformat-4.4.0-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/ipython-5.10.0-py2-none-any.whl"))

        Execute(format("pip install /opt/jupyter/ipykernel-4.10.1-py2-none-any.whl"))
        Execute(format("pip install /opt/jupyter/nbconvert-5.6.1-py2.py3-none-any.whl"))
        Execute(format("pip install /opt/jupyter/notebook-5.7.13-py2.py3-none-any.whl"))

        # 删除安装文件夹
        Execute("rm -rf /opt/jupyter")

        Logger.info("安装完成!")

    def configure(self, env, upgrade_type=None, config_dir=None):
        import params
        env.set_params(params)

        Logger.info("配置开始")

        # 不需要生成jupyter配置文件原因：下面的File方法无法修改隐藏文件的内容
        # 解决方法：手动生成配置文件夹并修改权限为700，通过链接到ambari安装目录下的配置文件
        Execute("rm -rf ~/.jupyter && mkdir ~/.jupyter/ && chmod 700 ~/.jupyter")

        Execute(format("rm -rf {jupyter_dir} && mkdir {jupyter_dir}"))

        Execute(format("rm -rf {jupyter_log_dir} && mkdir {jupyter_log_dir}"))

        configurations = params.config['configurations']['jupyter-config']
        File(format("{jupyter_dir}/jupyter_notebook_config.py"),
             content=Template("jupyter_notebook_config.py.j2", configurations=configurations))

        Execute(format("ln -s {jupyter_dir}/jupyter_notebook_config.py ~/.jupyter/jupyter_notebook_config.py"))

        # 生成pid目录
        Execute(format("mkdir -p {jupyter_pid_dir}"))

        Logger.info("配置结束")

    def start(self, env, upgrade_type=None):
        import params
        env.set_params(params)

        Logger.info("启动开始")

        # 启动前的配置
        self.configure(env)

        Execute(format("LANG=zn nohup jupyter notebook >> {jupyter_log_dir}/jupyter.log &"))

        # 获取jupyter服务的pid并写入文件
        cmd = "ps -aux | grep jupyter | grep -v grep | awk '{print $2}' > " + params.jupyter_pid_file
        Execute(cmd)

        Logger.info("启动结束")

    def stop(self, env, upgrade_type=None):
        import params
        env.set_params(params)

        Logger.info("停止开始")

        pid = os.popen(format("cat {jupyter_pid_file}")).read()

        Execute(format("kill -9 {pid}"))

        # jupyter的pid文件夹删除
        Directory([params.jupyter_pid_dir], action="delete")

        Logger.info("停止结束")

    def status(self, env):
        import params
        env.set_params(params)

        check_process_status(params.jupyter_pid_file)

    def restart(self, env):
        Logger.info("重启开始")

        self.stop(env)
        self.start(env)

        Logger.info("重启结束")


if __name__ == "__main__":
    Master().execute()

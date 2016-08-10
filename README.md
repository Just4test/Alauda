# Alauda
An simple python API for alauda.cn and alauda.io
Read docs: http://docs.alauda.cn/

# Installation
pip install just4alauda

# Usage
``` python
import alauda


alauda_ns = 'your_namespace'
alauda_token = 'xxxxxxxxxxxxxxx'

a = alauda.Alauda(alauda_ns, alauda_token)

# Create build repo
tag_config = alauda.TagConfig.create('latest', 'master')
git_url = 'https://github.com/nginxinc/docker-nginx.git'
build_config = alauda.BuildConfig.create_simple(git_url, tag_config)
repo = a.create_repo('repo_name', 'description', build_config = build_config)

# Run service
yaml_str = '''
redis:
  image: nginx
  ports:
  - '80/http'
'''
repo.build()
config = alauda.Service.yml_to_json(a, yaml)
service = a.create_service('service_name', config)

# Run app

```



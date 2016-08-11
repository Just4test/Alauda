from alauda import *
import os

alauda_ns = os.environ.get('ALAUDA_NS')
alauda_token = os.environ.get('ALAUDA_TOKEN')

alauda = Alauda(alauda_ns, alauda_token)

# Create build repo
GIT_URL = 'https://github.com/nginxinc/docker-nginx.git'
BUILD_CONTEXT_PATH = '/mainline/jessie/'
REPO_NAME = 'test-nginx'

tag_config = TagConfig.create('latest', 'master', build_context_path = BUILD_CONTEXT_PATH)
build_config = BuildConfig.create_simple(GIT_URL, tag_config)
repo = alauda.create_repo(REPO_NAME, 'Just for test alauda API', build_config = build_config)

repo.build()
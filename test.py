from alauda import *
import os

alauda_ns = os.environ.get('ALAUDA_NS')
alauda_token = os.environ.get('ALAUDA_TOKEN')
alauda_region = os.environ.get('ALAUDA_REGION')
if not alauda_ns:
    print('You must set env ALAUDA_NS')
    exit(1)
if not alauda_token:
    print('You must set env ALAUDA_TOKEN')
    exit(1)

print('Login to alauda...')
alauda = Alauda(alauda_ns, alauda_token, alauda_region)

def print_(l, *args):
    tab = '  '* l + '├−'
    print(tab, *args)
    
print('Show All Service...')

print(alauda)
for region in alauda.regions:
    print_(1, region)
    for service in region.list_service():
        print_(2, service)
    for app in region.list_application():
        print_(2, app)
        for service in app.list_service():
            print_(3, service)
            
exit()

# Create build repo
GIT_URL = 'https://github.com/nginxinc/docker-nginx.git'
BUILD_CONTEXT_PATH = '/mainline/jessie/'
REPO_NAME = 'test-nginx'

repo = alauda.get_repo(REPO_NAME)
if repo:
    print('Repo already exist {}. delete...'.format(repo))
    repo.delete()

tag_config = TagConfig.create('latest', 'master', build_context_path = BUILD_CONTEXT_PATH)
build_config = BuildConfig.create_simple(GIT_URL, tag_config)
print('Create repo...')
repo = alauda.create_repo(REPO_NAME, 'Just for test alauda API', build_config = build_config)
print(repo)
print('Build...')
print(repo.build())

# Create service
yaml_str = '''
nginx:
  image: nginx
  ports:
  - '80/http'
'''
config = Service.yml_to_json(alauda, yaml_str)
print(config)
service = alauda.create_service(config[0])
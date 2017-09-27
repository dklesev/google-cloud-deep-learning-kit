import os
from IPython.lib import passwd
from s3contents import S3ContentsManager

c = get_config()
c.IPKernelApp.pylab = 'inline'
c.NotebookApp.ip = '*'
c.NotebookApp.port = 8888
c.NotebookApp.open_browser = False
c.MultiKernelManager.default_kernel_name = 'python'
c.NotebookApp.token = ''
c.NotebookApp.notebook_dir = '/src'

# Tell Jupyter to use S3ContentsManager for all storage.
if 'JUPYTER_S3_BUCKET' in os.environ:
  c.NotebookApp.contents_manager_class = S3ContentsManager
  c.S3ContentsManager.access_key_id = os.environ.pop('JUPYTER_S3_ACCESS_KEY', None) # assuming IAM Role-based access it can be set None
  c.S3ContentsManager.secret_access_key = os.environ.pop('JUPYTER_S3_SECRET_KEY', None)
  c.S3ContentsManager.bucket_name = os.environ.pop('JUPYTER_S3_BUCKET')

# sets a password if PASSWORD is set in the environment
if 'PASSWORD' in os.environ:
  c.NotebookApp.password = passwd(os.environ.pop('PASSWORD'))

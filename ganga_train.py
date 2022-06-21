app = Executable()
app.exe = File('train.sh')
args = []

backend = Condor()
backend.cdf_options['request_memory'] = '16G'

name = 'InnerEye'

j = Job(application=app, backend=backend, name=name)
j.submit()

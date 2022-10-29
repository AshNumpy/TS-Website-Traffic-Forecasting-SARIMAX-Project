import pip

packages = ['numpy', 'pandas', 'matplotlib', 'plotly', 'statsmodels']

for package in packages:
    try:
        __import__(package) 
        print(f'{package} available on your computer.')
    except:
        pip.main(['install',package])
        print(f'{package} installed on your computer.')
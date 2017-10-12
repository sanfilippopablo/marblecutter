from setuptools import find_packages, setup

version = '0.1.3'

setup(
    name='marblecutter',
    version=version,
    description='Raster manipulation',
    url='https://github.com/mojodna/marblecutter',
    author='Seth Fitzsimmons',
    author_email='seth@mojodna.net',
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    package_data={
        'marblecutter': ['static/images/*', 'templates/*'],
    },
    install_requires=[
        'haversine',
        'mercantile',
        'numpy',
        'Pillow',
        'rasterio>=1.0a10[s3]',
        'scipy',
    ],
    extras_require={
        'color_ramp': 'matplotlib',
        'postgis': 'psycopg2',
        'web': [
            'flask',
            'flask-cors',
        ],
    },
)

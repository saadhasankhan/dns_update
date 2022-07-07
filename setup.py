from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='route53_utils',
      version='0.1',
      description='Created, deletes and updates A host an CNAME records in route 53 ops.cloud.cengage.com domain',
      url='https://github.com/saadhasankhan/route53_utils',
      author='skhan',
      author_email='saadhasankhan@gmail.com',
      license='MIT',
      packages=['route53_utils'],
      install_requires=[
          'boto3'
      ],
      zip_safe=False,
      entry_points={
          'console_scripts': ['dns_update=route53_utils.dns_update:main'],
      },
      )

# %%
import setuptools

with open("readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ADC',
    version='0.0.1',
    author='Yang Wu',
    author_email='yang.wu@ontario.ca',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/yangg1224/ADC.git',
    project_urls = {
        "Bug Tracker": "https://github.com/Muls/toolbox/issues"
    },
    license='MIT',
    packages=['ADC'],
    install_requires=['requests','pandas','regex'],
)
from setuptools import find_packages, setup


# Required dependencies
required = [
    # Please keep alphabetized
    # 'gym==0.12.1',
    'gym==0.15.4',
    # 'mujoco-py<2.1,>=2.0',
    'mujoco-py<2.2,>=2.0',
    'opencv-python>=4.1.0.25',
    'cython<3'
]


# Development dependencies
extras = dict()
extras['dev'] = [
    # Please keep alphabetized
    'ipdb',
    'memory_profiler',
    'pylint',
    'pyquaternion==0.9.5',
    'pytest>=3.6',
]


setup(
    name='metaworld',
    packages=find_packages(),
    include_package_data=True,
    install_requires=required,
    extras_require=extras,
)

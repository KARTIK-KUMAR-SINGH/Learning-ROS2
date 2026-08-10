from setuptools import find_packages, setup

package_name = 'robot_counter_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kartik-kumar-singh',
    maintainer_email='kartiksinghcarrier@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'number_publisher = robot_counter_pkg.number_publisher:main',
            'number_counter = robot_counter_pkg.number_counter:main',
        ],
    },
)

from setuptools import find_packages, setup

package_name = 'learning_publisher'

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
            "robot_news = learning_publisher.practice1:main",
            "robot_count = learning_publisher.practice2:main",
            "robot_temprature = learning_publisher.practice3:main"
        ],
    },
)

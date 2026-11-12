from setuptools import find_packages, setup

package_name = 'my_new_pkg'

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
            "py_node = my_new_pkg.new_node:main",
            "py_node_printing = my_new_pkg.new_node_printing:main",
            "py_node_printing2 = my_new_pkg.py_node_printing2:main",
            "py_new = my_new_pkg.py_node_printing_multiple_times:main",
            "new_node2 = my_new_pkg.new_node2:main",
            "new_node_node = my_new_pkg.new_node_node:main",
            "practice1_node = my_new_pkg.practice:main",
            "practice2_node = my_new_pkg.practice2:main",
            "practice3_node = my_new_pkg.practice3:main",
            "practice4_node = my_new_pkg.practice4:main",
            "practice5_node = my_new_pkg.practice5:main",
            "practice6_node = my_new_pkg.practice6:main",
            "practice7_node = my_new_pkg.practice7:main"
        ],
    },
)

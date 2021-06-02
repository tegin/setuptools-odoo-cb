# Copyright © 2015-2017 ACSONE SA/NV
# License LGPLv3 (http://www.gnu.org/licenses/lgpl-3.0-standalone.html)

import os

import setuptools

here = os.path.abspath(os.path.dirname(__file__))

long_description = []

setuptools.setup(
    name="setuptools-odoo-cb",
    use_scm_version=True,
    description="A library to help package Odoo addons with setuptools",
    long_description="\n".join(long_description),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: " "GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: POSIX",  # because we use symlinks
        "Programming Language :: Python",
        "Framework :: Odoo",
    ],
    license="LGPLv3",
    author="ACSONE SA/NV",
    author_email="info@acsone.eu",
    url="http://github.com/acsone/setuptools-odoo",
    packages=["setuptools_odoo_cb"],
    include_package_data=True,
    install_requires=["setuptools", "setuptools_scm>=2.1,!=4.0.0", "setuptools-odoo"],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    setup_requires=["setuptools-scm!=4.0.0"],
    entry_points={
        "console_scripts": [
            "setuptools-odoo-cb-get-requirements="
            "setuptools_odoo_cb.get_requirements:main",
        ]
    },
)

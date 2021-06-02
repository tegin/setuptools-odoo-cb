# Copyright © 2020 ACSONE SA/NV
# License LGPLv3 (http://www.gnu.org/licenses/lgpl-3.0-standalone.html)

from __future__ import print_function

import argparse
import os
import sys
from functools import partial

from setuptools_odoo import get_requirements
from setuptools_odoo.manifest import read_manifest


def _new_get_metadata_overrides(
    addons_dir,
    addon_name,
    setup_dir="setup",
    organization=False,
    repo_name=False,
    branch=False,
):
    overrides = get_requirements._get_metadata_overrides_from_setup_dir(
        addons_dir, addon_name, setup_dir=setup_dir
    )
    overrides.setdefault("depends_override", {})
    data = read_manifest(os.path.join(addons_dir, addon_name,))
    depends = data.get("depends", [])
    for d in depends:
        if not os.path.exists(os.path.join(addons_dir, d)):
            continue
        overrides["depends_override"].setdefault(
            d,
            "git+https://github.com/%s/%s.git@%s#subdirectory=setup/%s"
            % (organization, repo_name, branch, d),
        )
    return overrides


def main(args=None):
    parser = argparse.ArgumentParser(
        description=(
            "Print external python dependencies for all addons in an "
            "Odoo addons directory. If dependencies overrides are declared "
            "in setup/{addon}/setup.py, they are honored in the output. "
        )
    )
    parser.add_argument(
        "--addons-dir", "-d", default=".", help="addons directory (default: .)",
    )
    parser.add_argument(
        "--repo", "-r", default=".", help="Repo name",
    )
    parser.add_argument(
        "--branch", "-b", help="Branch",
    )
    parser.add_argument(
        "--organization", "-g", default="tegin", help="Organization name",
    )
    parser.add_argument(
        "--output", "-o", default="-", help="output file (default: stdout)",
    )
    parser.add_argument(
        "--header", help="output file header",
    )
    parser.add_argument(
        "--include-addons",
        action="store_true",
        help=(
            "Include addons and odoo requirements in addition to "
            "python external dependencies (default: false)"
        ),
    )
    args = parser.parse_args(args)
    organization = args.organization
    branch = args.branch
    repo_name = args.repo
    requirements = get_requirements._get_requirements(
        args.addons_dir,
        include_addons=args.include_addons,
        get_metadata_overrides=partial(
            _new_get_metadata_overrides,
            organization=organization,
            repo_name=repo_name,
            branch=branch,
        ),
    )
    if args.output == "-":
        get_requirements._render(requirements, args.header, sys.stdout)
    else:
        if os.path.exists(args.output) or requirements:
            with open(args.output, "w") as fp:
                get_requirements._render(requirements, args.header, fp)


if __name__ == "__main__":
    main(sys.argv[1:])

import sys
import os

from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(username="vida", channel="stable")

    if sys.platform == "linux":
        builder.add(settings={"os":"Windows", "arch": "x86_64", "build_type": "Debug"},
                    options={}, env_vars={}, build_requires={})

        builder.add(settings={"os":"Windows", "arch": "x86_64", "build_type": "Release"},
                    options={}, env_vars={}, build_requires={})

        builder.add(settings={"os":"Windows", "arch": "x86", "build_type": "Debug"},
                    options={}, env_vars={}, build_requires={})

        builder.add(settings={"os":"Windows", "arch": "x86", "build_type": "Release"},
                    options={}, env_vars={}, build_requires={})

    builder.add(settings={"arch": "x86_64", "build_type": "Debug"},
                options={}, env_vars={}, build_requires={})

    builder.add(settings={"arch": "x86_64", "build_type": "Release"},
                options={}, env_vars={}, build_requires={})

    builder.run()

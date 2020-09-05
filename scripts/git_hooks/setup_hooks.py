import shutil
import os

basePath = os.path.dirname(os.path.realpath(__file__))

shutil.copy2(
    os.path.join(basePath, 'pre_commit.sh'),
    os.path.join(basePath, '../../.git/hooks/pre-commit')
)

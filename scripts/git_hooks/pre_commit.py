import subprocess
import sys

def get_changed_files():
    files = []

    proc = subprocess.Popen(
        ['git', 'diff', '--cached', '--name-only'],
        stdout=subprocess.PIPE
    )
    output = proc.communicate()[0]

    if proc.returncode != 0:
        print("git diff failed: " + str(proc.returncode))
        sys.exit(1)

    for line in output.split(b'\n'):
        files.append(str(line))

    return files

def generate_single_header():
    proc = subprocess.Popen(
        [
            'python',
            './scripts/generate_single_header/generate_single_header.py',
            'include/test.h',
            '-o',
            'single_header/test.h'
        ],
        stdout=subprocess.PIPE
    )

    output = proc.communicate()[0]
    if proc.returncode != 0:
        print("failed to generate single header: " + str(proc.returncode))
        print(output)
        return False

    return True

def add_single_header():
    proc = subprocess.Popen(
        ['git', 'add', 'single_header/test.h'],
        stdout=subprocess.PIPE
    )
    output = proc.communicate()[0]

    if proc.returncode != 0:
        print("git add single header failed: " + str(proc.returncode))
        print(output)
        return False

    return True

def stash_unstaged_changes():
    proc = subprocess.Popen(
        ['git', 'stash', '--keep-index', '--include-untracked'],
        stdout=subprocess.PIPE
    )
    output = proc.communicate()[0]

    if proc.returncode != 0:
        print("git stash unstaged changes failed: " + str(proc.returncode))
        print(output)
        return False

    return True

def stash_pop():
    proc = subprocess.Popen(
        ['git', 'stash', 'pop'],
        stdout=subprocess.PIPE
    )
    output = proc.communicate()[0]

    if proc.returncode != 0:
        print("git stash pop failed: " + str(proc.returncode))
        print(output)
        return False

    return True

generateSingleHeader = False

files = get_changed_files()
for filepath in files:
    if filepath.startswith("include/"):
        generateSingleHeader = True
        break

if generateSingleHeader:
    print("generating single header...")
    if not stash_unstaged_changes():
        sys.exit(1)
    if not generate_single_header():
        stash_pop()
        sys.exit(1)
    if not add_single_header():
        stash_pop()
        sys.exit(1)
    if not stash_pop():
        sys.exit(1)

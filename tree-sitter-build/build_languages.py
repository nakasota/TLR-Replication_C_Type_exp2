import os
import subprocess
from pathlib import Path

def build_parser():
    current_dir = Path(__file__).parent.absolute()
    tree_sitter_go_dir = current_dir / 'tree-sitter-go'

    try:
        # Change to tree-sitter-go directory
        os.chdir(str(tree_sitter_go_dir))

        # Build using make
        subprocess.run(['make'], check=True)
        
        # Copy the built library to the desired location
        os.makedirs(str(current_dir / 'lib'), exist_ok=True)
        subprocess.run([
            'cp',
            'libtree-sitter-go.so',
            str(current_dir / 'lib' / 'parser.so')
        ], check=True)

        print("Successfully built parser")
    except subprocess.CalledProcessError as e:
        print(f"Error building parser: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == '__main__':
    build_parser() 
import os
import sys

def init_program(base_path, program_name):
    paths = [
        f'programs/{program_name}/scans',
        f'programs/{program_name}/exploits',
        f'programs/{program_name}/notes',
        f'programs/{program_name}/loot',
        f'programs/{program_name}/reports'
    ]
    for p in paths:
        full_path = os.path.join(base_path, p)
        os.makedirs(full_path, exist_ok=True)
        with open(os.path.join(full_path, '.keep'), 'w') as f:
            pass
    print(f'Program {program_name} initialized successfully.')

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: python init_program.py <base_path> <program_name>')
    else:
        init_program(sys.argv[1], sys.argv[2])

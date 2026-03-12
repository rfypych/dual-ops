import argparse
import time
import os

def delegate(workspace_path, program_name, task_desc, wait=False):
    todo_path = os.path.join(workspace_path, 'shared_queue', 'qwen_todo.txt')
    status_path = os.path.join(workspace_path, 'shared_queue', 'zai_status.txt')
    
    # 1. Write the task
    message = f"PROGRAM: {program_name}\nTASK: {task_desc}"
    with open(todo_path, 'w') as f:
        f.write(message)
    print(f"[+] Task delegated to Qwen for program: {program_name}")
    
    if wait:
        print("[*] Waiting for Qwen to complete the task...")
        while True:
            if os.path.exists(status_path):
                with open(status_path, 'r') as f:
                    status = f.read().strip()
                if status and "Task completed" in status:
                    print(f"\n[!] Qwen Output: {status}")
                    break
            time.sleep(5)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Dual-Ops Agent Delegation Tool')
    parser.add_argument('--workspace', default='/home/xrphy/dual-ops/active_workspace', help='Path to active_workspace')
    parser.add_argument('--program', required=True, help='Name of the active program')
    parser.add_argument('--task', required=True, help='Task description for Qwen')
    parser.add_argument('--wait', action='store_true', help='Wait for task completion')
    
    args = parser.parse_args()
    delegate(args.workspace, args.program, args.task, args.wait)

import json
import time
import os

def load_workflow(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_animation():
    animation = ["|", "/", "-", "\\"]
    for i in range(10):
        time.sleep(0.1)
        clear_screen()
        print(f"Moving... {animation[i % len(animation)]}")

def ask_user_about_steps(timeframe, steps):
    index = 0
    while index < len(steps):
        step_info = steps[index]
        step = step_info['step']
        response = input(f"🌟 Have you completed '{step}'? (yes/no/info/back/next): ").strip().lower()
        
        if response == 'info':
            print(f"ℹ️  Info: {step_info.get('info', 'No additional information available.')}")
        elif response == 'back':
            if index > 0:
                show_animation()
                index -= 1
            else:
                print("🚧 You are at the first step. Cannot go back. 🚧")
        elif response == 'next':
            if index < len(steps) - 1:
                show_animation()
                index += 1
            else:
                print("🚧 You are at the last step. Cannot go forward. 🚧")
        elif response == 'yes':
            print(f"Great! You've completed '{step}'.")
            index += 1
        else:
            print(f"🚧 Please complete '{step}' before proceeding. 🚧")
            return False
    return True

def main():
    # ASCII Art Header
    print(r"""
     _    _      _                            _         
    | |  | |    | |                          | |        
    | |  | | ___| | ___ ___  _ __ ___   ___  | |_ ___   
    | |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  
    \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | 
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  
                                                      
    """)

    workflow = load_workflow('workflow.json')
    timeframes = workflow.get('timeframes', {})
    if not timeframes:
        print("No timeframes found in the workflow.")
        return
    
    for timeframe, steps_dict in timeframes.items():
        print(f"\n🚀 Starting Timeframe: {timeframe} 🚀")
        for sub_timeframe, steps in steps_dict.items():
            print(f"\n📅 Sub-Timeframe: {sub_timeframe}")
            if not ask_user_about_steps(sub_timeframe, steps):
                break

if __name__ == "__main__":
    main()
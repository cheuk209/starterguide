import json

def load_workflow(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def ask_user_about_steps(timeframe, steps):
    print(f"\nTimeframe: {timeframe}")
    for step in steps:
        response = input(f"🌟 Have you completed '{step}'? (yes/no): ").strip().lower()
        if response != 'yes':
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
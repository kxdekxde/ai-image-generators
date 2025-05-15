import os
from pathlib import Path

def get_user_choice():
    print("Select the model you want to use:")
    print("1) WAI-NSFW-illustrious-SDXL v14.0")
    print("2) WAI-ANI-NSFW-PONYXL v14.0")   
    print("3) Hassaku XL (Illustrious) v2.2")
    print("4) Hassaku (SD1.5) v1.3")
    print("5) Nova Anime XL v7.0")
    print("6) Nova Orange XL v9.0")    
    print("7) Nova Cartoon XL v1.0")
    print("8) Nova Furry XL v7B")
    print("9) Sudachi XL (Illustrious) v1")
    print("10) Sudachi v1.0")
    print("11) Amanatsu (Illustrious) v1.1")
    choice = input("Input the number: ")
    return choice.strip()

def get_model_script_path(choice):
    model_scripts = {
        "1": "WAI-NSFW-illustrious-SDXL v14.0.py",
        "2": "WAI-ANI-NSFW-PONYXL v14.0.py",
        "3": "Hassaku XL (Illustrious) v2.2.py",
        "4": "Hassaku (SD1.5) v1.3.py",  
        "5": "Nova Anime XL v7.0.py",
        "6": "Nova Orange XL v9.0.py",
        "7": "Nova Cartoon XL v1.0.py",
        "8": "Nova Furry XL v7B.py",
        "9": "Sudachi XL (Illustrious) v1.py",
        "10": "Sudachi v1.0.py",
        "11": "Amanatsu (Illustrious) v1.1.py"
    }
    return model_scripts.get(choice)

def read_script_content(script_path):
    try:
        with open(script_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Script file not found at {script_path}")
        return None

def create_text_file(script_content, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(script_content)

def add_lora_to_text_file(file_path, lora_url):
    # Extract filename from URL
    lora_filename = lora_url.split('/')[-1].split('?')[0] + '.safetensors'
    lora_code = f'\n# Download LoRA\n!mkdir -p models/Lora\n!wget -O "models/Lora/{lora_filename}" "{lora_url}"\n'
    
    # Read the existing content
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the position before the launch command
    launch_pos = content.find('!COMMANDLINE_ARGS=')
    
    if launch_pos >= 0:
        # Insert the LoRA code before the launch command
        modified_content = content[:launch_pos] + lora_code + content[launch_pos:]
    else:
        # If launch command not found, append to end
        modified_content = content + lora_code
    
    # Write the modified content back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(modified_content)

def ask_for_lora(file_path):
    while True:
        add_lora = input("Do you wish to add some LoRA? (y/n): ").strip().lower()
        if add_lora == 'n':
            break
        elif add_lora == 'y':
            lora_url = input("Input the LoRA download URL: ").strip()
            add_lora_to_text_file(file_path, lora_url)
            
            while True:
                more_lora = input("Do you wish to add more LoRA? (y/n): ").strip().lower()
                if more_lora == 'n':
                    return
                elif more_lora == 'y':
                    lora_url = input("Input the LoRA download URL: ").strip()
                    add_lora_to_text_file(file_path, lora_url)
                else:
                    print("Please enter 'y' or 'n'.")
        else:
            print("Please enter 'y' or 'n'.")

def main():
    # Get user choice
    choice = get_user_choice()
    if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]:
        print("Invalid choice. Please select 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 or 11.")
        return
    
    # Get corresponding script filename
    script_filename = get_model_script_path(choice)
    if not script_filename:
        print("Invalid choice. No corresponding script found.")
        return
    
    # Set up paths
    current_dir = Path(__file__).parent
    script_path = current_dir / "model_scripts" / script_filename
    output_dir = current_dir / "notebooks"
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(exist_ok=True)
    
    # Read the script content
    script_content = read_script_content(script_path)
    if script_content is None:
        return
    
    # Create output text file path
    output_filename = script_filename.replace('.py', '.txt')
    output_path = output_dir / output_filename
    
    # Create the text file
    create_text_file(script_content, output_path)
    print(f"Text file created successfully at: {output_path}")
    
    # Ask about LoRA
    ask_for_lora(output_path)
    print("Script modification complete.")

if __name__ == "__main__":
    main()
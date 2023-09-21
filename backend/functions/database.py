import json
import random

# Get recent messages
def get_recent_message():
    
    # define file anme and learn instruction
    file_name ="stored_data.json"
    learn_instruction = {
        "role": "system",
        "content": "You are interviewing the user for a machine learning engineer role. Mimic a real interview and questions.",
        
    }
    
    # init messages
    messages = []
    
    # Add random elt
    x = random.uniform(0,1)
    if x < 0.2:
        learn_instruction["content"] = learn_instruction["content"] + " Your response will include some dry humor."
    else:
        learn_instruction["content"] = learn_instruction["content"] + " Your response will include a challenging question"

    # Append instruction to messages
    messages.append(learn_instruction)
    
    # Get last messages
    try:
        with open(file_name) as user_file:
            data = json.load(user_file)
            
            # Append the last 5 items of data
            if data:
                if len(data) <5:
                    for item in data:
                        messages.append(item)
                else:
                    for item in data[-5:]:
                        messages.append(item)
    except Exception as e:
        print(e)
        pass
    
    # return
    return messages
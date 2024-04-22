import time

def calculate_typing_speed(words_typed, time_taken):
    words_per_minute = (words_typed / time_taken) * 60
    return words_per_minute

def main():
    given_text = "Sometimes we're Tested not to Show our Weakness,but to Discover over Strength"
    print("Type the following text , to check your typing speed, accuracy,time taken,words typed:")
    print(given_text)
    input("Press Enter! when you're ready to start typing...")
    
    start_time = time.time()
    user_input = input("Type here: ")
    end_time = time.time()
    
    time_taken = end_time - start_time
    words_typed = len(user_input.split())
    typing_speed = calculate_typing_speed(words_typed, time_taken)
    
    accuracy = sum(a == b for a, b in zip(user_input, given_text)) / len(given_text) * 100
    
    print("\n--- Results ---")
    print("Time taken by you: {:.2f} seconds".format(time_taken))
    print("Words typed:", words_typed)
    print("your Typing speed: {:.2f} WPM".format(typing_speed))
    print("your Accuracy: {:.2f}%".format(accuracy))

if __name__ == "__main__":
    main()


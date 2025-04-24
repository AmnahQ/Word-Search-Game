
input_file = "wordDictionary.txt" 
output_file = "final_dictionary.txt" 

try:
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
           
            word = line.split("|")[0].strip()
        
            outfile.write(word + "\n")
    print(f"Words extracted successfully to {output_file}")
except FileNotFoundError:
    print(f"Error: {input_file} not found")
except Exception as e:
    print(f"An error occurred: {e}")
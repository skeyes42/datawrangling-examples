## persistance.py

This program demonstrates how to define a custom data structure using **Python Dataclasses** and how to perform **object serialization** (saving and loading) using the **pickle** module.

As of 2026, this remains a standard way to persist complex Python objects to disk. Here is the breakdown of each section:

**1. The Data Structure (@dataclass)**

The program uses the @dataclass decorator to create the StatLine class.

**Purpose**: Dataclasses automatically generate boilerplate code like \__init__() and \__repr__().

**Properties**: It defines six integer fields for basketball statistics. By defining them this way, the object is more structured than a simple dictionary or list.

**2. Object Instantiation**

The variable stat1 is an **instance** of the StatLine class, populated with specific game data (e.g., 10 field goals made out of 25 attempted).

**3. Saving the Object (pickle.dump)**

The program uses the pickle module to save the object to a file.

**wb Mode**: The file stat1.pkl is opened in **Write Binary** mode.

**Serialization**: pickle.dump() converts the Python object into a byte stream that can be stored on your hard drive. Unlike a CSV file, which only saves raw text, a "pickle" file saves the **entire object**, including its class type and structure.

**4. Clearing Memory**

del stat1 explicitly deletes the object from your computer's RAM. This is done to prove that the subsequent "Load" step is actually restoring the data from the disk, not just accessing a variable that was already there.

**5. Loading the Object (pickle.load)**

The program restores the object from the file.

**rb Mode**: The file is opened in **Read Binary** mode.

**Deserialization**: pickle.load() reconstructs the StatLine object exactly as it was. When printed, the output shows the object is fully restored with all its original attributes.

**Key Benefits for 2026 Workflows**

**Saves Everything**: You don't have to manually tell Python that FGM is an integer when you reload it; the object "remembers" its schema.

**Ease of Use**: It is much faster to code than manual JSON or CSV parsing for complex, nested objects.

**Integration**: Pickling is the foundation for saving models in libraries like Scikit-Learn.

**Warning:** Only unpickle files you trust. Loading a malicious pickle file can execute arbitrary code on your system. For sharing data across different programming languages or untrusted sources, consider using JSON or Parquet.

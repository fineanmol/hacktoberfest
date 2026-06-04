
# Python Program to Implement a Phone
# Directory Using Trie Data Structure
 
class TrieNode:
    def __init__(self):
       
        # Each Trie Node contains a Map 'child'
        # where each alphabet points to a Trie
        # Node.
        self.child = {}
        self.is_last = False
 
# Making root NULL for ease so that it doesn't
# have to be passed to all functions.
root = TrieNode()
 
# Insert a Contact into the Trie
def insert(string):
   
    # 'itr' is used to iterate the Trie Nodes
    itr = root
    for char in string:
       
        # Check if the s[i] is already present in
        # Trie
        if char not in itr.child:
           
            #  If not found then create a new TrieNode
            itr.child[char] = TrieNode()
             
        # Move the iterator('itr') ,to point to next
        # Trie Node
        itr = itr.child[char]
         
    # If its the last character of the string 's'
    # then mark 'isLast' as true
    itr.is_last = True
 
# This function simply displays all dictionary words
# going through current node. String 'prefix'
# represents string corresponding to the path from
# root to curNode.
def display_contacts_util(cur_node, prefix):
   
    # Check if the string 'prefix' ends at this Node
    # If yes then display the string found so far
    if cur_node.is_last:
        print(prefix)
         
    # Find all the adjacent Nodes to the current
    # Node and then call the function recursively
    # This is similar to performing DFS on a graph
    for i in range(ord('a'), ord('z') + 1):
        char = chr(i)
        next_node = cur_node.child.get(char)
        if next_node:
            display_contacts_util(next_node, prefix + char)
             
# Display suggestions after every character enter by
# the user for a given query string 'str'
def displayContacts(string):
    prev_node = root
    prefix = ""
     
    # Display the contact List for string formed
    # after entering every character
    for i, char in enumerate(string):
       
        # 'prefix' stores the string formed so far
        prefix += char
         
        # Find the Node corresponding to the last
        # character of 'prefix' which is pointed by
        # prevNode of the Trie
        cur_node = prev_node.child.get(char)
         
        # If nothing found, then break the loop as
        # no more prefixes are going to be present.
        if not cur_node:
            print(f"No Results Found for {prefix}\n")
            break
        # If present in trie then display all
        # the contacts with given prefix.
        print(f"Suggestions based on {prefix} are ",end=" ")
        display_contacts_util(cur_node, prefix)
        print()
        # Change prevNode for next prefix
        prev_node = cur_node
         
    # Once search fails for a prefix, we print
    # "Not Results Found" for all remaining
    # characters of current query string "str".
    for char in string[i+1:]:
        prefix += char
        print(f"No Results Found for {prefix}\n")
 
# Insert all the Contacts into the Trie
def insertIntoTrie(contacts):
    # Insert each contact into the trie
    for contact in contacts:
        insert(contact)
 
         
# Driver program to test above functions
 
# Contact list of the User        
contacts=["gforgeeks","geeksquiz"]
 
# Size of the Contact List
n=len(contacts)
 
# Insert all the Contacts into Trie
insertIntoTrie(contacts)
query = "gekk"
 
# Note that the user will enter 'g' then 'e', so
# first display all the strings with prefix as 'g'
# and then all the strings with prefix as 'ge'
displayContacts(query)
